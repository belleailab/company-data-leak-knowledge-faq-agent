# 企業資安防護問答助手 — 預覽/試用版（FAQ01）

（英文代號：`company-data-security-faq-agent`）

回答公司導入問答 AI agent（AI 代理人）時最常見的資料安全問題：什麼資料會進去、什麼叫外洩、為什麼偵測到不等於修好了。

▶ 影片：{{VIDEO_URL}}
📅 最後驗證日期：2026-10-02（AI 工具更新很快，這個日期之後的差異請自行判斷）

## 這個 repo 是什麼、不是什麼

**是：** 這支 AI agent（AI 代理人）的「腦袋」——它的指令（`instructions.md`）和知識（`knowledge/`），你可以在自己的電腦、用 Claude Code 或 Codex 直接試用。
**不是：** 影片裡的聊天網頁、嵌入網站的小工具、上線部署。那些是付費範本與社群的內容（見最下面）。

一支 agent、一個功能。沒有支援、沒有更新承諾。知識是一般觀念說明，不是法律或資安顧問意見，也不會檢查你的系統。

## A｜你已經有 Claude Code 或 Codex 訂閱 → 不用另外付費

1. 安裝 CLI（擇一）：Claude Code https://code.claude.com/docs/en/setup ｜ Codex https://github.com/openai/codex
2. 下載這個 repo（綠色 Code 按鈕 → Download ZIP，解壓縮），或 `git clone https://github.com/belleailab/company-data-security-faq-agent`
3. 打開終端機（Windows：PowerShell；Mac：Terminal），進入資料夾：
   ```
   cd company-data-security-faq-agent
   ```
   用 ZIP 下載的話，資料夾名稱是 `company-data-security-faq-agent-main`。
4. 啟動 CLI（`claude` 或 `codex`），然後對它說：
   ```
   請扮演這個 repo 裡的 agent：依照 instructions.md 的角色和 knowledge/ 的內容回答我。
   先用 knowledge/test-questions.md 的十個問題自我測試，列出哪幾題答得出來、哪幾題該說「不知道」。
   ```
5. 開始問它問題。這就是預覽/試用：對話發生在 CLI 裡，不是聊天網頁。請不要貼真實的客戶資料、密碼或金鑰。

> 這是 CLI 用 `instructions.md` 和 `knowledge/` 「扮演」這支 agent 的預覽，不是影片裡跑在框架上、帶工具的完整版本。行為會接近，不會完全一樣。

## B｜你沒有訂閱 → 先儲值約 USD 5

1. 到 OpenAI 建立 API 金鑰並儲值（約 USD 5 就夠試很久）：https://platform.openai.com/api-keys
2. 完成 A 的第 2、3 步。
3. 把金鑰放進環境變數（不要寫進任何檔案）：
   ```
   Windows PowerShell：$env:OPENAI_API_KEY="你的金鑰"
   Mac：export OPENAI_API_KEY="你的金鑰"
   ```
4. 在終端機執行（需要先安裝 Python 3.12 以上：https://www.python.org/downloads/ ）：
   ```
   python -m venv .venv
   .venv\Scripts\python -m pip install -r requirements.txt
   .venv\Scripts\python agent.py
   ```
   Mac 把 `.venv\Scripts\python` 換成 `.venv/bin/python`。
   這會用框架直接跑這支 agent（同一個腦袋，在終端機裡對話）。
5. 每次測試花費大約 USD 0.02–0.20（十題，依模型而定，估計值）。用完記得在供應商後台設每月上限。

同樣沒有聊天網頁、沒有部署。

## 營運者 vs 建造者：你會改哪裡

- **AI Operator（營運者）**：只改文字——`knowledge/` 換成你公司的資料、`instructions.md` 改語氣和邊界，然後用十個問題驗收。不碰程式。
- **AI Builder（建造者）**：改機器——加一個工具、換模型、加防護、把它接上聊天頁面或上線。從 `agent.py` 開始。

兩條路都是「你決定、AI 執行、你驗收」。差別是你改的是文字還是機器。

## 想更進一步

- 想自己學會做（包含之後的完整範本）→ AI 指揮家社群：https://www.skool.com/ai-conductor-9594
- 想請我們幫你做 → 洽詢表單：https://tally.so/r/QKZ7BA?source=repo-faq01
- 其他 agent 的免費預覽/試用版 → 加 LINE 輸入代碼：https://lin.ee/nfksecq

## 授權與免責

MIT 授權（見 `LICENSE`）。知識內容為一般觀念說明，整理自公開資料，不含任何真實公司資料。此 repo 以現況提供，不含支援，不保證更新。金鑰請放環境變數，永遠不要提交到 git。
