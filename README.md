# 🪐 Gemini Studio · Text-to-Image Generator

> **AI 輔助程式開發（AI-Assisted Development）實作作業**  
> 使用 Antigravity IDE 內建的 AI Agent 加速完成本專案開發

---

## 🔗 線上體驗網址
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://l5b-hw3-ef8dqoh7rawjyieqhjxbsi.streamlit.app/)  
**👉 [點此開啟網頁應用程式](https://l5b-hw3-ef8dqoh7rawjyieqhjxbsi.streamlit.app/)**

---

## 📖 專案簡介

本專案是一個基於 **Python + Streamlit** 建立的 Text-to-Image 生圖網頁應用程式。為了解決使用者在免費額度與進階繪圖需求之間的平衡，本系統整合了兩種獨立的生圖引擎：

1. **🎨 Microsoft Designer (Bing) — 100% 免費且免金鑰**：
   - 適合想要快速、免登入、無限制次數生圖的使用者。
   - 基於微軟 DALL-E 3 圖像生成技術，對中文描述理解力強，物理擬真度高。
2. **🪐 Google Gemini 3.1 Flash Image — 進階付費繪圖**：
   - 適合需要進行專業 API 整合，或體驗 Google 原生多模態編輯的使用者。
   - 使用 `gemini-3.1-flash-image` 模型，需要使用者提供個人的 Google AI Studio API Key，且該專案必須**啟用帳單與信用卡儲值**。

### ✨ 主要功能
* **雙引擎切換**：可隨時切換免費的微軟引擎與付費的 Gemini 引擎。
* **藝術風格預設 (Art Style)**：提供科幻宇宙、賽博龐克、奇幻史詩、寫實攝影、動漫風格等多種預設詞綴。
* **尺寸比例調整 (Aspect Ratio)**：支援 1:1 正方形、16:9 寬螢幕、9:16 直幅比例。
* **隨機靈感 (Inspire)**：內建多個創意 Prompt，一鍵激發創作靈感。
* **作品管理與下載**：生圖完成後可直接下載高品質 PNG 檔，並內建最近 20 筆歷史生成紀錄的歷史畫廊，支援一鍵載回與獨立下載。
* **金鑰診斷面板**：提供視覺化的 API 連線與權限診斷，即時查驗金鑰可用模型與帳單權限。

---

## 🛠️ 技術棧

* **前端與應用框架**：[Streamlit](https://streamlit.io/) (Python)
* **AI 生圖模型**：
  * `gemini-3.1-flash-image` (Google Gemini 3.1 付費生圖模型)
  * Microsoft Designer (Bing 備用免費生圖管道)
* **API 整合**：[Google AI Studio](https://aistudio.google.com/) Gemini API (REST Endpoint)
* **部署平台**：Streamlit Community Cloud

---

## 🚀 部署流程

本專案採用 **GitHub 儲存庫 ➜ Streamlit Community Cloud** 雲端部署，幾分鐘內即可完成發布：

### Step 1｜準備本地專案檔案
在專案資料夾中，確保包含以下核心檔案：
* **`app.py`**：主要應用邏輯程式碼。
* **`requirements.txt`**：套件依賴清單。其內容如下：
  ```
  streamlit>=1.35.0
  requests>=2.31.0
  Pillow>=10.0.0
  ```
* **`.streamlit/config.toml`**：主題設定（深空暗色主題）。
* **`.gitignore`**：排除敏感的本機 secrets 設定檔。

### Step 2｜程式碼上傳 GitHub
```bash
git init
git remote add origin https://github.com/KevinLin13/L5B-HW3.git
git add app.py requirements.txt .streamlit/config.toml .gitignore
git commit -m "feat: Gemini Studio Text-to-Image app"
git push -u origin master
```

### Step 3｜在 Streamlit Community Cloud 上部署
1. 登入 [share.streamlit.io](https://share.streamlit.io) 並連動 GitHub 帳號。
2. 點擊 **"New app"**，設定專案參數：
   * **Repository**：`KevinLin13/L5B-HW3`
   * **Branch**：`master`
   * **Main file path**：`app.py`
3. 點擊 **"Advanced settings" ➜ "Secrets"**，貼上您在 AI Studio 申請的 API Key：
   ```toml
   GOOGLE_API_KEY = "AIzaSy...（您的 API 金鑰）"
   ```
4. 點擊 **"Deploy!"** 進行部署，完成後即可獲取公開網址。

---

## 📁 專案結構

```
L5B-HW3/
├── app.py                    # 主程式（Streamlit 應用與 API 邏輯）
├── requirements.txt          # Python 套件依賴清單
├── .gitignore                # Git 排除清單
└── .streamlit/
    ├── config.toml           # Streamlit 深空暗色主題設定
    └── secrets.toml          # 本地端金鑰設定檔（已加入 gitignore，防止洩漏）
```

---

## 🔑 API 金鑰取得方式

若要使用 Google Gemini 3.1 生圖引擎，請遵循以下步驟取得金鑰：

1. 前往 **[Google AI Studio](https://aistudio.google.com/)**。
2. 點擊左上角 **"Get API key"**。
3. 選擇 **"Create API key in new project"** 建立一個新的 Google Cloud 專案金鑰。
4. 複製產生的金鑰（格式為 `AIzaSy...`）。
5. 在本系統上方的「🔑 Set Key」折疊面板中輸入並保存，或在雲端部署時加入為 `GOOGLE_API_KEY` Secret。

---

## 💡 開發心得：AI 輔助開發流程

本專案全程使用 **Antigravity IDE** 內建的 AI Agent 進行開發，實踐了現代化的 AI 協同開發模式：

1. **視覺參考與框架轉譯**：參考 React (.tsx) 版型的視覺排版，引導 AI 將其轉譯為 Python Streamlit 的網頁架構，大幅縮短了原型建置時間。
2. **多模式架構設計**：透過 AI 協助快速整合多個生圖 API（包含 Microsoft Designer 與 Gemini v1beta REST 路由），並設計了輕量、不重刷頁面的狀態回呼與診斷面板。
3. **錯誤攔截與透明排查**：在測試中發現了 Streamlit 狀態同步 bug（Inspire 按鈕導致的文字域不更新問題），AI 能夠精確定位 Streamlit 內部 session_state 的生命週期並給出覆寫 key 的修正方案。

---

## ⚠️ 注意事項

### 1. Gemini API 生圖計費規則重要說明
> [!IMPORTANT]
> **Gemini API 的「程式碼串接（API 呼叫）」沒有提供免費的生圖額度。**
> * 雖然 Gemini API 在文字對話與多模態輸入（如圖片辨識、影片分析）上有提供免費方案（Free Tier），但**生圖模型（Imagen 4 系列或 `gemini-3.1-flash-image`）從第一張圖片開始就會直接計費**。
> * **啟用方式**：您必須登入 [Google Cloud Console Billing](https://console.cloud.google.com/billing) 將您的金鑰專案連結到已啟用信用卡的**付費帳單帳戶（Paid Tier）**。
> * **計費價格**：基本款 `Imagen 4 Fast` 每張約 `$0.02` 美元；支援原生多模態的 `Gemini 3.1 Flash Image` 1024px 每張約 `$0.067` 美元（批次處理折半）。
> * **免費替代方案**：若不想綁定信用卡或儲值，請使用專案內建的 **Microsoft Designer (Bing)** 引擎，可享 100% 免費生圖。

### 2. Gemini 3.1 API 呼叫上限 (Tier 1 速率限制)
| 模型識別碼 (Model ID) | 類別 | 每分鐘請求數 (RPM) | 每天最大請求數 (RPD) | 每分鐘 Token 數 (TPM) |
|---|---|---|---|---|
| **Gemini 3.1 Flash Image** | AI 影像生成 | 100 RPM | 1,000 RPD | 200,000 TPM |
| **Imagen 4 Generate** | 舊版影像生成 | 10 RPM | 70 RPD | - |

### 3. 常見錯誤與排除對策
| 錯誤代碼 / 訊息 | 可能原因 | 排除對策 |
|---|---|---|
| `429 Quota exceeded, limit: 0` | 您的 API 專案未連結付費帳單或餘額為 0 | 1. 請至 Google Cloud 啟用帳單帳戶並儲值。<br>2. 或者切換回免金鑰的 **Microsoft Designer (Bing)** 免費引擎。 |
| `401 / 403 Invalid API key` | API Key 複製錯誤或已失效 | 請至 AI Studio 重新複製正確的 Key 並貼上。 |
| `No image returned` | Prompt 內容觸發安全敏感詞過濾 | 修改您的 Prompt 描述，避免敏感或不當詞彙。 |

---

*Built with ❤️ using Antigravity IDE AI Agent + Google Gemini 3.1 + Streamlit*
