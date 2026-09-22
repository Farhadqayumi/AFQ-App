import streamlit as st
from PIL import Image
import google.generativeai as genai

# --- تنظیمات صفحه و استایل سلطنتی ---
st.set_page_config(page_title="AFQ AI - Royal International AI Assistant", page_icon="👑", layout="centered")

# تنظیم کلید API گوگل جمینای (کلید خود را اینجا بگذارید)
GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY_HERE"

if GOOGLE_API_KEY != "YOUR_GEMINI_API_KEY_HERE":
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    model = None

st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: #ffffff; }
    .royal-header-box {
        background: linear-gradient(135deg, rgba(11, 102, 35, 0.25), rgba(212, 175, 55, 0.2));
        border: 2px solid #d4af37; border-radius: 20px; padding: 25px 15px; text-align: center; direction: rtl;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(212, 175, 55, 0.2); margin-bottom: 25px;
    }
    .main-ai {
        font-size: 54px; font-weight: 900; background: linear-gradient(to bottom, #ffdf00, #b8860b);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0px;
        filter: drop-shadow(3px 3px 5px rgba(0,0,0,0.8)); direction: ltr; unicode-bidi: embed;
    }
    .main-title {
        font-size: 32px; font-weight: 800; background: linear-gradient(to bottom, #00ff66, #0b6623);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-top: 5px;
        filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.8));
    }
    .sub-title { color: #f1f1f1 !important; font-size: 14px; font-weight: 600; margin-top: 12px; line-height: 1.7; text-shadow: 1px 1px 3px rgba(0,0,0,0.9); }
    .footer-box {
        text-align: center; margin-top: 40px; padding: 18px; border: 2px solid #d4af37; color: #ffffff;
        font-size: 14px; font-weight: bold; background: linear-gradient(135deg, #111a14, #1a1a1a);
        border-radius: 12px; direction: rtl; box-shadow: 0 5px 20px rgba(212, 175, 55, 0.25);
    }
    .quran-text {
        font-family: 'Amiri', serif; font-size: 18px; line-height: 2.0; color: #e0e0e0;
        text-align: right; direction: rtl; padding: 20px; background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px; margin-top: 10px;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown("""
    <div class="royal-header-box">
        <div class="main-ai">AFQ AI</div>
        <div class="main-title">هوش مصنوعی بین‌المللی AFQ</div>
        <div class="sub-title">
            <b>Royal International AI Superstars; Smart, Global & Creative Design</b><br>
            👑 سوپراستار سلطنتی هوش مصنوعی؛ هوشمند، جهانی و طراح خلاق خودکار
        </div>
    </div>
""", unsafe_allow_html=True)

st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("🗑️ Clear Chat History / پاک کردن تاریخچه گفتگو"):
    st.session_state.messages = []
    st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)
        if "image" in message and message["image"] is not None:
            st.image(message["image"], width=300)

with st.sidebar:
    st.header("📸 Image Upload / آپلود عکس")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

prompt = st.chat_input("هر سوالی دارید بپرسید، متنی تایپ کنید، یا نام سوره را بنویسید...")

if prompt or uploaded_file:
    img_to_save = None
    if uploaded_file is not None:
        img_to_save = Image.open(uploaded_file)

    user_text = prompt if prompt else "Please analyze this image."
    st.session_state.messages.append({"role": "user", "content": user_text, "image": img_to_save})
    
    with st.chat_message("user"):
        st.markdown(user_text)
        if img_to_save:
            st.image(img_to_save, width=300)

    prompt_lower = user_text.lower().strip()
    
    with st.chat_message("assistant"):
        with st.spinner("در حال پردازش هوشمند..."):
            try:
                response = ""
                if any(word in prompt_lower for word in ["سازنده", "کی", "چه کسی", "ساخته", "درست کرده", "creator", "made you"]):
                    response = "مرا احمد فرهاد قیومی پسر عبدالسلام درست کرده است. (Created by Ahmad Farhad Qayumi, son of Abdulsalam)."
                elif any(word in prompt_lower for word in ["سوره بقره", "بقره", "surah baqarah"]):
                    response = """📖 **متن سوره مبارکه بقره (آیات ۱ تا ۵):**<br><br>
                        <div class="quran-text">
                        بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ<br>الم (١)<br>ذَٰلِكَ الْكِتَابُ لَا رَيْبَ ۛ فِيهِ ۛ هُدًى لِلْمُتَّقِينَ (٢)
                        </div><br>(Created by Ahmad Farhad Qayumi, son of Abdulsalam)."""
                elif img_to_save and model is not None:
                    ai_response = model.generate_content([user_text, img_to_save])
                    response = ai_response.text
                elif prompt and model is not None:
                    ai_response = model.generate_content(user_text)
                    response = ai_response.text
                else:
                    response = f"🌐 درخواست شما دریافت شد: «{user_text}». (برای فعال شدن هوش کامل، کلید API را وارد کنید).\n\n(Created by Ahmad Farhad Qayumi, son of Abdulsalam)."
            except Exception as e:
                response = f"⚠️ خطا: {e}"
        
        st.markdown(response, unsafe_allow_html=True)
    
    st.session_state.messages.append({"role": "assistant", "content": response, "image": None})

st.markdown("""
    <div class="footer-box">
        <b>Created by Ahmad Farhad Qayumi, son of Abdulsalam</b><br>
        <i>ساخته شده توسط احمد فرهاد قیومی پسر عبدالسلام</i>
    </div>
""", unsafe_allow_html=True)
