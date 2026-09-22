import streamlit as st
from PIL import Image

# --- تنظیمات صفحه و استایل سلطنتی ---
st.set_page_config(page_title="AFQ AI - Royal International AI Assistant", page_icon="👑", layout="centered")

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

# --- هدر و عناوین سلطنتی ---
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

# --- مدیریت تاریخچه گفتگو ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# دکمه پاک کردن تاریخچه چت
if st.button("🗑️ Clear Chat History / پاک کردن تاریخچه گفتگو"):
    st.session_state.messages = []
    st.rerun()

# نمایش پیام‌های قبلی چت
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)
        if "image" in message and message["image"] is not None:
            st.image(message["image"], width=300)

# --- بخش آپلود عکس (سایدبار) ---
with st.sidebar:
    st.header("📸 Image Upload / آپلود عکس")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# --- کادر دریافت پیام (متن) در پایین صفحه ---
prompt = st.chat_input("هر سوالی دارید بپرسید، متنی تایپ کنید، یا نام سوره را بنویسید...")

# --- پردازش هوشمند پیام یا عکس کاربر ---
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
            # پاسخ‌های اتوماتیک و هوشمند پیشرفته بدون نیاز به کتابخانه بیرونی
            if any(word in prompt_lower for word in ["سازنده", "کی", "چه کسی", "ساخته", "درست کرده", "creator", "made you"]):
                response = "مرا احمد فرهاد قیومی پسر عبدالسلام درست کرده است. من هوش مصنوعی بین‌المللی و سلطنتی او (AFQ) هستم!\n\n(Created by Ahmad Farhad Qayumi, son of Abdulsalam)."
            
            elif any(word in prompt_lower for word in ["سوره بقره", "بقره", "surah baqarah"]):
                response = """📖 **متن سوره مبارکه بقره (آیات ۱ تا ۵):**<br><br>
                    <div class="quran-text">
                    بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ<br>
                    الم (١)<br>
                    ذَٰلِكَ الْكِتَابُ لَا رَيْبَ ۛ فِيهِ ۛ هُدًى لِلْمُتَّقِينَ (٢)<br>
                    الَّذِينَ يُؤْمِنُونَ بِالْغَيْبِ وَيُقِيمُونَ الصَّلَاةَ وَمِمَّا رَزَقْنَاهُمْ يُنْفِيقُونَ (٣)<br>
                    وَالَّذِينَ يُؤْمِنُونَ بِمَا أُنْزِلَ إِلَيْكَ وَمَا أُنْزِلَ مِنْ قَبْلِكَ وَبِالْآخِرَةِ هُمْ يُوقِنُونَ (٤)<br>
                    أُولَٰئِكَ عَلَىٰٰ هُدًى مِنْ رَبِّهِمْ ۖ وَأُولَٰئِكَ هُمُ الْمُفْلِحُونَ (٥)
                    </div><br>✨ (Created by Ahmad Farhad Qayumi, son of Abdulsalam)."""
            
            elif any(word in prompt_lower for word in ["سوره", "سوره‌ها", "سورها", "surah"]):
                response = "📖 قرآن کریم دارای **۱۱۴ سوره** مبارکه است (۸۶ سوره مکی و ۲۸ سوره مدنی).\n\nThe Holy Quran has **114 Surahs**."
            
            elif any(word in prompt_lower for word in ["سلام", "hello", "hi", "درود"]):
                response = "سلام! من هوش مصنوعی سلطنتی AFQ هستم. امروز چه کمکی از دست من برای شما برمی‌آید؟\n\nHello! I am AFQ AI assistant."
            
            else:
                response = f"🌐 درخواست هوشمند شما دریافت و پردازش شد: «{user_text}»\n\nسیستم اتوماتیک AFQ AI آماده پاسخگویی به تمام ایده‌ها و سوالات شماست.\n\n(Created by Ahmad Farhad Qayumi, son of Abdulsalam)."
        
        st.markdown(response, unsafe_allow_html=True)
    
    st.session_state.messages.append({"role": "assistant", "content": response, "image": None})

# --- بخش پاورقی (فوتر) در انتهای صفحه ---
st.markdown("""
    <div class="footer-box">
        <b>Created by Ahmad Farhad Qayumi, son of Abdulsalam</b><br>
        <i>ساخته شده توسط احمد فرهاد قیومی پسر عبدالسلام</i>
    </div>
""", unsafe_allow_html=True)
