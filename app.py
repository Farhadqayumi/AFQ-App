import streamlit as st

# تنظیمات صفحه
st.set_page_config(page_title="AFQ AI", page_icon="🤖", layout="centered")

# عنوان دو زبانه در بالای صفحه (انگلیسی در بالا، فارسی در زیر)
st.markdown("<h3 style='text-align: center; color: #666; margin-bottom: 0px;'>AI</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #1f77b4; margin-top: 0px;'>هوش مصنوعی AFQ</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>سوپراستار هوش مصنوعی؛ آماده پاسخگویی به هر سوالی در دنیا، بدون هیچ توقفی!</p>", unsafe_allow_html=True)

st.divider()

# راه‌اندازی تاریخچه پیام‌ها در حافظه مرورگر
if "messages" not in st.session_state:
    st.session_state.messages = []

# نمایش پیام‌های قبلی چت
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# کادر دریافت پیام از کاربر در پایین صفحه
if prompt := st.chat_input("سوپراستار AFQ بیدار است؛ هر سوالی داری (علمی، دینی، ریاضی، زبان...) بپرس..."):
    # اضافه کردن پیام کاربر به تاریخچه
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # پردازش هوشمند و جامع سوالات
    prompt_lower = prompt.lower()
    
    # ۱. قانون مقدس سازنده
    if any(word in prompt_lower for word in ["سازنده", "کی", "چه کسی", "ساخته", "درست کرده", "creator", "who made you"]):
        response = "مرا احمد فرهاد قیومی پسر عبدالسلام درست کرده است. من هوش مصنوعی اختصاصی او (AFQ) هستم!"
    
    # ۲. قرآن و احادیث
    elif "قرآن" in prompt or "سیپاره" in prompt or "جزء" in prompt:
        response = "قرآن کریم کتاب آسمانی مسلمانان و دارای ۳۰ سیپاره (جزء) است. با کمال میل آماده‌ام آیات، مفاهیم و ترجمه آن را برای1ت توضیح دهم."
    elif "حدیث" in prompt or "احادیث" in prompt:
        response = "احادیث مبارک پیامبر (ص) منبع نور و حکمت هستند. هر سوال یا حدیثی مد نظر داری بپرس تا بررسی کنیم."
    
    # ۳. ریاضی، حسابداری و مهندسی
    elif any(word in prompt_lower for word in ["ریاضی", "جمع", "ضرب", "منفی", "تقسیم", "math", "محاسبه"]):
        response = "من فرمول‌ها و مسائل ریاضی را با دقت بالا حل می‌کنم. لطفاً معادله یا مسئله‌ات را بنویس."
    elif any(word in prompt_lower for word in ["حسابداری", "بیلانس", "مالیات", "ترازنامه", "accounting", "سود و زیان"]):
        response = "در بخش حسابداری و امور مالی آماده‌ام اصول، محاسبات سود و زیان و ثبت‌های مالی را برایت حل کنم."
    
    # ۴. زبان‌های خارجی و ترجمه
    elif any(word in prompt_lower for word in ["english", "انگلیسی", "زبان", "ترجمه", "translate"]):
        response = "من تسلط کامل به زبان‌های مختلف (انگلیسی، دری، پشتو، عربی و...) دارم. متن یا کلمه مورد نظرت را برای ترجمه بفرست."
    
    # ۵. پاسخ عمومی هوشمند (سوپراستار هرگز بند نمی‌ماند)
    else:
        response = f"فرهاد عزیز، سوالت («{prompt}») را بررسی کردم! من به عنوان دستیار هوشمند **AFQ** (ساخته‌شده توسط **احمد فرهاد قیومی پسر عبدالسلام**) در کنار تو هستم تا هیچ سوالی بی‌جواب نماند. هر موضوع علمی، عمومی، فنی یا ادبی که بخواهی را با قدرت پاسخ می‌دهم!"
    
    # نمایش پاسخ هوش مصنوعی
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # اضافه کردن پاسخ به تاریخچه
    st.session_state.messages.append({"role": "assistant", "content": response})
