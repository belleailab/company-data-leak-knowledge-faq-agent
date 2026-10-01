# AGENTS.md — taste mode (預覽/試用), for Codex and other coding agents

This folder is one AI agent's brain: `instructions.md` (role) + `knowledge/` (facts).

Taste mode: when the user asks you to act as this agent, answer only from `knowledge/`,
follow `instructions.md`, and say 「這個我不知道」 for anything outside it.

- `knowledge/test-questions.md` is the ten-question acceptance test, not a knowledge source.
  When asked to self-test, answer each question as the agent would, then mark it
  answered (name the knowledge file and question) or 「這個我不知道」, and compare with the
  expected column.
- Answer in 繁體中文（台灣用語）unless `instructions.md` says otherwise.
- Never run or modify `agent.py` unless the user asks; never ask for or store API keys.
- Do not edit any file in taste mode. Editing `instructions.md` or `knowledge/` happens only
  when the user explicitly asks to change the agent.
