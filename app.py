
import streamlit as st

# تنظیمات صفحه
st.set_page_config(page_title="AFQ AI", page_icon="🤖", layout="centered")

# عنوان جذاب برنامه
st.title("🤖 هوش مصنوعی AFQ")
st.write("سلام! من AFQ هستم؛ دستیار هوشمند شما. هر سوالی دارید بپرسید تا با هم گفتگو کنیم.")

# راه‌اندازی تاریخچه پیام‌ها در حافظه مرورگر
if "messages" not in st.session_state:
    st.session_state.messages = []

# نمایش پیام‌های قبلی چت
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# کادر دریافت پیام از کاربر در پایین صفحه
if prompt := st.chat_input("سؤال یا پیام خود را اینجا بنویسید..."):
    # اضافه کردن پیام کاربر به تاریخچه
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # پاسخ هوش مصنوعی (فعلاً به صورت هوشمند و دوستانه)
    response = f"سلام فرهاد عزیز! پیامت را دریافت کردم: «{prompt}». من دستیار AFQ هستم و به‌زودی به مدل‌های پیشرفته‌تر هوش مصنوعی متصل می‌شوم تا دقیق‌تر پاسخگویت باشم!"
    
    # نمایش پاسخ هوش مصنوعی
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # اضافه کردن پاسخ به تاریخچه
    st.session_state.messages.append({"role": "assistant", "content": response})
