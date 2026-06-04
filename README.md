# 🪐 Gemini Studio · Text-to-Image Generator

> **AI 輔助程式開發（AI-Assisted Development）實作作業**  
> 使用 Antigravity IDE 內建的 AI Agent 加速完成本專案開發

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://l5b-hw3-ef8dqoh7rawjyieqhjxbsi.streamlit.app/)

**🌐 線上體驗網址：[https://l5b-hw3-ef8dqoh7rawjyieqhjxbsi.streamlit.app/](https://l5b-hw3-ef8dqoh7rawjyieqhjxbsi.streamlit.app/)**

---

> [!IMPORTANT]
> **📢 關於 Gemini API 機制與免費生圖管道的致歉與修正說明**
> 
> 這是我需要向你致歉並修正的地方。我先前的說明**有些混淆了 Google 不同的產品線，對 Gemini API 的機制給出了錯誤的解釋**。
> 
> 為了不讓你多花冤枉錢，請以下面最新的官方邏輯為準：
> 
> ### 1. 修正：Gemini API 只要一綁定，就「沒有」免費圖了
> 
> 我之前提到的「每天免費生 25 張圖，綁卡驗證解鎖」其實是**混淆了 ChatGPT/Claude 那類網頁版訂閱制、或是 Google Vertex AI 的某些企業試用機制**。
> 
> 在 **Google AI Studio (Gemini API)** 的官方定價規則中：
> 
> * **純文字/多模態輸入模型**（如 `gemini-2.0-flash` 的純文字或圖片讀取）：確實有提供**完全免費的額度（Free Tier）**。
> * **生圖或多媒體生成模型**（例如 Imagen 系列模型）：官方定價中通常顯示 **Free Tier「無法使用（Not Available）」**。這意味著生圖這類高成本的功能，**只要你沒儲值，在免費層級下是完全沒辦法呼叫的**。
> 
> ### 2. 你現在的狀態是什麼？
> 
> 從你提供的第二張截圖來看，你已經成功把專案升級到了 **Paid 1（付費第 1 級）**。
> 
> * **在 Paid Tier（付費層級）下：** 所有的請求（包含文字、生圖）都**不再享有任何免費額度**，而是完全改為「按量計費（Pay-as-you-go）」，也就是從頭開始每呼叫一次就扣一次錢。
> * **因為你目前餘額是 NT$0：** 雖然你已經切換成付費管道，但系統一查發現裡面沒錢可以扣，所以你在呼叫 API 時，它才會繼續噴 429 錯誤或拒絕連線。
> 
> ---
> 
> ### 🛠️ 結論與建議
> 
> 如果你今天原本的目的是「想要一毛錢都不花，只用免費額度」：
> 
> > 💡 **解決方法：** 請點擊左側選單的 **Projects** 或 **API Keys**，看看能不能把這個專案的計費層級改回 **Free**，或者直接**重新建立一個新的 API Key/新專案**。只要在「免費層級（Free Tier）」下，你就可以繼續免費呼叫 `gemini-2.0-flash` 等文字模型的免費額度（但請記得，免費層級沒辦法用來生成圖片）。
> 
> 如果你本來就打算**花點小錢買順暢、或真的需要呼叫生圖模型**：
> 
> > 💡 **解決方法：** 那你就必須點選 **Buy credits** 至少儲值最低金額（官方規定最低為 $10 美元，約台幣 NT$300 多元，你也可以自訂 Other amount，不一定要選畫面上的 NT$1,000）。儲值完成後，你的 Paid 1 就會正式運作，程式便能正常跑通。
> 
> ---
> 
> ### 🌍 網路上的其他免費生圖管道（2026年最主流推薦）
> 
> 有的，網路上其實有非常多**完全免費**、或者**提供每日免費額度**的強大生圖工具。如果你不想在 Google AI Studio 儲值，可以試試看以下幾個目前（2026年）最主流且好用的免費管道：
> 
> #### 1. 免費額度最慷慨：微軟 Microsoft Designer (Bing Image Creator)
> 
> * **核心模型**：DALL-E 3 / GPT Image 系列。
> * **免費機制**：只要登入微軟帳號就能**完全免費、無限次生成**！
> * **特點**：每天會送你 15~25 個「快速生成點數（Boosts）」，點數用完只是生成速度變慢（需要等 30~60 秒），但**依然可以繼續畫，不限張數**。它對中文的理解能力很好，畫風也很均衡。
> 
> #### 2. 想要繼續用 Google 的最新生圖模型：網頁版 Google Gemini (非 API)
> 
> * **核心模型**：Imagen 3 / Nano Banana 2
> * **免費機制**：去一般的 **[Google Gemini 網頁版/App](https://gemini.google.com/)**，直接用聊天對話的方式叫它畫圖。
> * **特點**：雖然 API 專案要收費，但**消費級的 Gemini 網頁版 App 是有提供每日免費生圖額度的（有每日上限）**。這裡使用的通常就是 Google 最新引以為傲、物理擬真度極高的影像模型。
> 
> #### 3. 字體渲染、標誌設計最強：Ideogram
> 
> * **核心模型**：Ideogram 3.0
> * **免費機制**：每天免費提供約 10 次生成機會（一次出 4 張圖，一天約 40 張）。
> * **特點**：如果你的圖片裡需要出現**精準、不扭曲的英文單字或句子**（例如設計 Logo、海報、路標），Ideogram 是目前公認全行業最強的模型。
> 
> #### 4. 寫實與動漫風格頂級：Leonardo.ai
> 
> * **核心模型**：Phoenix 模型 / 支援 FLUX
> * **免費機制**：每天自動重置 **150 個免費代幣**（大概可以免費生 15~30 張高品質圖）。
> * **特點**：非常適合拿來畫遊戲道具、動漫風格、3D 盲盒或極致寫實的人像。它還內建畫布編輯器，功能非常專業。
> 
> #### 5. 開源黑馬免費體驗：FLUX 相關線上 Demo
> 
> * **核心模型**：FLUX 2.0 (Schnell / Dev)
> * **免費機制**：FLUX 是目前最強大的開源生圖模型，在 **Hugging Face Spaces** 或 **Together.ai / Replicate** 等平台上都有開發者提供的免費 Demo 網頁可以無限或有限度地試用。
> * **特點**：細節處理和肢體、手指的擬真度甚至超越舊版的 Midjourney。
> 
> ---
> 
> #### 💡 總結建議
> 
> * 如果你想要**完全不用管額度、隨便畫** ➡️ 首選 **Microsoft Designer (Bing)**。
> * 如果你想試試 **Google 最新的物理寫實與人像一致性** ➡️ 直接去 **Gemini 網頁版** 呼叫它生圖。
> * 如果想要圖片裡有**完美的藝術字體** ➡️ 用 **Ideogram**。

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
