import streamlit as st
from PIL import Image
import google.generativeai as genai

# تنظیمات صفحه
st.set_page_config(page_title="AFQ AI - Royal International AI Assistant", page_icon="👑", layout="centered")

# تنظیم کلید API گوگل جمینای (شما می‌توانید کلید رایگان خود را از گوگل بگیرید و اینجا قرار دهید)
# برای تست یا استفاده عمومی، اگر کلید دارید اینجا وارد کنید یا از st.secrets استفاده کنید
GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY_HERE"  # کلید API خود را اینجا بگذارید

if GOOGLE_API_KEY != "YOUR_GEMINI_API_KEY_HERE":
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    model = None

# استایل‌دهی حرفه‌ای، سه‌بعدی و سلطنتی
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }
    .royal-header-box {
        background: linear-gradient(135deg, rgba(11, 102, 35, 0.25), rgba(212, 175, 55, 0.2));
        border: 2px solid #d4af37;
        border-radius: 20px;
        padding: 25px 15px;
        text-align: center;
        direction: rtl;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(212, 175, 55, 0.2);
        margin-bottom: 25px;
    }
    .main-ai {
        font-size: 54px;
        font-weight: 900;
        background: linear-gradient(to bottom, #ffdf00, #b8860b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        filter: drop-shadow(3px 3px 5px rgba(0,0,0,0.8));
        direction: ltr;
        unicode-bidi: embed;
    }
    .main-title {
        font-size: 32px;
        font-weight: 800;
        background: linear-gradient(to bottom, #00ff66, #0b6623);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 5px;
        filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.8));
    }
    .sub-title {
        color: #f1f1f1 !important;
        font-size: 14px;
        font-weight: 600;
        margin-top: 12px;
        line-height: 1.7;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.9);
    }
    .footer-box {
        text-align: center;
        margin-top: 40px;
        padding: 18px;
        border: 2px solid #d4af37;
        color: #ffffff;
        font-size: 14px;
        font-weight: bold;
        background: linear-gradient(135deg, #111a14, #1a1a1a);
        border-radius: 12px;
        direction: rtl;
        box-shadow: 0 5px 20px rgba(212, 175, 55, 0.25);
    }
    </style>
""", unsafe_allow_html=True)

# هدر و عناوین سلطنتی
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

# دکمه پاک کردن تاریخچه چت
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

# بخش آپلود عکس در سایدبار
with st.sidebar:
    st.header("📸 Image Upload / آپلود عکس")
    st.write("Upload an image for AI analysis / عکسی را آپلود کنید تا هوش مصنوعی تحلیل کند")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# کادر دریافت پیام (متن) در پایین صفحه
prompt = st.chat_input("هر سوالی دارید بپرسید یا متنی تایپ کنید...")

# پردازش پیام یا عکس کاربر به صورت کاملاً اتوماتیک
if prompt or uploaded_file:
    img_to_save = None
    if uploaded_file is not None:
        img_to_save = Image.open(uploaded_file)

    user_text = prompt if prompt else "این تصویر را تحلیل کن."
    
    # ثبت پیام کاربر در حافظه
    st.session_state.messages.append({"role": "user", "content": user_text, "image": img_to_save})
    
    with st.chat_message("user"):
        st.markdown(user_text)
        if img_to_save:
            st.image(img_to_save, width=300)

    # تولید پاسخ اتوماتیک از طریق مدل هوش مصنوعی (Google Gemini)
    with st.chat_message("assistant"):
        with st.spinner("در حال پردازش هوشمند..."):
            try:
                if model is not None:
                    if img_to_save:
                        # ارسال متن و عکس به مدل هوش مصنوعی
                        ai_response = model.generate_content([user_text, img_to_save])
                    else:
                        # ارسال فقط متن به مدل هوش مصنوعی
                        ai_response = model.generate_content(user_text)
                    
                    response = ai_response.text
                else:
                    # حالت پیش‌فرض اگر کلید API تنظیم نشده باشد
                    if "سازنده" in user_text or "creator" in user_text:
                        response = "مرا احمد فرهاد قیومی پسر عبدالسلام ساخته است. (Created by Ahmad Farhad Qayumi, son of Abdulsalam)."
                    else:
                        response = f"پاسخ اتوماتیک سیستم به سوال شما: «{user_text}». (برای دسترسی به موتور کامل هوش مصنوعی، لطفاً API Key خود را در کد وارد کنید).\n\nCreated by Ahmad Farhad Qayumi, son of Abdulsalam."
            except Exception as e:
                response = f"خطا در ارتباط با سرور هوش مصنوعی: {str_err if 'str_err' in locals() else e}"
        
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response, "image": None})

# بخش پاورقی (فوتر)
st.markdown("""
    <div class="footer-box">
        <b>Created by Ahmad Farhad Qayumi, son of Abdulsalam</b><br>
        <i>ساخته شده توسط احمد فرهاد قیومی پسر عبدالسلام</i>
    </div>
""", unsafe_allow_html=True)
