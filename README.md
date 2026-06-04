# 🪐 Gemini Studio · Text-to-Image Generator

> **AI 輔助程式開發（AI-Assisted Development）實作作業**  
> 使用 Antigravity IDE 內建的 AI Agent 加速完成本專案開發

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://l5b-hw3-ef8dqoh7rawjyieqhjxbsi.streamlit.app/)

**🌐 線上體驗網址：[https://l5b-hw3-ef8dqoh7rawjyieqhjxbsi.streamlit.app/](https://l5b-hw3-ef8dqoh7rawjyieqhjxbsi.streamlit.app/)**

---

## 📖 專案簡介

本專案是一個基於 **Python + Streamlit** 建立的 Text-to-Image 生圖網頁應用程式，串接 **Google Gemini 3.1 Flash Image** 模型進行 AI 繪圖（免費方案可用）。使用者可透過自然語言描述（中文或英文），由 AI 自動生成對應的高品質圖像。

### ✨ 主要功能

| 功能 | 說明 |
|------|------|
| 🔮 AI Enhance Prompt | 使用 Gemini 3.5 Flash 將中文或簡單描述自動翻譯、擴寫為高品質英文 Prompt |
| 🎨 Art Style 風格選擇 | 無風格 / 宇宙科幻 / 賽博龐克 / 奇幻史詩 / 寫實攝影 / 動漫風格 |
| 📐 Aspect Ratio 尺寸 | 1:1 正方形 / 16:9 橫幅 / 9:16 直幅 |
| 💡 Inspire Me | 隨機生成靈感提示詞 |
| 🚀 Gemini 3.1 Flash 生圖 | 呼叫 Gemini 3.1 Flash Image 引擎（**免費配額可用**） |
| ⬇️ 下載圖片 | 一鍵下載 PNG 格式圖像 |
| 🌌 歷史紀錄 | 保留最近 20 筆生成紀錄，可一鍵重載或個別下載 |

---

## 🛠️ 技術棧

- **框架**：[Streamlit](https://streamlit.io/) (Python)
- **生圖模型**：`gemini-3.1-flash-image`（**Google 免費配額可用**）
- **Prompt 優化**：`gemini-3.5-flash`（免費配額較大）
- **API**：[Google AI Studio](https://aistudio.google.com/) Gemini API
- **部署平台**：Streamlit Community Cloud

> ⚠️ **注意**：本專案已改用 `gemini-3.1-flash-image`，**使用 Google AI Studio 免費 API Key 即可生圖**。

---

## 🚀 部署流程

本專案採用目前最便利、也最主流的 Streamlit 部署方式：

```
本地寫好程式  →  Push 到 GitHub  →  串接 Streamlit Community Cloud 完成部署
```

> ⚠️ **關鍵技術細節**：Streamlit 是基於 **Python** 的網頁框架。  
> 上傳的主程式應為 `.py` 檔（`app.py`），而非前端 React 採用的 `.tsx` 檔。  
> 如果參考 React 版型，需要「**用 Python Streamlit 重寫**」，而非直接上傳 `.tsx`。

### Streamlit 部署 4 步驟

#### Step 1｜準備專案檔案（本地端）

在專案資料夾中，至少需要準備以下兩個核心檔案：

- **主程式檔案（`app.py`）**：用 Python 撰寫的 Streamlit 程式碼
- **套件清單（`requirements.txt`）**：告訴 Streamlit 伺服器需要安裝哪些 Python 套件

> 💡 **小技巧**：在終端機輸入 `pip freeze > requirements.txt` 可自動產生套件清單，  
> 或手動建立文字檔，寫入需要的套件名稱。

本專案的 `requirements.txt`：
```
streamlit>=1.35.0
requests>=2.31.0
Pillow>=10.0.0
```

#### Step 2｜將程式碼 Push 到 GitHub

```bash
git init
git remote add origin https://github.com/KevinLin13/L5B-HW3.git
git add app.py requirements.txt .streamlit/config.toml .gitignore
git commit -m "feat: Gemini Studio Text-to-Image app"
git push -u origin master
```

#### Step 3｜登入 Streamlit Community Cloud

1. 前往 [share.streamlit.io](https://share.streamlit.io)
2. 點擊 **"Sign in"** → 選擇 **"Continue with GitHub"** 連動登入

#### Step 4｜串接與發布

1. 登入後點擊右上角 **"New app"**
2. 設定部署參數：
   - **Repository**：`KevinLin13/L5B-HW3`
   - **Branch**：`master`
   - **Main file path**：`app.py`
3. 點擊 **"Advanced settings" → "Secrets"**，填入 API 金鑰：
   ```toml
   GOOGLE_API_KEY = "AIza...你的金鑰..."
   ```
4. 點擊 **"Deploy!"**，幾分鐘後即可獲得公開網址

---

## 📁 專案結構

```
L5B-HW3/
├── app.py                    # 主程式（Streamlit + Gemini API）
├── requirements.txt          # Python 套件清單
├── .gitignore                # 排除敏感檔案（secrets.toml 不上傳）
└── .streamlit/
    ├── config.toml           # Streamlit 主題設定（深空暗色）
    └── secrets.toml          # 本機測試用金鑰（不上傳 GitHub）
```

---

## 🔑 API 金鑰取得方式

1. 前往 [aistudio.google.com](https://aistudio.google.com/)
2. 點擊 **"Get API key"** → **"Create API key in new project"**（建立全新專案以確保有免費配額）
3. 複製金鑰（格式為 `AIza...`）
4. 在 Streamlit app 上方的「🔑 Set Key」輸入金鑰，或部署時設定為 Secret

> 🔒 **安全提醒**：API 金鑰僅存在於瀏覽器 Session，不會儲存在伺服器端。

### 常見錯誤排解

| `429 Quota exceeded, limit: 0` (生圖模型) | API 專案未啟用 Google Cloud 帳單 | 1. 登入 [Google Cloud Console Billing](https://console.cloud.google.com/billing) 將此專案與信用卡連結以開啟付費方案。<br>2. 亦可在 App 設定金鑰處點擊 **🔍 Run API Diagnostics** 進行權限診斷。 |
| `429 Quota exceeded, limit: 0` (對話模型) | API Key 所在專案沒有免費配額 | 至 aistudio.google.com 重新建立 Key，選「**Create API key in new project**」以重置免費額度。 |
| `401 / 403 Invalid API key` | 金鑰錯誤或已失效 | 重新複製正確的 Key 並貼上 |
| `No image returned` | Prompt 觸發安全過濾 | 修改 Prompt，避免敏感詞彙 |

---

## 💡 開發心得：AI 輔助開發流程

本作業使用 **Antigravity IDE** 內建的 AI Agent 完成，體驗了現代 AI 輔助程式開發流程：

1. 用自然語言描述需求（Prompt Engineering）
2. AI 自動生成完整的 `app.py` 程式碼與 `requirements.txt`
3. 人工審閱、調整並修正細節
4. 透過 AI 協助完成 Git 操作與 GitHub 推送
5. 部署至 Streamlit Community Cloud

> **關鍵技術修正 Prompt**：  
> *"I want to create a Python Streamlit web app for Text-to-Image generation. We will use Google's Gemini model (`gemini-3.1-flash-image`) for image generation. Please help me build the app as a single `app.py` file, incorporating text inputs and image displays inspired by the layout of `text_to_image_app.tsx`, so that it can be deployed directly to streamlit.io. Please provide the Python code and `requirements.txt`."*
>
> 重點：明確指定「用 Python Streamlit（`app.py`）重寫，**參考** React 版型的視覺佈局，而非直接上傳 `.tsx`」，並指定免費的 Gemini 圖像生成模型，這樣 AI 才能生成正確可執行的程式碼。

---

*Built with ❤️ using Antigravity IDE AI Agent + Google Gemini 3.1 & 3.5 + Streamlit*
