import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, Streamlit!")

with st.sidebar:
    st.title("Menu")
    menu = st.multiselect("select food",["pizza","panipuri","pavbhaji","vadapav"])
    cq =st.slider("cachap pakage",0,10,2)
    st.button("order")
    st.text(f"your order is {menu} with extra cathep {cq} ")



# 1. Properly create your columns (spelled 'col1', 'col2')
col1, col2 = st.columns(2)




# First Column
with col1:
    st.image("https://thumbs.dreamstime.com/b/shuddha-desi-ghee-clarified-butter-desi-ghee-clarified-butter-glass-copper-container-ceramic-jar-spoon-104387643.jpg", width=200)
    dg1 = st.number_input("desi ghee1", min_value=0, max_value=100, key="desi_ghee_1")

    st.image("https://thumbs.dreamstime.com/b/shuddha-desi-ghee-clarified-butter-desi-ghee-clarified-butter-glass-copper-container-ceramic-jar-spoon-104387643.jpg", width=200)
    dg2 = st.number_input("desi ghee2", min_value=0, max_value=100, key="desi_ghee_2")

# Second Column
with col2:
    st.image("https://thumbs.dreamstime.com/b/shuddha-desi-ghee-clarified-butter-desi-ghee-clarified-butter-glass-copper-container-ceramic-jar-spoon-104387643.jpg", width=200)
    cg1 = st.number_input("cow ghee1", min_value=0, max_value=100, key="cow_ghee_1")

    st.image("https://thumbs.dreamstime.com/b/shuddha-desi-ghee-clarified-butter-desi-ghee-clarified-butter-glass-copper-container-ceramic-jar-spoon-104387643.jpg", width=200)
    cg2 = st.number_input("cow ghee2", min_value=0, max_value=100, key="cow_ghee_2")


if st.button("place order"):
    st.header("your orders")
    
    # Calculate total quantity
    total_items = dg1 + dg2 + cg1 + cg2
    st.text(f"Total items ordered: {total_items}")
    
    # Optional: Breakdown of what was selected
    st.write(f"- Desi Ghee 1: {dg1} | Desi Ghee 2: {dg2}")
    st.write(f"- Cow Ghee 1: {cg1} | Cow Ghee 2: {cg2}")