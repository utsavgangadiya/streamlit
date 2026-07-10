import streamlit as st

# Page Title
st.set_page_config(page_title="Student Portal")

st.title("Student Information Portal")
st.write("Fill in the student details below.")

# Name
name = st.text_input("Enter Student Name")

# Age
age = st.number_input("Enter Age", min_value=1, max_value=100)

# Gender
gender = st.radio("Gender", ["Male", "Female", "Other"])

# Course
course = st.selectbox(
    "Select Course",
    ["BCA", "B.Tech", "B.Com", "MCA", "MBA"]
)

# Skills
skills = st.multiselect(
    "Programming Skills",
    ["Python", "Java", "C++", "JavaScript", "SQL"]
)

# Percentage
percentage = st.slider(
    "Percentage",
    0,
    100,
    75
)

# Upload Photo
photo = st.file_uploader(
    "Upload Profile Photo",
    type=["jpg", "jpeg", "png"]
)

# Accept Terms
agree = st.checkbox("I confirm the above information is correct.")

# Submit Button
if st.button("Submit"):

    if name == "":
        st.warning("Please enter your name.")

    elif not agree:
        st.error("Please accept the declaration.")

    else:
        st.success("Student Information Submitted Successfully!")

        st.subheader("Student Details")

        st.write("**Name:**", name)
        st.write("**Age:**", age)
        st.write("**Gender:**", gender)
        st.write("**Course:**", course)
        st.write("**Skills:**", ", ".join(skills))
        st.write("**Percentage:**", percentage, "%")

        if photo:
            st.image(photo, width=180)