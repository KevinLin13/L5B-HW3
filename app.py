"""
╔══════════════════════════════════════════════════════════╗
║         Gemini Studio · Text-to-Image Generator          ║
║         Powered by Google Imagen 4 via Gemini API        ║
║         Inspired by text_to_image_app.tsx layout         ║
║         Deploy directly to streamlit.io                  ║
╚══════════════════════════════════════════════════════════╝
"""

import streamlit as st
import requests
import base64
import time
import random
import uuid
from datetime import datetime
from io import BytesIO
from PIL import Image

# ═══════════════════════════════════════════════════════════
# PAGE CONFIG  ← must be the very first Streamlit call
# ═══════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Gemini Studio · AI Image Generator",
    page_icon="🪐",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════
# GLOBAL CSS — Deep-space dark theme
# ═══════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ── Reset ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    color: #e2e8f0;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 0.8rem !important;
    padding-bottom: 5rem !important;
    max-width: 680px !important;
}

/* ── Animated space background ── */
.stApp {
    background:
        radial-gradient(ellipse 90% 50% at 50% -15%, rgba(99,65,230,0.22) 0%, transparent 65%),
        radial-gradient(ellipse 50% 30% at 85% 60%, rgba(236,72,153,0.08) 0%, transparent 55%),
        linear-gradient(180deg, #020617 0%, #050d1f 60%, #020617 100%);
    min-height: 100vh;
}

/* ── Hero header ── */
.hero-wrap {
    display: flex; align-items: center; gap: 14px;
    padding: 14px 0 12px;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 20px;
}
.hero-logo {
    width: 46px; height: 46px; border-radius: 14px; flex-shrink: 0;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #db2777 100%);
    display: flex; align-items: center; justify-content: center;
    font-size: 22px;
    box-shadow: 0 0 0 0 rgba(99,102,241,0.5);
    animation: heroPulse 3s ease-in-out infinite;
}
@keyframes heroPulse {
    0%,100% { box-shadow: 0 0 18px rgba(99,102,241,0.45); }
    50%      { box-shadow: 0 0 38px rgba(168,85,247,0.7), 0 0 60px rgba(99,102,241,0.2); }
}
.hero-text { flex: 1; }
.hero-title {
    font-size: 1.15rem; font-weight: 900; line-height: 1.1;
    background: linear-gradient(90deg, #c7d2fe 0%, #a5b4fc 40%, #f0abfc 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    letter-spacing: -0.01em;
}
.hero-sub { font-size: 0.63rem; color: #475569; margin-top: 2px; letter-spacing: 0.05em; }
.hero-badge {
    background: linear-gradient(135deg, rgba(88,28,135,0.7), rgba(49,10,101,0.7));
    border: 1px solid rgba(167,139,250,0.35);
    color: #c084fc; font-size: 0.63rem; font-weight: 700;
    padding: 5px 12px; border-radius: 20px;
    letter-spacing: 0.03em;
    box-shadow: 0 0 12px rgba(167,139,250,0.15);
}

/* ── Section dividers ── */
.section-title {
    font-size: 0.7rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;
    color: #94a3b8; margin: 0 0 10px; display: flex; align-items: center; gap: 7px;
}
.section-title::before {
    content: ''; display: inline-block; width: 3px; height: 14px;
    background: linear-gradient(180deg, #6366f1, #a855f7);
    border-radius: 2px;
}

/* ── Key status bar ── */
.key-bar {
    display: flex; align-items: center; gap: 8px;
    padding: 10px 14px;
    background: rgba(15,23,42,0.6);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    margin-bottom: 4px;
}
.dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
.dot-green { background: #10b981; box-shadow: 0 0 8px #10b981; }
.dot-amber {
    background: #f59e0b; box-shadow: 0 0 8px #f59e0b;
    animation: dotBlink 1.8s ease-in-out infinite;
}
@keyframes dotBlink { 0%,100%{ opacity:1; } 50%{ opacity:0.3; } }
.key-bar-text { font-size: 0.74rem; color: #cbd5e1; flex: 1; }
.key-bar-hint { font-size: 0.63rem; color: #475569; }

/* ── Info / error / success banners ── */
.banner {
    border-radius: 14px; padding: 12px 16px;
    font-size: 0.76rem; line-height: 1.6;
    margin-bottom: 12px;
    animation: fadeIn 0.3s ease;
}
.banner-info    { background: rgba(30,27,75,0.55);  border: 1px solid rgba(99,102,241,0.3);  color: #a5b4fc; }
.banner-error   { background: rgba(127,29,29,0.45); border: 1px solid rgba(239,68,68,0.35);  color: #fca5a5; }
.banner-success { background: rgba(6,78,59,0.45);   border: 1px solid rgba(52,211,153,0.35); color: #6ee7b7; }
.banner-warn    { background: rgba(120,53,15,0.45); border: 1px solid rgba(245,158,11,0.35); color: #fcd34d; }
@keyframes fadeIn { from{opacity:0;transform:translateY(-4px);} to{opacity:1;transform:none;} }

/* ── Textarea / Inputs ── */
.stTextArea > div > div > textarea {
    background: rgba(2,6,23,0.9) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 16px !important; color: #e2e8f0 !important;
    font-size: 0.83rem !important; line-height: 1.65 !important;
    resize: vertical !important; padding: 14px !important;
    font-family: 'Inter', sans-serif !important;
}
.stTextArea > div > div > textarea:focus {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 3px rgba(124,58,237,0.18) !important;
    outline: none !important;
}
.stTextInput > div > div > input {
    background: rgba(2,6,23,0.9) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 12px !important; color: #e2e8f0 !important;
    font-size: 0.83rem !important; padding: 10px 14px !important;
}
.stTextInput > div > div > input:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.18) !important;
}

/* ── Buttons ── */
div.stButton > button {
    border-radius: 12px !important; font-weight: 600 !important;
    font-size: 0.81rem !important; transition: all 0.18s ease !important;
    background: rgba(15,23,42,0.7) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: #cbd5e1 !important;
    padding: 8px 14px !important;
}
div.stButton > button:hover {
    background: rgba(30,41,59,0.9) !important;
    border-color: rgba(99,102,241,0.5) !important;
    color: #e0e7ff !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 16px rgba(99,102,241,0.2) !important;
}

/* Generate CTA button */
div[data-testid="stButton"].generate-cta > div > button,
.generate-cta button {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #be185d 100%) !important;
    color: white !important; border: none !important;
    padding: 15px 0 !important; font-size: 1rem !important;
    font-weight: 800 !important; letter-spacing: 0.03em !important;
    border-radius: 18px !important;
    box-shadow: 0 4px 28px rgba(99,102,241,0.4), 0 1px 0 rgba(255,255,255,0.1) inset !important;
    width: 100% !important;
}
.generate-cta button:hover {
    box-shadow: 0 8px 40px rgba(124,58,237,0.55) !important;
    transform: translateY(-2px) !important;
}

/* Enhance button */
.enhance-cta button {
    background: linear-gradient(135deg, rgba(79,70,229,0.22), rgba(124,58,237,0.22)) !important;
    color: #a5b4fc !important;
    border: 1px solid rgba(99,102,241,0.35) !important;
    width: 100% !important; padding: 10px 0 !important;
}
.enhance-cta button:hover {
    background: linear-gradient(135deg, rgba(79,70,229,0.35), rgba(124,58,237,0.35)) !important;
    border-color: rgba(99,102,241,0.6) !important;
}

/* Download button */
.stDownloadButton > button {
    background: linear-gradient(135deg, #4f46e5, #6d28d9) !important;
    color: white !important; border: none !important;
    border-radius: 12px !important; font-weight: 700 !important;
    padding: 10px 0 !important; width: 100% !important;
    box-shadow: 0 3px 14px rgba(79,70,229,0.35) !important;
}
.stDownloadButton > button:hover {
    box-shadow: 0 6px 22px rgba(99,102,241,0.5) !important;
    transform: translateY(-1px) !important;
}

/* ── Radio pills ── */
.stRadio > div {
    flex-direction: row !important; flex-wrap: wrap !important; gap: 8px !important;
}
.stRadio > div > label {
    background: rgba(15,23,42,0.85) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 50px !important; padding: 5px 16px !important;
    font-size: 0.72rem !important; cursor: pointer !important;
    color: #94a3b8 !important; transition: all 0.15s !important;
    white-space: nowrap !important;
}
.stRadio > div > label:hover {
    border-color: rgba(99,102,241,0.55) !important; color: #e0e7ff !important;
}
/* selected radio label */
.stRadio > div > label[data-baseweb="radio"]:has(input:checked),
.stRadio > div > label:has(> div[data-checked="true"]) {
    background: rgba(79,70,229,0.25) !important;
    border-color: rgba(99,102,241,0.7) !important;
    color: #c7d2fe !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: rgba(15,23,42,0.6) !important;
    border-radius: 12px !important; font-size: 0.78rem !important;
    color: #94a3b8 !important;
}
.streamlit-expanderContent {
    background: rgba(2,6,23,0.6) !important;
    border-radius: 0 0 12px 12px !important;
    border-top: 1px solid rgba(255,255,255,0.05) !important;
}

/* ── Spinner ── */
.stSpinner > div { color: #a5b4fc !important; }

/* ── Progress ── */
.stProgress > div > div {
    background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899) !important;
    border-radius: 4px !important;
}

/* ── Image frame ── */
.generated-img {
    border-radius: 20px; overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 12px 50px rgba(0,0,0,0.7), 0 0 0 1px rgba(99,102,241,0.1);
    margin-bottom: 14px;
}

/* ── History grid ── */
.hist-thumb {
    border-radius: 14px; overflow: hidden;
    border: 1px solid rgba(255,255,255,0.07);
    margin-bottom: 6px;
    transition: border-color 0.2s, box-shadow 0.2s;
}
.hist-thumb:hover {
    border-color: rgba(99,102,241,0.5);
    box-shadow: 0 4px 20px rgba(99,102,241,0.15);
}
.hist-meta-row {
    font-size: 0.62rem; color: #475569;
    display: flex; justify-content: space-between;
    padding: 2px 2px 6px;
}
.hist-prompt-text {
    font-size: 0.67rem; color: #64748b; line-height: 1.5;
    margin-bottom: 4px; padding: 0 2px;
    display: -webkit-box; -webkit-line-clamp: 2;
    -webkit-box-orient: vertical; overflow: hidden;
}

/* ── Empty state ── */
.empty-state {
    text-align: center; padding: 44px 20px;
    background: rgba(15,23,42,0.25);
    border: 1px dashed rgba(255,255,255,0.07);
    border-radius: 20px; color: #334155;
}
.empty-state .emoji { font-size: 2.4rem; margin-bottom: 10px; }
.empty-state p { font-size: 0.76rem; color: #475569; margin: 0; }

/* ── HR ── */
hr { border-color: rgba(255,255,255,0.05) !important; margin: 20px 0 !important; }

/* ── Code block ── */
.stCodeBlock { border-radius: 12px !important; font-size: 0.75rem !important; }

/* ── Char counter ── */
.char-count {
    text-align: right; font-size: 0.66rem; color: #334155;
    margin-top: -6px; margin-bottom: 10px; font-variant-numeric: tabular-nums;
}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════
STYLE_PRESETS = {
    "🎨 No Style":        "",
    "🌌 Sci-Fi Cosmos":   ", cinematic lighting, cosmos physics, cybernetic elements, hyperdetailed digital art, 8k resolution, neon glow, nebula background",
    "🏙️ Cyberpunk":       ", cyberpunk aesthetic, neon holograms, rainy night city reflections, dense futuristic skyscrapers, moody cinematic lighting, ultra-detailed",
    "🐉 Epic Fantasy":    ", high fantasy, mystical aura, rich glowing colors, intricate details, atmospheric light, octane render, masterpiece quality",
    "📸 Photorealistic":  ", photorealistic, 8k resolution, cinematic atmosphere, shot on 35mm lens, depth of field, ray-traced shadows, physically based rendering",
    "🌸 Anime Art":       ", modern anime illustration, vibrant colors, beautiful key art, Kyoto Animation style, highly detailed scenery, dramatic sky, studio quality",
}

ASPECT_LABELS = ["1:1 Square", "16:9 Widescreen", "9:16 Portrait"]

INSPIRATIONS = [
    "An astronaut exploring ancient ruins on a floating island inside a pastel nebula.",
    "A majestic neon jellyfish floating above a futuristic Tokyo cyber-canal at midnight.",
    "A glass castle emerging from volcanic black sand, glowing with blue internal flames.",
    "Cute mechanical pet fox sitting on a workbench surrounded by glowing holographic gears.",
    "Sunbeams piercing through a dense giant mushroom forest, cinematic perspective, magical dust.",
    "A lone samurai meditating on a mountaintop at dawn, cherry blossoms drifting in slow motion.",
    "An underwater library where koi fish swim between ancient glowing books, bioluminescent light.",
    "A steampunk airship city floating on golden clouds, brass gears, Victorian aesthetic, dusk light.",
    "A crystal dragon coiled around a lighthouse on a stormy sea, lightning in the dark sky.",
    "Moonlit alpine lake perfectly reflecting a Milky Way arch, long-exposure photograph.",
]

# Gemini 3.1 Flash Image — 免費配額可用
GEMINI_IMG_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image:generateContent"
# Gemini 3.5 Flash — 用於 AI Enhance Prompt
GEMINI_URL  = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"


# ═══════════════════════════════════════════════════════════
# SESSION STATE
# ═══════════════════════════════════════════════════════════
def _init():
    defs = {
        "api_key":        "",
        "key_from_secret": False,   # True if auto-loaded from st.secrets
        "prompt":         "",
        "style":          "🎨 No Style",
        "aspect":         "1:1 Square",
        "history":        [],       # list[dict]
        "result_b64":     None,
        "result_prompt":  "",
        "error_msg":      "",
        "success_msg":    "",
        "show_key_panel": False,
        "generating":     False,
        "diag_results":   None,
        "image_model":    "🖼️ Pollinations AI (Flux - Free)",
    }
    for k, v in defs.items():
        if k not in st.session_state:
            st.session_state[k] = v

    # Auto-load from Streamlit secrets (Streamlit Cloud deployment)
    if not st.session_state.api_key and not st.session_state.key_from_secret:
        try:
            secret = st.secrets.get("GOOGLE_API_KEY", "")
            if secret:
                st.session_state.api_key = secret
                st.session_state.key_from_secret = True
        except Exception:
            pass

_init()


# ═══════════════════════════════════════════════════════════
# API HELPERS
# ═══════════════════════════════════════════════════════════
def _post(url: str, payload: dict, retries: int = 3) -> dict:
    """POST with exponential-backoff retry (skips retry on quota/auth errors)."""
    delay = 1.2
    for attempt in range(retries + 1):
        try:
            r = requests.post(url, json=payload, timeout=120)

            if r.status_code == 429:
                # 配額超限 — 不重試（重試沒有意義）
                try:
                    msg = r.json().get("error", {}).get("message", "Quota exceeded")
                except Exception:
                    msg = "Quota exceeded"
                raise RuntimeError(f"QUOTA_EXCEEDED: {msg}")

            if r.status_code in (401, 403):
                # 金鑰無效 — 不重試
                try:
                    msg = r.json().get("error", {}).get("message", "Invalid API key")
                except Exception:
                    msg = "Invalid API key"
                raise RuntimeError(f"AUTH_ERROR: {msg}")

            r.raise_for_status()
            return r.json()

        except RuntimeError:
            raise  # 直接往上拋，不重試
        except requests.exceptions.Timeout:
            if attempt < retries:
                time.sleep(delay); delay *= 2; continue
            raise RuntimeError("Request timed out after 120 s. Try again.")
        except requests.exceptions.ConnectionError:
            if attempt < retries:
                time.sleep(delay); delay *= 2; continue
            raise RuntimeError("Network connection failed. Check your internet.")
        except requests.exceptions.HTTPError as e:
            try:
                msg = r.json().get("error", {}).get("message", str(e))
            except Exception:
                msg = str(e)
            raise RuntimeError(f"API error ({r.status_code}): {msg}")
    raise RuntimeError("Max retries exceeded.")


def call_imagen(prompt: str, api_key: str) -> str:
    """Return base64-encoded PNG from Imagen 4 (requires billing)."""
    try:
        data = _post(f"{IMAGEN_URL}?key={api_key}", {
            "instances":  {"prompt": prompt},
            "parameters": {"sampleCount": 1},
        })
    except RuntimeError as e:
        msg = str(e)
        if "QUOTA_EXCEEDED" in msg:
            raise RuntimeError(
                "QUOTA_EXCEEDED: Imagen 4 需要啟用 Google Cloud 帳單才能使用。\n"
                "請前往 console.cloud.google.com 啟用帳單，或改用下方的免費生圖模式。"
            )
        raise
    b64 = data.get("predictions", [{}])[0].get("bytesBase64Encoded", "")
    if not b64:
        raise RuntimeError(
            "Imagen 4 returned no image. "
            "This may be due to a policy-blocked prompt or missing billing."
        )
    return b64


def call_gemini_image(prompt: str, aspect: str, api_key: str) -> str:
    """Return base64-encoded PNG via Gemini 3.1 Flash Image generation (free tier)."""
    aspect_map = {
        "1:1 Square": "1:1",
        "16:9 Widescreen": "16:9",
        "9:16 Portrait": "9:16"
    }
    api_aspect = aspect_map.get(aspect, "1:1")
    data = _post(f"{GEMINI_IMG_URL}?key={api_key}", {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE", "TEXT"],
            "imageConfig": {
                "aspectRatio": api_aspect
            }
        },
    })
    # Find the inline image part
    parts = (
        data.get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [])
    )
    for part in parts:
        if "inlineData" in part:
            return part["inlineData"]["data"]   # base64 string
    raise RuntimeError(
        "Gemini image generation returned no image. "
        "Try a different prompt or check your API quota."
    )


def call_enhance(prompt: str, api_key: str) -> str:
    """Expand / translate prompt with Gemini 3.5 Flash."""
    system = (
        "You are an elite Prompt Engineer for state-of-the-art image generation models. "
        "Rewrite the user's idea (Chinese or English) into a rich, masterpiece-grade English "
        "prompt. Include: vivid lighting description, texture details, camera perspective, "
        "color palette, and mood. Be concise yet evocative (under 220 words). "
        "Output ONLY the final prompt — no introductions, markdown, or quotes."
    )
    try:
        data = _post(f"{GEMINI_URL}?key={api_key}", {
            "contents": [{"parts": [{"text": f'Enhance this image prompt: "{prompt}"'}]}],
            "systemInstruction": {"parts": [{"text": system}]},
            "generationConfig": {"temperature": 0.85, "maxOutputTokens": 350},
        })
    except RuntimeError as e:
        msg = str(e)
        if "QUOTA_EXCEEDED" in msg:
            raise RuntimeError(
                "QUOTA_EXCEEDED: Gemini 免費配額已用盡。\n"
                "請至 aistudio.google.com/apikey 建立新的 API Key，"
                "或直接輸入英文 Prompt 後點擊生圖（跳過 AI Enhance）。"
            )
        if "AUTH_ERROR" in msg:
            raise RuntimeError("AUTH_ERROR: API Key 無效或已失效，請重新確認並更新 Key。")
        raise
    text = (
        data.get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "")
            .strip()
    )
    if not text:
        raise RuntimeError("Gemini returned an empty response. Try again.")
    return text


def b64_to_pil(b64: str) -> Image.Image:
    return Image.open(BytesIO(base64.b64decode(b64)))

def b64_to_bytes(b64: str) -> bytes:
    return base64.b64decode(b64)


def call_list_models(api_key: str) -> dict:
    """Query Google AI Studio ListModels endpoint using the user's API Key."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        try:
            err_json = r.json()
            msg = err_json.get("error", {}).get("message", str(e))
        except Exception:
            msg = str(e)
        raise RuntimeError(msg)


def call_pollinations_image(prompt: str, aspect: str) -> str:
    """Return base64-encoded PNG via Pollinations.ai (free, keyless Flux model)."""
    w, h = 1024, 1024
    if aspect == "16:9 Widescreen":
        w, h = 1024, 576
    elif aspect == "9:16 Portrait":
        w, h = 576, 1024
        
    encoded_prompt = requests.utils.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={w}&height={h}&nologo=true&private=true&model=flux"
    try:
        r = requests.get(url, timeout=90)
        r.raise_for_status()
        b64 = base64.b64encode(r.content).decode("utf-8")
        if not b64:
            raise RuntimeError("Received empty response from Pollinations.")
        return b64
    except Exception as e:
        raise RuntimeError(f"Pollinations generation failed: {e}")


# ═══════════════════════════════════════════════════════════
# ── HERO HEADER ────────────────────────────────────────────
# ═══════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-wrap">
  <div class="hero-logo">🪐</div>
  <div class="hero-text">
    <div class="hero-title">Gemini Studio</div>
    <div class="hero-sub">TEXT · TO · IMAGE &nbsp;·&nbsp; POWERED BY GOOGLE AI</div>
  </div>
  <div class="hero-badge">⚡ Gemini 3.1 & 3.5</div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# ── API KEY PANEL ──────────────────────────────────────────
# ═══════════════════════════════════════════════════════════
has_key     = bool(st.session_state.api_key.strip())
dot_cls     = "dot-green" if has_key else "dot-amber"
status_text = "Gemini API key ready ✓" if has_key else "API key required"
hint_text   = (
    "Loaded from Streamlit Secrets" if st.session_state.key_from_secret
    else ("Key saved for this session" if has_key else "Enter your key below to generate images")
)

# Status bar row
col_s, col_t = st.columns([4, 1])
with col_s:
    st.markdown(f"""
    <div class="key-bar">
      <div class="dot {dot_cls}"></div>
      <span class="key-bar-text">{status_text}</span>
      <span class="key-bar-hint">{hint_text}</span>
    </div>""", unsafe_allow_html=True)
with col_t:
    lbl = "▲ Close" if st.session_state.show_key_panel else "🔑 Set Key"
    if st.button(lbl, key="btn_key_toggle", use_container_width=True):
        st.session_state.show_key_panel = not st.session_state.show_key_panel
        st.rerun()

# Expanded key entry
if st.session_state.show_key_panel or not has_key:
    st.markdown("""
    <div class="banner banner-info" style="margin-top:8px;">
      🔒 Your API key is <b>only held in this browser session</b> — never stored server-side.<br>
      Get a <b>free</b> key at
      <a href="https://aistudio.google.com/" target="_blank"
         style="color:#818cf8;font-weight:700;">aistudio.google.com</a>
      → "Get API key".<br>
      On Streamlit Cloud, add <code>GOOGLE_API_KEY = "AIza..."</code> under
      <b>App Settings → Secrets</b> for auto-load.
    </div>""", unsafe_allow_html=True)

    entered_key = st.text_input(
        "Google AI Studio API Key",
        value="" if st.session_state.key_from_secret else st.session_state.api_key,
        type="password",
        placeholder="Paste your AIza… API key here",
        key="key_text_input",
        label_visibility="collapsed",
    )
    ka, kb = st.columns(2)
    with ka:
        if st.button("💾 Save Key", key="btn_save_key", use_container_width=True):
            k = entered_key.strip()
            if k:
                st.session_state.api_key = k
                st.session_state.key_from_secret = False
                st.session_state.show_key_panel = False
                st.session_state.diag_results = None
                st.session_state.success_msg = "✅ API key saved for this session."
            else:
                st.session_state.error_msg = "Please paste a valid API key first."
            st.rerun()
    with kb:
        if st.button("🗑 Clear Key", key="btn_clear_key", use_container_width=True):
            st.session_state.api_key = ""
            st.session_state.key_from_secret = False
            st.session_state.diag_results = None
            st.rerun()

    # Billing warning & diagnostics panel
    if has_key:
        st.markdown("""
        <div class="banner banner-warn" style="margin-top:12px;">
          ⚠️ <b>生圖限額提醒 (Billing & Quota Check)</b>：<br>
          Google Gemini 3.1 Flash Image 生圖模型<b>不提供預設的免費額度</b>。如果您的 API 專案未連結 Google Cloud 帳單與信用卡，呼叫生圖時會遇到 <code>limit: 0</code> (Quota Exceeded) 錯誤。<br>
          請至 <a href="https://console.cloud.google.com/billing" target="_blank" style="color:#f59e0b;font-weight:700;">Google Cloud Console Billing</a> 連結您的專案，或建立新 Key 以嘗試。
        </div>""", unsafe_allow_html=True)

        if st.button("🔍 Run API Diagnostics (測試金鑰與授權模型)", key="btn_diagnostics", use_container_width=True):
            with st.spinner("Testing connection to Google AI..."):
                try:
                    res = call_list_models(st.session_state.api_key)
                    models = res.get("models", [])
                    if models:
                        model_names = [m.get("name", "") for m in models]
                        model_displays = [m.get("displayName", "") for m in models]
                        
                        has_img_model = any("gemini-3.1-flash-image" in name for name in model_names)
                        has_txt_model = any("gemini-3.5-flash" in name for name in model_names)
                        
                        st.session_state.diag_results = {
                            "success": True,
                            "model_names": model_names,
                            "model_displays": model_displays,
                            "has_img_model": has_img_model,
                            "has_txt_model": has_txt_model
                        }
                        st.session_state.success_msg = "✅ API Key 連線測試成功！"
                    else:
                        st.session_state.diag_results = {
                            "success": False,
                            "error": "API 連線成功，但未傳回任何模型列表。"
                        }
                except Exception as ex:
                    st.session_state.diag_results = {
                        "success": False,
                        "error": str(ex)
                    }
            st.rerun()

    # Display diagnostics results if available
    if st.session_state.get("diag_results"):
        diag = st.session_state.diag_results
        st.markdown("<br>", unsafe_allow_html=True)
        if diag["success"]:
            st.markdown("##### 📋 API 金鑰授權模型狀態")
            st.markdown(f"""
            | 功能 | 模型名稱 (Model ID) | 狀態 |
            |---|---|---|
            | 🖼️  **生圖模型** | `models/gemini-3.1-flash-image` | {'✅ 已授權可用' if diag["has_img_model"] else '❌ 未授權 (帳單限制)'} |
            | 🔮  **Prompt優化** | `models/gemini-3.5-flash` | {'✅ 已授權可用' if diag["has_txt_model"] else '❌ 未授權'} |
            """)
            
            if not diag["has_img_model"]:
                st.markdown("""
                > ⚠️  **診斷分析**：您的 API 金鑰**尚未取得** `gemini-3.1-flash-image` 權限。  
                > 請至 [console.cloud.google.com/billing](https://console.cloud.google.com/billing) 確認您的 Google Cloud 專案已綁定信用卡與帳單帳戶，或是前往 AI Studio 重新建立一個新專案的 API Key。
                """)
            else:
                st.markdown("""
                > 👍  **診斷分析**：金鑰已具有 `gemini-3.1-flash-image` 的呼叫權限！  
                > 如果生圖仍失敗，請確認該 Google Cloud 專案是否連結到啟用的帳單帳戶（即使是免費額度，部分模型亦需要 billing link 作為身份驗證）。
                """)
            
            with st.expander("📂 展開查看所有可用的 {:,} 個模型".format(len(diag["model_names"]))):
                for name, disp in zip(diag["model_names"], diag["model_displays"]):
                    st.write(f"- **{disp}** (`{name}`)")
        else:
            st.error(f"❌ 診斷連線失敗：{diag['error']}")

st.markdown("<hr>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════
# ── ENGINE / MODEL SELECTION ───────────────────────────────
# ═══════════════════════════════════════════════════════════
st.markdown('<div class="section-title">⚙️ &nbsp;Image Generation Engine</div>', unsafe_allow_html=True)
model_pick = st.radio(
    "image_model",
    options=[
        "🖼️ Pollinations AI (Flux - 100% Free & Keyless)",
        "🪐 Gemini 3.1 Flash Image (Paid Tier / Billing Required)"
    ],
    index=0 if st.session_state.image_model == "🖼️ Pollinations AI (Flux - Free)" else 1,
    horizontal=True,
    key="radio_model",
    label_visibility="collapsed"
)
st.session_state.image_model = "🖼️ Pollinations AI (Flux - Free)" if "Pollinations" in model_pick else "🪐 Gemini 3.1 Flash Image (Paid)"
st.markdown("<br>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# ── PROMPT PANEL ───────────────────────────────────────────
# ═══════════════════════════════════════════════════════════
st.markdown('<div class="section-title">✏️ &nbsp;Creative Prompt</div>', unsafe_allow_html=True)

c_label, c_inspire = st.columns([4, 1])
with c_inspire:
    if st.button("💡 Inspire", key="btn_inspire", use_container_width=True):
        st.session_state.prompt = random.choice(INSPIRATIONS)
        st.session_state.error_msg = ""
        st.rerun()

prompt_val = st.text_area(
    "prompt",
    value=st.session_state.prompt,
    placeholder=(
        "Describe your vision in English or Chinese…\n"
        "e.g. 「一隻機械狐狸在霓虹城市中奔跑」or 'A crystal dragon above a stormy sea'\n\n"
        "💡 Tip: Use '🔮 AI Enhance' to auto-translate & expand your idea!"
    ),
    height=140,
    key="prompt_textarea",
    label_visibility="collapsed",
)
st.session_state.prompt = prompt_val

# Char counter with colour hint
clen = len(prompt_val)
c_color = "#475569" if clen < 200 else ("#f59e0b" if clen < 400 else "#ef4444")
st.markdown(
    f'<div class="char-count" style="color:{c_color};">{clen} / 500 chars</div>',
    unsafe_allow_html=True,
)

# ── AI Enhance button ──
st.markdown('<div class="enhance-cta">', unsafe_allow_html=True)
if st.button(
    "🔮  AI Enhance Prompt  —  translate Chinese & expand details via Gemini",
    key="btn_enhance",
    use_container_width=True,
):
    if not st.session_state.prompt.strip():
        st.session_state.error_msg = "Please enter some text or an idea before enhancing."
        st.rerun()
    elif not st.session_state.api_key.strip():
        st.session_state.error_msg = "API key is missing. Expand the key panel above."
        st.rerun()
    else:
        with st.spinner("🔮 Gemini is crafting your perfect prompt…"):
            try:
                enhanced = call_enhance(st.session_state.prompt, st.session_state.api_key)
                st.session_state.prompt   = enhanced
                st.session_state.error_msg = ""
                st.session_state.success_msg = "✨ Prompt enhanced by Gemini AI!"
            except Exception as ex:
                st.session_state.error_msg = f"Enhancement failed: {ex}"
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# ── STYLE & ASPECT RATIO ───────────────────────────────────
# ═══════════════════════════════════════════════════════════
st.markdown('<div class="section-title">🎨 &nbsp;Art Style</div>', unsafe_allow_html=True)
style_pick = st.radio(
    "style", options=list(STYLE_PRESETS.keys()),
    index=list(STYLE_PRESETS.keys()).index(st.session_state.style),
    horizontal=True, key="radio_style", label_visibility="collapsed",
)
st.session_state.style = style_pick

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-title">📐 &nbsp;Aspect Ratio</div>', unsafe_allow_html=True)
aspect_pick = st.radio(
    "aspect", options=ASPECT_LABELS,
    index=ASPECT_LABELS.index(st.session_state.aspect),
    horizontal=True, key="radio_aspect", label_visibility="collapsed",
)
st.session_state.aspect = aspect_pick

st.markdown("<hr>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# ── STATUS BANNERS ─────────────────────────────────────────
# ═══════════════════════════════════════════════════════════
if st.session_state.error_msg:
    st.markdown(
        f'<div class="banner banner-error">⚠️ &nbsp;{st.session_state.error_msg}</div>',
        unsafe_allow_html=True,
    )

if st.session_state.success_msg:
    st.markdown(
        f'<div class="banner banner-success">{st.session_state.success_msg}</div>',
        unsafe_allow_html=True,
    )
    st.session_state.success_msg = ""  # auto-clear after render


# ═══════════════════════════════════════════════════════════
# ── GENERATE BUTTON ────────────────────────────────────────
# ═══════════════════════════════════════════════════════════
st.markdown('<div class="generate-cta">', unsafe_allow_html=True)
is_free_model = (st.session_state.image_model == "🖼️ Pollinations AI (Flux - Free)")
btn_label = "🚀  Generate with Flux (Free)" if is_free_model else "🚀  Generate with Gemini 3.1 Flash Image"
gen_clicked = st.button(
    btn_label,
    key="btn_generate",
    use_container_width=True,
)
st.markdown('</div>', unsafe_allow_html=True)

if gen_clicked:
    st.session_state.error_msg = ""
    if not st.session_state.prompt.strip():
        st.session_state.error_msg = "Please enter a prompt first."
        st.rerun()
    elif not is_free_model and not st.session_state.api_key.strip():
        st.session_state.error_msg = "API key is missing. Open the key panel above."
        st.session_state.show_key_panel = True
        st.rerun()
    else:
        suffix       = STYLE_PRESETS[st.session_state.style]
        final_prompt = st.session_state.prompt.strip() + suffix

        spinner_ph = st.empty()
        prog_ph    = st.empty()

        spinner_msg = "🪐 Flux 正在生成圖像…" if is_free_model else "🪐 Gemini 3.1 Flash Image 正在生成圖像…"
        with st.spinner(spinner_msg):
            prog_ph.progress(0, text="Connecting to AI Server…")
            time.sleep(0.4)
            prog_ph.progress(25, text="Sending prompt…")
            try:
                if is_free_model:
                    b64 = call_pollinations_image(final_prompt, st.session_state.aspect)
                else:
                    b64 = call_gemini_image(final_prompt, st.session_state.aspect, st.session_state.api_key)
                prog_ph.progress(85, text="Decoding image…")
                time.sleep(0.2)
                prog_ph.progress(100, text="Done!")
                time.sleep(0.3)

                st.session_state.result_b64    = b64
                st.session_state.result_prompt = final_prompt
                st.session_state.success_msg   = "✅ Image generated successfully!"
                st.session_state.error_msg     = ""

                # Push to history with unique ID
                st.session_state.history.insert(0, {
                    "id":        str(uuid.uuid4()),
                    "prompt":    final_prompt,
                    "image_b64": b64,
                    "timestamp": datetime.now().strftime("%H:%M:%S"),
                    "style":     st.session_state.style,
                    "aspect":    st.session_state.aspect,
                })
                st.session_state.history = st.session_state.history[:20]

            except Exception as ex:
                st.session_state.error_msg  = str(ex)
                st.session_state.result_b64 = None

        prog_ph.empty()
        st.rerun()


# ═══════════════════════════════════════════════════════════
# ── RESULT DISPLAY ─────────────────────────────────────────
# ═══════════════════════════════════════════════════════════
if st.session_state.result_b64:
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">🖼️ &nbsp;Generated Image</div>',
                unsafe_allow_html=True)

    pil_img = b64_to_pil(st.session_state.result_b64)

    # Aspect-ratio constrained display
    st.markdown('<div class="generated-img">', unsafe_allow_html=True)
    st.image(pil_img, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Expandable prompt details
    with st.expander("📝 Prompt used for this image"):
        st.code(st.session_state.result_prompt, language=None)

    # Action buttons
    col_dl, col_regen = st.columns(2)
    with col_dl:
        st.download_button(
            label="⬇️  Download PNG",
            data=b64_to_bytes(st.session_state.result_b64),
            file_name=f"gemini_art_{int(time.time())}.png",
            mime="image/png",
            key="btn_download",
            use_container_width=True,
        )
    with col_regen:
        if st.button("🔁  Generate Another", key="btn_regen", use_container_width=True):
            st.session_state.result_b64 = None
            st.rerun()


# ═══════════════════════════════════════════════════════════
# ── GENERATION HISTORY GALLERY ─────────────────────────────
# ═══════════════════════════════════════════════════════════
st.markdown("<hr>", unsafe_allow_html=True)

hdr_col, clr_col = st.columns([4, 1])
with hdr_col:
    st.markdown(
        f'<div class="section-title">🌌 &nbsp;History '
        f'<span style="font-weight:400;color:#334155;font-size:0.65rem;">({len(st.session_state.history)} / 20)</span>'
        f'</div>',
        unsafe_allow_html=True,
    )
with clr_col:
    if st.session_state.history:
        if st.button("🗑 Clear", key="btn_clear_hist", use_container_width=True):
            st.session_state.history    = []
            st.session_state.result_b64 = None
            st.rerun()

if not st.session_state.history:
    st.markdown("""
    <div class="empty-state">
      <div class="emoji">🌌</div>
      <p>No generations yet.<br>
      <span style="font-size:0.7rem;color:#334155;">
        Create your first AI masterpiece above!</span></p>
    </div>""", unsafe_allow_html=True)
else:
    COLS = 2
    items = st.session_state.history
    for row_i in range(0, len(items), COLS):
        row = items[row_i : row_i + COLS]
        gcols = st.columns(COLS)
        for col_widget, item in zip(gcols, row):
            with col_widget:
                # Thumbnail
                if item.get("image_b64"):
                    st.markdown('<div class="hist-thumb">', unsafe_allow_html=True)
                    st.image(b64_to_pil(item["image_b64"]), use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.markdown(
                        '<div style="aspect-ratio:1;background:#0a0f1e;border-radius:14px;'
                        'display:flex;align-items:center;justify-content:center;'
                        'font-size:2rem;border:1px solid rgba(255,255,255,0.06);">🪐</div>',
                        unsafe_allow_html=True,
                    )

                # Prompt preview
                preview = item["prompt"][:90] + ("…" if len(item["prompt"]) > 90 else "")
                st.markdown(
                    f'<div class="hist-prompt-text">{preview}</div>'
                    f'<div class="hist-meta-row">'
                    f'  <span>{item["timestamp"]}</span>'
                    f'  <span style="color:#334155;">{item.get("aspect","1:1")}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

                # Per-item action buttons
                ba, bb = st.columns(2)
                with ba:
                    # Restore: reload prompt + image into main view
                    if st.button("↩ Load", key=f"restore_{item['id']}", use_container_width=True):
                        st.session_state.prompt        = item["prompt"]
                        st.session_state.result_b64    = item.get("image_b64")
                        st.session_state.result_prompt = item["prompt"]
                        st.session_state.style         = item.get("style", "🎨 No Style")
                        st.session_state.aspect        = item.get("aspect", "1:1 Square")
                        st.rerun()
                with bb:
                    # Download directly from history
                    if item.get("image_b64"):
                        st.download_button(
                            label="⬇️",
                            data=b64_to_bytes(item["image_b64"]),
                            file_name=f"gemini_art_{item['id'][:8]}.png",
                            mime="image/png",
                            key=f"dl_{item['id']}",
                            use_container_width=True,
                        )

        st.markdown("<br>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# ── FOOTER ─────────────────────────────────────────────────
# ═══════════════════════════════════════════════════════════
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div class="banner banner-info">
  <b>💡 How to deploy on Streamlit Cloud</b><br>
  1. Push <code>app.py</code>, <code>requirements.txt</code>, and <code>.streamlit/config.toml</code>
     to a public GitHub repo.<br>
  2. Go to <a href="https://share.streamlit.io" target="_blank"
     style="color:#818cf8;font-weight:600;">share.streamlit.io</a>
     → New app → select your repo.<br>
  3. In <b>App Settings → Secrets</b>, add:<br>
     <code>GOOGLE_API_KEY = "AIza…your_key…"</code><br>
  The app will auto-load your key — no manual entry needed for visitors!
</div>
<div style="text-align:center;margin-top:14px;font-size:0.63rem;color:#1e293b;padding-bottom:20px;">
  Gemini Studio · Built with Streamlit &amp; Gemini 3.1 Flash Image · 2026
</div>
""", unsafe_allow_html=True)
