import streamlit as st
from PIL import Image
import urllib.parse
from gtts import gTTS
import os
import uuid

# --- تنظیمات صفحه و استایل سلطنتی ---
st.set_page_config(
    page_title="AFQ AI - Royal International AI Assistant", 
    page_icon="👑", 
    layout="centered"
)

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
    .chat-box-rtl {
        direction: rtl; text-align: right; font-family: Tahoma, Arial, sans-serif; line-height: 1.8;
    }
    .footer-box {
        text-align: center; margin-top: 40px; padding: 18px; border: 2px solid #d4af37; color: #ffffff;
        font-size: 14px; font-weight: bold; background: linear-gradient(135deg, #111a14, #1a1a1a);
        border-radius: 12px; direction: rtl; box-shadow: 0 5px 20px rgba(212, 175, 55, 0.25);
    }
    </style>
""", unsafe_allow_html=True)

# --- هدر و عناوین سلطنتی ---
st.markdown("""
    <div class="royal-header-box">
        <div class="main-ai">AFQ AI</div>
        <div class="main-title">هوش مصنوعی بین‌المللی AFQ</div>
        <div class="sub-title">
            <b>Royal International AI Superstars; Smart, Global & Creative Design</b><br>
            👑 سیستم هوشمند گفتگو، جستجوی عکس و قابلیت انتخاب خواندن متنی یا شنیدن با اسپیکر صوتی
        </div>
    </div>
""", unsafe_allow_html=True)

st.divider()

# --- مدیریت تاریخچه گفتگو ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("🗑️ پاک کردن تاریخچه گفتگو / Clear Chat History"):
    st.session_state.messages = []
    st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f'<div class="chat-box-rtl">{message["content"]}</div>', unsafe_allow_html=True)
        if "image" in message and message["image"] is not None:
            st.image(message["image"], width=300)
        if "audio_path" in message and message["audio_path"] and os.path.exists(message["audio_path"]):
            st.audio(message["audio_path"], format="audio/mp3")

with st.sidebar:
    st.header("📸 Image & Sound / امکانات")
    uploaded_file = st.file_uploader("عکسی برای تحلیل آپلود کنید...", type=["jpg", "jpeg", "png"])
    st.markdown("---")
    st.markdown("### درباره سیستم")
    st.info("این ربات هوشمند صوتی و متنی توسط احمد فرهاد قیومی پسر عبدالسلام ساخته شده است.")

prompt = st.chat_input("هر سوالی دارید بپرسید، یا بنویسید مثلاً 'سوره فاتحه' یا 'عکس شیر'...")

if prompt or uploaded_file:
    img_to_save = None
    if uploaded_file is not None:
        img_to_save = Image.open(uploaded_file)

    user_text = prompt if prompt else "توضیح این عکس"
    st.session_state.messages.append({"role": "user", "content": user_text, "image": img_to_save, "audio_path": None})
    
    with st.chat_message("user"):
        st.markdown(f'<div class="chat-box-rtl">{user_text}</div>', unsafe_allow_html=True)
        if img_to_save:
            st.image(img_to_save, width=300)

    prompt_lower = user_text.lower().strip()
    
    with st.chat_message("assistant"):
        with st.spinner("در حال پردازش پاسخ..."):
            response = ""
            dynamic_image_url = None

            # ۱. درخواست عکس
            if any(k in prompt_lower for k in ["عکس", "تصویر", "pic", "photo", "عکسا"]):
                search_query = prompt_lower.replace("عکس", "").replace("تصویر", "").replace("را بفرست", "").replace("برام بفرست", "").replace("بفرست", "").strip()
                if not search_query:
                    search_query = "nature"
                response = f"📸 این هم از تصویر درخواستی شما برای: **{user_text}**"
                encoded_query = urllib.parse.quote(search_query)
                dynamic_image_url = f"https://source.unsplash.com/featured/?{encoded_query}"

            # ۲. سوالات درباره سازنده
            elif any(word in prompt_lower for word in ["سازنده", "کی", "چه کسی", "ساخته", "درست کرده", "creator", "made you"]):
                response = "مرا **احمد فرهاد قیومی پسر عبدالسلام** درست کرده است. من هوش مصنوعی بین‌المللی و سلطنتی او (**AFQ AI**) هستم!"
            
            # ۳. سوره فاتحه
            elif "فاتحه" in prompt_lower:
                response = "📖 متن سوره مبارکه فاتحه:\n\nبِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ (۱) الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ (۲) الرَّحْمَٰنِ الرَّحِيمِ (۳) مَالِكِ يَوْمِ الدِّينِ (۴) إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ (۵) اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ (۶) صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ (۷)"

            # ۴. سوره بقره
            elif "بقره" in prompt_lower:
                response = "📖 متن سوره مبارکه بقره (آیات ۱ تا ۵):\n\nبِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\nالم (١)\nذَٰلِكَ الْكِتَابُ لَا رَيْبَ ۛ فِيهِ ۛ هُدًى لِلْمُتَّقِينَ (٢)"
            
            # ۵. پاسخ عمومی هوشمند
            else:
                response = f"💬 پاسخ هوشمند به پرسش شما ('{user_text}'):\n\nمن به عنوان هوش مصنوعی بین‌المللی AFQ آماده‌ی پاسخگویی هستم. شما می‌توانید درخواست عکس، متن‌های مذهبی یا هر سوال دیگری را بپرسید.\n\n(Created by Ahmad Farhad Qayumi, son of Abdulsalam)."
        
        # تولید صدا برای اسپیکر
        audio_file_path = f"audio_{uuid.uuid4().hex[:6]}.mp3"
        try:
            clean_text = response.replace("*", "").replace("📸", "").replace("💬", "").replace("📖", "")
            tts = gTTS(text=clean_text, lang='fa', slow=False)
            tts.save(audio_file_path)
        except Exception:
            audio_file_path = None

        st.markdown(f'<div class="chat-box-rtl">{response}</div>', unsafe_allow_html=True)
        if dynamic_image_url:
            st.image(dynamic_image_url, width=350)
            
        if audio_file_path and os.path.exists(audio_file_path):
            st.write("🔊 **برای شنیدن با صدای بلند، روی دکمه پخش اسپیکر زیر کلیک کنید:**")
            st.audio(audio_file_path, format="audio/mp3")
    
    st.session_state.messages.append({"role": "assistant", "content": response, "image": None, "audio_path": audio_file_path})

st.markdown("""
    <div class="footer-box">
        <b>Created by Ahmad Farhad Qayumi, son of Abdulsalam</b><br>
        <i>ساخته شده توسط احمد فرهاد قیومی پسر عبدالسلام</i>
    </div>
""", unsafe_allow_html=True)
