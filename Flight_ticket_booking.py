import streamlit as st
from datetime import date

st.set_page_config(page_title="Flight Ticket Booking")

st.title("Flight Ticket Booking System")
st.write("Book your flight in a few simple steps.")

st.header("Passenger Details")

name = st.text_input("Passenger Name")

age = st.number_input("Age", min_value=1, max_value=100)

gender = st.radio(
    "Gender",
    ["Male", "Female", "Other"]
)

st.header("Flight Details")

from_city = st.selectbox(
    "From",
    ["Ahmedabad", "Delhi", "Mumbai", "Bangalore", "Chennai"]
)

to_city = st.selectbox(
    "To",
    ["Ahmedabad", "Delhi", "Mumbai", "Bangalore", "Chennai"]
)

travel_date = st.date_input(
    "Travel Date",
    min_value=date.today()
)

flight_class = st.selectbox(
    "Class",
    ["Economy", "Business", "First Class"]
)

passengers = st.slider(
    "Number of Passengers",
    1,
    10,
    1
)

meal = st.checkbox("Add Meal (+₹500 per passenger)")

payment = st.radio(
    "Payment Method",
    ["UPI", "Credit Card", "Debit Card", "Cash"]
)

# Price Calculation
price = 3000

if flight_class == "Business":
    price = 6000
elif flight_class == "First Class":
    price = 10000

total = price * passengers

if meal:
    total += 500 * passengers

st.divider()

if st.button("Book Ticket"):

    if name == "":
        st.warning("Please enter passenger name.")

    elif from_city == to_city:
        st.error("Departure and destination cannot be the same.")

    else:

        st.success("✅ Flight Booked Successfully!")

        st.subheader("Booking Summary")

        st.write(f"**Passenger:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**From:** {from_city}")
        st.write(f"**To:** {to_city}")
        st.write(f"**Travel Date:** {travel_date}")
        st.write(f"**Class:** {flight_class}")
        st.write(f"**Passengers:** {passengers}")
        st.write(f"**Meal:** {'Yes' if meal else 'No'}")
        st.write(f"**Payment Method:** {payment}")

        st.subheader("Total Fare")
        st.success(f"₹ {total}")