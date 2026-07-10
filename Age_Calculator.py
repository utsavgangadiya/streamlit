from datetime import date
import streamlit as st

st.set_page_config(page_title="Age Calculator")

st.title("Age Calculator")
st.write("Select your date of birth to calculate your age.")

dob = st.date_input(
    "Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

if st.button("Calculate Age"):
    today = date.today()

    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    if days < 0:
        from calendar import monthrange

        previous_month = today.month - 1 if today.month > 1 else 12
        previous_year = today.year if today.month > 1 else today.year - 1

        days += monthrange(previous_year, previous_month)[1]
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    st.success(f"Your Age is: {years} Years, {months} Months, {days} Days")

    total_days = (today - dob).days
    st.info(f" Total Days Lived: {total_days:,}")

    next_birthday = date(today.year, dob.month, dob.day)

    if next_birthday < today:
        next_birthday = date(today.year + 1, dob.month, dob.day)

    days_left = (next_birthday - today).days

    st.write(f" Days Until Next Birthday: **{days_left}**")