import streamlit as st
from PIL import Image

# تنظیمات صفحه
st.set_page_config(page_title="AFQ AI", page_icon="👑", layout="centered")

# استایل‌دهی اختصاصی (سبز زمردی، طلایی سلطنتی و فوتر ثابت در پایین)
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
        margin-top: 50px;
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

# بخش آپلود عکس
st.subheader("📸 بخش تحلیل عکس و قیمت‌گذاری")
uploaded_file = st.file_uploader("عکس مورد نظر خود را آپلود کنید...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="عکسی که شما آپلود کردید", use_column_width=True)
    st.success("✅ عکس دریافت شد! در حال بررسی تصویر...")

st.divider()

# راه‌اندازی تاریخچه پیام‌ها
if "messages" not in st.session_state:
    st.session_state.messages = []

# نمایش پیام‌های قبلی چت
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# کادر دریافت پیام
if prompt := st.chat_input("سوال خود را به فارسی یا انگلیسی بنویسید..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    prompt_lower = prompt.lower().strip()
    
    # ۱. تشخیص سوالات درباره سازنده
    if any(word in prompt_lower for word in ["سازنده", "کی", "چه کسی", "ساخته", "درست کرده", "creator", "made you", "who made", "mad you", "how mad you"]):
        response = "مرا احمد فرهاد قیومی پسر عبدالسلام درست کرده است. من هوش مصنوعی اختصاصی او (AFQ) هستم!\n\nI was created by Ahmad Farhad Qayumi, son of Abdulsalam."
    
    # ۲. سوالات قرآنی
    elif "قرآن" in prompt or "quran" in prompt or "سیپاره" in prompt or "جزء" in prompt:
        response = "قرآن کریم کتاب آسمانی مسلمانان و دارای ۳۰ سیپاره (جزء) است. / The Holy Quran has 30 parts (Juz)."
    
    # ۳. سلام و احوالپرسی
    elif any(word in prompt_lower for word in ["hello", "hi", "سلام", "درود"]):
        response = "سلام! من دستیار هوشمند AFQ هستم (ساخته‌شده توسط احمد فرهاد قیومی پسر عبدالسلام). امروز چطور می‌توانم کمکتان کنم?"
    
    # ۴. مدیریت سوالات نامفهوم یا کوتاه
    elif len(prompt_lower) < 3 or prompt_lower in ["?", ".", "a", "s"]:
        response = "⚠️ من متوجه سوالتان نشدم! لطفاً منظورتان را به صورت واضح‌تر بنویسید (مثلاً بپرسید: «تو را کی ساخته؟» یا «قرآن چند سیپاره است؟»)."
    
    # ۵. پاسخ عمومی هوشمند
    else:
        response = f"فرهاد عزیز، عبارت شما («{prompt}») دریافت شد. لطفاً سوال خود را در زمینه‌های علمی، ریاضی، حسابداری یا ترجمه دقیق‌تر مطرح کنید!\n\n(ساخته‌شده توسط احمد فرهاد قیومی پسر عبدالسلام)."
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# بخش پاورقی (فوتر) در انتهای صفحه به دو زبان
st.markdown("""
    <div class="footer-box">
        <b>ساخته شده توسط احمد فرهاد قیومی پسر عبدالسلام</b><br>
        <i>Created by Ahmad Farhad Qayumi, son of Abdulsalam</i>
    </div>
""", unsafe_allow_html=True)
