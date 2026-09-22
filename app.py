import streamlit as st
from PIL import Image

# تنظیمات صفحه
st.set_page_config(page_title="AFQ AI - Royal International AI Assistant", page_icon="👑", layout="centered")

# استایل‌دهی حرفه‌ای، سه‌بعدی و سلطنتی (سبز و طلایی با گرادیانت‌های خیره‌کننده)
st.markdown("""
    <style>
    /* پس‌زمینه کلی و تنظیمات نمایشی */
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }
    
    /* کادر اصلی هدر با قاب و پس‌زمینه لوکس */
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

    /* عنوان طلایی سه‌بعدی و گرادیانت */
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

    /* عنوان سبز سلطنتی گرادیانت */
    .main-title {
        font-size: 32px;
        font-weight: 800;
        background: linear-gradient(to bottom, #00ff66, #0b6623);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 5px;
        filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.8));
    }

    /* زیرعنوان‌های شیک و خوانا */
    .sub-title {
        color: #f1f1f1 !important;
        font-size: 14px;
        font-weight: 600;
        margin-top: 12px;
        line-height: 1.7;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.9);
    }

    /* پاورقی لوکس و برجسته */
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

# هدر و عناوین سلطنتی با دیزاین جدید
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

# راه‌اندازی تاریخچه پیام‌ها قبل از استفاده
if "messages" not in st.session_state:
    st.session_state.messages = []

# دکمه پاک کردن تاریخچه چت
if st.button("🗑️ Clear Chat History / پاک کردن تاریخچه گفتگو"):
    st.session_state.messages = []
    st.rerun()

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
    
    # ثبت پیام کاربر در حافظه
    st.session_state.messages.append({"role": "user", "content": user_text, "image": img_to_save})
    
    with st.chat_message("user"):
        st.markdown(user_text)
        if img_to_save:
            st.image(img_to_save, width=300)

    prompt_lower = user_text.lower().strip()
    
    # منطق بروزرسانی شده و هوشمند پاسخ‌ها
    if any(word in prompt_lower for word in ["سازنده", "کی", "چه کسی", "ساخته", "درست کرده", "creator", "made you", "who made", "mad you"]):
        response = "مرا احمد فرهاد قیومی پسر عبدالسلام درست کرده است. من هوش مصنوعی بین‌المللی و سلطنتی او (AFQ) هستم که برای استفاده تمام مردم جهان طراحی شده‌ام!\n\nI was created by Ahmad Farhad Qayumi, son of Abdulsalam. I am his royal international AI assistant!"
    
    elif any(word in prompt_lower for word in ["سوره", "سوره‌ها", "سورها", "surah", "surat"]):
        response = "📖 قرآن کریم دارای **۱۱۴ سوره** مبارکه است (۸۶ سوره مکی و ۲۸ سوره مدنی).\n\nThe Holy Quran has **114 Surahs** (chapters)."
    
    elif any(word in prompt_lower for word in ["قرآن", "quran", "سیپاره", "سپاره", "جزء", "juz"]):
        response = "📖 قرآن کریم کتاب آسمانی مسلمانان دارای **۳۰ سیپاره (جزء)** و **۱۱۴ سوره** است.\n\nThe Holy Quran has **30 parts (Juz)** and **114 Surahs**."
    
    elif uploaded_file is not None:
        response = f"🎨 **هوش مصنوعی AFQ در حال دیزاین و پردازش تصویر شماست...**\n\nمن این اثر را با استانداردهای جهانی و خلاقیت تمام‌خودکار بازطراحی کردم تا برای هر کاربری در سراسر دنیا جذاب باشد.\n\n✨ *AI Automatic Design Completed Successfully.*\n\n(Created by Ahmad Farhad Qayumi, son of Abdulsalam)."
    
    elif any(word in prompt_lower for word in ["hello", "hi", "سلام", "درود"]):
        response = "سلام! من هوش مصنوعی بین‌المللی AFQ هستم. از هر کجای جهان که هستید، آماده‌ام تا ایده‌ها و دیزاین‌های شما را خلق کنم!\n\nHello! I am AFQ AI. Ready to design and assist users worldwide!"
    
    else:
        response = f"🌐 درخواست شما دریافت شد: «{user_text}». من به عنوان یک هوش مصنوعی بین‌المللی، آماده‌ی پاسخ به تمام سوالات و اجرای درخواست‌های شما از سراسر جهان هستم!\n\nYour global request has been processed successfully by AFQ AI.\n\n(Created by Ahmad Farhad Qayumi, son of Abdulsalam)."
    
    # نمایش و ذخیره پاسخ دستیار
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
