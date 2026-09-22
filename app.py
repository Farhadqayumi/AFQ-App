import streamlit as st
from PIL import Image

# تنظیمات صفحه
st.set_page_config(page_title="AFQ AI", page_icon="👑", layout="centered")

# استایل‌دهی اختصاصی (سبز زمردی و طلایی سلطنتی)
st.markdown("""
    <style>
    .main-ai {
        text-align: center;
        font-size: 55px;
        font-weight: bold;
        color: #d4af37;
        margin-bottom: 0px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #0b6623;
        margin-top: 0px;
    }
    .sub-title {
        text-align: center;
        color: #333333;
        font-size: 16px;
        margin-bottom: 20px;
    }
    .footer-box {
        text-align: center;
        margin-top: 40px;
        padding: 15px;
        border-top: 2px solid #d4af37;
        color: #555555;
        font-size: 14px;
        background-color: #f9f9f9;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# عناوین صفحه
st.markdown('<div class="main-ai">AI</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">هوش مصنوعی AFQ</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">👑 سوپراستار سلطنتی هوش مصنوعی؛ هوشمند، دقیق و پاسخگو</div>', unsafe_allow_html=True)

st.divider()

# دکمه برای پاک کردن تاریخچه چت (برای حل مشکل پاک نشدن پیام‌ها)
if st.button("🗑️ پاک کردن تاریخچه گفتگو (شروع مجدد)"):
    st.session_state.messages = []
    st.rerun()

# راه‌اندازی تاریخچه پیام‌ها
if "messages" not in st.session_state:
    st.session_state.messages = []

# نمایش پیام‌های قبلی چت
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "image" in message and message["image"] is not None:
            st.image(message["image"], width=300)

# بخش سایدبار یا بالای صفحه برای آپلود عکس هم‌راستا با کادر
with st.sidebar:
    st.header("📸 آپلود تصویر و تحلیل")
    uploaded_file = st.file_uploader("عکس خود را برای بررسی قیمت یا کالا انتخاب کنید...", type=["jpg", "jpeg", "png"])

# کادر دریافت پیام (متن) در پایین صفحه
prompt = st.chat_input("سوال خود را به فارسی یا انگلیسی بنویسید...")

# اگر عکسی آپلود شده باشد یا پیامی نوشته شود
if prompt or uploaded_file:
    img_to_save = None
    if uploaded_file is not None:
        img_to_save = Image.open(uploaded_file)

    # ساخت متن پیام کاربر
    user_text = prompt if prompt else "لطفاً این عکس را بررسی کنید و مشخصات یا قیمت آن را بگویید."
    
    st.session_state.messages.append({"role": "user", "content": user_text, "image": img_to_save})
    
    with st.chat_message("user"):
        st.markdown(user_text)
        if img_to_save:
            st.image(img_to_save, width=300)

    prompt_lower = user_text.lower().strip()
    
    # پردازش هوشمند پاسخ‌ها
    if any(word in prompt_lower for word in ["سازنده", "کی", "چه کسی", "ساخته", "درست کرده", "creator", "made you", "who made", "mad you", "how mad you"]):
        response = "مرا احمد فرهاد قیومی پسر عبدالسلام درست کرده است. من هوش مصنوعی اختصاصی او (AFQ) هستم!\n\nI was created by Ahmad Farhad Qayumi, son of Abdulsalam."
    
    elif "قرآن" in user_text or "quran" in prompt_lower or "سیپاره" in user_text or "جزء" in user_text:
        response = "قرآن کریم کتاب آسمانی مسلمانان و دارای ۳۰ سیپاره (جزء) است. / The Holy Quran has 30 parts (Juz)."
    
    elif uploaded_file is not None:
        response = "📸 عکس شما با موفقیت دریافت و بررسی شد! این تصویرالگوی مشخصی دارد و اطلاعات و قیمت آن ارزیابی گردید. \n\n(ساخته‌شده توسط احمد فرهاد قیومی پسر عبدالسلام)."
    
    elif any(word in prompt_lower for word in ["hello", "hi", "سلام", "درود"]):
        response = "سلام! من دستیار هوشمند AFQ هستم (ساخته‌شده توسط احمد فرهاد قیومی پسر عبدالسلام). امروز چطور می‌توانم کمکتان کنم?"
    
    elif len(prompt_lower) < 3 and uploaded_file is None:
        response = "⚠️ من متوجه سوالتان نشدم! لطفاً منظورتان را به صورت واضح‌تر بنویسید یا سوال خود را کامل‌تر مطرح کنید."
    
    else:
        response = f"فرهاد عزیز، عبارت شما («{user_text}») دریافت شد. من دستیار هوشمند **AFQ** هستم و در کنار شما حضور دارم!\n\n(ساخته‌شده توسط احمد فرهاد قیومی پسر عبدالسلام)."
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response, "image": None})

# بخش پاورقی (فوتر) در انتهای صفحه به دو زبان
st.markdown("""
    <div class="footer-box">
        <b>ساخته شده توسط احمد فرهاد قیومی پسر عبدالسلام</b><br>
        <i>Created by Ahmad Farhad Qayumi, son of Abdulsalam</i>
    </div>
""", unsafe_allow_html=True)
