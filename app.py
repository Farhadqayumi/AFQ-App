import streamlit as st
from PIL import Image

# تنظیمات صفحه
st.set_page_config(page_title="AFQ AI - Royal International AI Assistant", page_icon="👑", layout="centered")

# استایل‌دهی پیشرفته، تری‌دی، برجسته و سازگار با حالت تاریک و روشن
st.markdown("""
    <style>
    /* پس‌زمینه کلی و تنظیمات متن */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .main-container {
        text-align: center;
        direction: rtl;
        padding: 10px;
    }
    /* عنوان برجسته طلاسی تری‌دی */
    .main-ai {
        font-size: 52px;
        font-weight: 900;
        color: #ffdf00;
        margin-bottom: 0px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.8), 0 0 25px rgba(255,215,0,0.5);
        direction: ltr;
        unicode-bidi: embed;
    }
    /* عنوان فارسی برجسته و واضح */
    .main-title {
        font-size: 30px;
        font-weight: 800;
        color: #00ff66;
        margin-top: 5px;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.8);
    }
    /* زیرعنوان با نور و وضوح بالا برای حالت موبایل */
    .sub-title {
        color: #f0f0f0;
        font-size: 15px;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 25px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.9);
        line-height: 1.6;
    }
    /* کادر پاورقی شیک و برجسته */
    .footer-box {
        text-align: center;
        margin-top: 40px;
        padding: 18px;
        border: 2px solid #ffdf00;
        color: #ffffff;
        font-size: 15px;
        font-weight: bold;
        background: linear-gradient(135deg, #1f1f1f, #2d2d2d);
        border-radius: 12px;
        direction: rtl;
        box-shadow: 0 4px 15px rgba(255,215,0,0.3);
    }
    /* تنظیمات دکمه‌ها و عناصر متن برای خوانایی کامل */
    p, span, label, div {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# عناوین منظم و دو زبانه با استایل برجسته HD
st.markdown("""
    <div class="main-container">
        <div class="main-ai">AFQ AI</div>
        <div class="main-title">هوش مصنوعی بین‌المللی AFQ</div>
        <div class="sub-title">
            <b>Royal International AI Superstars; Smart, Global & Creative Design</b><br>
            👑 سوپراستار سلطنتی هوش مصنوعی؛ هوشمند، جهانی و طراح خلاق خودکار
        </div>
    </div>
""", unsafe_allow_html=True)

st.divider()

# دکمه پاک کردن تاریخچه چت با ظاهر جذاب
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
    st.header("📸 Image Upload / آپلود عکس")
    st.write("Upload an image for AI automatic design / عکسی را آپلود کنید تا هوش مصنوعی آن را دیزاین کند")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# کادر دریافت پیام (متن) در پایین صفحه
prompt = st.chat_input("Ask AI to design or type your question in any language...")

# پردازش پیام یا عکس کاربر
if prompt or uploaded_file:
    img_to_save = None
    if uploaded_file is not None:
        img_to_save = Image.open(uploaded_file)

    user_text = prompt if prompt else "Please AI, design this image creatively for a global audience."
    
    st.session_state.messages.append({"role": "user", "content": user_text, "image": img_to_save})
    
    with st.chat_message("user"):
        st.markdown(user_text)
        if img_to_save:
            st.image(img_to_save, width=300)

    prompt_lower = user_text.lower().strip()
    
    # پردازش هوشمند سوالات درباره سازنده
    if any(word in prompt_lower for word in ["سازنده", "کی", "چه کسی", "ساخته", "درست کرده", "creator", "made you", "who made", "mad you"]):
        response = "مرا احمد فرهاد قیومی پسر عبدالسلام درست کرده است. من هوش مصنوعی بین‌المللی و سلطنتی او (AFQ) هستم که برای استفاده تمام مردم جهان طراحی شده‌ام!\n\nI was created by Ahmad Farhad Qayumi, son of Abdulsalam. I am his royal international AI assistant!"
    
    elif "قرآن" in user_text or "quran" in prompt_lower or "سیپاره" in user_text or "جزء" in user_text:
        response = "قرآن کریم کتاب آسمانی مسلمانان و دارای ۳۰ سیپاره (جزء) است.\n\nThe Holy Quran has 30 parts (Juz)."
    
    elif uploaded_file is not None:
        response = f"🎨 **هوش مصنوعی AFQ در حال دیزاین و پردازش تصویر شماست...**\n\nمن این اثر را با استانداردهای جهانی و خلاقیت تمام‌خودکار بازطراحی کردم تا برای هر کاربری در سراسر دنیا جذاب باشد.\n\n✨ *AI Automatic Design Completed Successfully.*\n\n(Created by Ahmad Farhad Qayumi, son of Abdulsalam)."
    
    elif any(word in prompt_lower for word in ["hello", "hi", "سلام", "درود"]):
        response = "سلام! من هوش مصنوعی بین‌المللی AFQ هستم. از هر کجای جهان که هستید، آماده‌ام تا ایده‌ها و دیزاین‌های شما را خلق کنم!\n\nHello! I am AFQ AI. Ready to design and assist users worldwide!"
    
    else:
        response = f"🌐 درخواست شما دریافت شد. من به عنوان یک هوش مصنوعی بین‌المللی، آماده‌ی خلق دیزاین‌ها و پاسخ به تمام سوالات شما از سراسر جهان هستم!\n\nYour global request has been processed successfully by AFQ AI.\n\n(Created by Ahmad Farhad Qayumi, son of Abdulsalam)."
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response, "image": None})

# بخش پاورقی (فوتر) در انتهای صفحه
st.markdown("""
    <div class="footer-box">
        <b>Created by Ahmad Farhad Qayumi, son of Abdulsalam</b><br>
        <i>ساخته شده توسط احمد فرهاد قیومی پسر عبدالسلام</i>
    </div>
""", unsafe_allow_html=True)
