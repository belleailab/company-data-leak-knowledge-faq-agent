"""Terminal runner for this agent (README path B).

Runs the same agent brain (instructions.md + knowledge/) on the agency-swarm
framework, as a conversation in your terminal.

    pip install -r requirements.txt
    python agent.py

A real conversation calls a paid model API with YOUR OpenAI key. Without a key
this script stops before any call and tells you what to do.

AI Operator: you never need to edit this file. Change instructions.md and the
files in knowledge/ instead; this runner reads them every time it starts.
AI Builder: this is where you add tools, swap the model, or add guardrails.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INSTRUCTIONS_FILE = ROOT / "instructions.md"
KNOWLEDGE_DIR = ROOT / "knowledge"
# The acceptance test is not knowledge: the agent must not read the answers.
TEST_QUESTIONS_FILE = "test-questions.md"
PINNED_FRAMEWORK_VERSION = "1.11.0"


def _use_utf8_output() -> None:
    """Print Traditional Chinese safely, also when output goes to a file or pipe."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def _fail(title: str, body: str) -> int:
    """Print a readable error and return the exit code 1."""
    print(f"\n{title}\n{'-' * len(title)}\n{body}\n", file=sys.stderr)
    return 1


def read_agent_name(instructions: str) -> str:
    """Use the first '# ' heading of instructions.md as the agent's display name."""
    for line in instructions.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "FAQ agent"


def framework_agent_id() -> str:
    """A plain-ASCII id for the framework (the folder name), safe for any API field."""
    return re.sub(r"[^A-Za-z0-9_-]+", "-", ROOT.name).strip("-") or "faq-agent"


def build_instructions() -> str:
    """instructions.md followed by every knowledge file except the test questions."""
    parts = [INSTRUCTIONS_FILE.read_text(encoding="utf-8").strip()]
    for path in sorted(KNOWLEDGE_DIR.glob("*.md")):
        if path.name == TEST_QUESTIONS_FILE:
            continue
        parts.append(f"## 知識檔案：knowledge/{path.name}\n\n{path.read_text(encoding='utf-8').strip()}")
    return "\n\n---\n\n".join(parts)


def main() -> int:
    _use_utf8_output()

    # 1. The framework must be installed.
    try:
        from agency_swarm import Agency, Agent
        from dotenv import load_dotenv
    except ImportError:
        return _fail(
            "還沒安裝框架 / Framework not installed",
            "請先在這個資料夾執行：\n"
            "  pip install -r requirements.txt\n"
            "Run `pip install -r requirements.txt` in this folder first.",
        )

    try:
        from importlib.metadata import version

        installed = version("agency-swarm")
    except Exception:
        installed = "unknown"
    if installed != PINNED_FRAMEWORK_VERSION:
        print(
            f"注意：這個 repo 用 agency-swarm {PINNED_FRAMEWORK_VERSION} 測試，"
            f"你裝的是 {installed}。建議用 requirements.txt 重新安裝。\n",
            file=sys.stderr,
        )

    # 2. The key must be set. Nothing has been sent anywhere yet.
    load_dotenv(ROOT / ".env")  # optional; an environment variable works too
    if not os.environ.get("OPENAI_API_KEY", "").strip():
        return _fail(
            "還沒設定 API 金鑰 / OPENAI_API_KEY is not set",
            "這一步會呼叫付費的模型 API，所以需要你自己的 OpenAI 金鑰。\n"
            "沒有送出任何請求，也沒有產生任何費用。\n\n"
            "設定方式（擇一，不要把金鑰寫進 git）：\n"
            '  Windows PowerShell：$env:OPENAI_API_KEY="你的金鑰"\n'
            '  Mac / Linux：      export OPENAI_API_KEY="你的金鑰"\n'
            "  或複製 .env.example 成 .env，把金鑰填在 OPENAI_API_KEY= 後面\n\n"
            "No request was sent and nothing was charged. Set OPENAI_API_KEY, then run again.\n"
            "No key and no subscription? See README path B.",
        )

    # 3. Build the agent from the two text sources and open the conversation.
    instructions = build_instructions()
    name = read_agent_name(instructions)
    kwargs = {
        "name": framework_agent_id(),
        "description": f"{name}：只根據 knowledge/ 回答的 FAQ agent。",
        "instructions": instructions,
    }
    model = os.environ.get("AGENT_MODEL", "").strip()
    if model:
        kwargs["model"] = model

    agent = Agent(**kwargs)
    agency = Agency(agent, name=f"{framework_agent_id()} (preview)")

    shown_model = model or f"框架預設 / framework default ({getattr(agent, 'model', 'unknown')})"
    print(f"啟動 {name}（agency-swarm {installed}，模型：{shown_model}）")
    print("這會呼叫付費的模型 API。按 Ctrl+C 結束。\n")
    agency.terminal_demo()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
