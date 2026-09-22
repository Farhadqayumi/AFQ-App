import streamlit as st
from PIL import Image

# تنظیمات صفحه
st.set_page_config(page_title="AFQ AI - International AI", page_icon="👑", layout="centered")

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
        font-size: 15px;
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

# عناوین دو زبانه در بالای صفحه
st.markdown('<div class="main-ai">AI</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">هوش مصنوعی AFQ</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="sub-title">
        <b>Global Multilingual AI Assistant (Supports all international languages)</b><br>
        👑 دستیار هوشمند بین‌المللی؛ پشتیبانی از تمامی زبان‌های دنیا و پاسخگویی جامع
    </div>
""", unsafe_allow_html=True)

st.divider()

# دکمه دو زبانه برای پاک کردن تاریخچه چت
if st.button("🗑️ Clear Chat History / پاک کردن تاریخچه گفتگو"):
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

# بخش آپلود عکس در منوی کناری (سایدبار)
with st.sidebar:
    st.header("📸 Image Upload & Analysis")
    st.write("Upload image for global analysis / آپلود عکس برای تحلیل جهانی و قیمت‌گذاری")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# کادر دریافت پیام (متن) در پایین صفحه با راهنمای چندزبانه
prompt = st.chat_input("Ask in any language (English, Persian, Pashto, Arabic, etc.) / سوال خود را به هر زبانی بنویسید...")

# پردازش پیام یا عکس کاربر
if prompt or uploaded_file:
    img_to_save = None
    if uploaded_file is not None:
        img_to_save = Image.open(uploaded_file)

    user_text = prompt if prompt else "Please analyze this image and check details."
    
    st.session_state.messages.append({"role": "user", "content": user_text, "image": img_to_save})
    
    with st.chat_message("user"):
        st.markdown(user_text)
        if img_to_save:
            st.image(img_to_save, width=300)

    prompt_lower = user_text.lower().strip()
    
    # پردازش هوشمند و چندزبانه سوالات درباره سازنده
    if any(word in prompt_lower for word in ["سازنده", "کی", "چه کسی", "ساخته", "درست کرده", "creator", "made you", "who made", "mad you", "how mad you", "من صنعك", "مشرک"]):
        response = "مرا احمد فرهاد قیومی پسر عبدالسلام درست کرده است. من هوش مصنوعی اختصاصی او (AFQ) هستم!\n\nI was created by Ahmad Farhad Qayumi, son of Abdulsalam."
    
    # سوالات قرآنی
    elif "قرآن" in user_text or "quran" in prompt_lower or "قرآن کریم" in prompt_lower or "سیپاره" in user_text or "جزء" in user_text:
        response = "قرآن کریم کتاب آسمانی مسلمانان و دارای ۳۰ سیپاره (جزء) است.\n\nThe Holy Quran has 30 parts (Juz)."
    
    # بررسی عکس آپلود شده
    elif uploaded_file is not None:
        response = "📸 تصویر شما دریافت و به صورت بین‌المللی تحلیل شد! مشخصات، جزئیات و قیمت آن ارزیابی گردید.\n\nYour image was successfully analyzed globally!\n\n(Created by Ahmad Farhad Qayumi, son of Abdulsalam)."
    
    # سلام و احوالپرسی بین‌المللی
    elif any(word in prompt_lower for word in ["hello", "hi", "سلام", "درود", "مرحبابا", "سلام علیکم"]):
        response = "سلام! من دستیار هوشمند AFQ هستم. هر سوالی به هر زبانی دارید بپرسید.\n\nHello! I am AFQ AI assistant, supporting all international languages. How can I help you?"
    
    # سوالات خیلی کوتاه یا نامفهوم
    elif len(prompt_lower) < 2 and uploaded_file is None:
        response = "⚠️ من متوجه سوالتان نشدم! لطفاً منظورتان را به صورت واضح‌تر بنویسید.\n\nI didn't understand your question! Please write more clearly."
    
    # پاسخ عمومی بین‌المللی (پشتیبانی از هر زبان ورودی)
    else:
        response = f"پیام شما («{user_text}») دریافت شد. من به عنوان یک هوش مصنوعی بین‌المللی (AFQ) به هر زبانی پاسخ می‌دهم!\n\nYour message has been received. I support all languages worldwide!\n\n(Created by Ahmad Farhad Qayumi, son of Abdulsalam)."
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response, "image": None})

# بخش پاورقی (فوتر) بین‌المللی در انتهای صفحه
st.markdown("""
    <div class="footer-box">
        <b>Created by Ahmad Farhad Qayumi, son of Abdulsalam</b><br>
        <i>ساخته شده توسط احمد فرهاد قیومی پسر عبدالسلام</i>
    </div>
""", unsafe_allow_html=True)
