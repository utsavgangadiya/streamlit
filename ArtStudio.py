import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="The Canvas | Artist Portfolio",
    page_icon="🎨",
    layout="wide"
)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🎨 Artist Hub")
st.sidebar.write("Welcome to my digital gallery!")

# Dropdown Menu
menu_choice = st.sidebar.selectbox(
    "Go to Section:",
    ["Home & Bio", "Gallery", "Commission a Piece", "Contact"]
)

# Interactive Sidebar Widgets
st.sidebar.markdown("---")
st.sidebar.subheader("Support the Artist")
like_art = st.sidebar.checkbox("Do you like my art style?")
if like_art:
    st.sidebar.success("Thank you for your support! ❤️")

# --- MAIN CONTENT ---

# 1. HOME & BIO SECTION
if menu_choice == "Home & Bio":
    st.title("🖌️ Welcome to the Studio of Alex Vance")
    st.subheader("Abstract & Digital Artist based in Seattle")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # A placeholder artist avatar/photo
        st.image("https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?auto=format&fit=crop&w=400&q=80", 
                 caption="Alex Vance, Visual Artist", use_container_width=True)
    with col2:
        st.markdown("""
        ### About Me
        Hello! I am Alex. I specialize in blending physical acrylic textures with modern digital tools. 
        My work explores the intersections of human emotion, technology, and nature. 
        
        * **Mediums:** Acrylics, Digital Illustration, Procreate, 3D Renderings.
        * **Inspirations:** Vaporwave, Cyberpunk, and Classic Impressionism.
        
        *Use the sidebar menu to navigate the gallery and explore my work!*
        """)

# 2. GALLERY SECTION
elif menu_choice == "Gallery":
    st.title("🖼️ Art Gallery")
    st.write("Browse through some of my favorite recent works. Click on images to view them in full size.")
    
    # Filter using tabs
    category = st.radio("Filter by Category:", ["All", "Digital Art", "Abstract Paintings"])
    
    col1, col2, col3 = st.columns(3)
    
    # Sample Image URLs
    img1 = "https://images.unsplash.com/photo-1541701494587-cb58502866ab?auto=format&fit=crop&w=600&q=80"
    img2 = "https://images.unsplash.com/photo-1549887534-1541e9326642?auto=format&fit=crop&w=600&q=80"
    img3 = "https://images.unsplash.com/photo-1515405295579-ba7b45403062?auto=format&fit=crop&w=600&q=80"

    if category == "All" or category == "Digital Art":
        with col1:
            st.image(img1, caption="Neon Dreamscape (Digital, 2024)", use_container_width=True)
        with col2:
            st.image(img2, caption="Metropolis Rain (Digital, 2025)", use_container_width=True)
            
    if category == "All" or category == "Abstract Paintings":
        with col3:
            st.image(img3, caption="Ember & Ice (Acrylic on Canvas, 2026)", use_container_width=True)

# 3. COMMISSION SECTION
elif menu_choice == "Commission a Piece":
    st.title("💼 Commission Custom Art")
    st.write("Want a custom piece tailored to your home or office? Let's design it together!")
    
    # Commission Form
    with st.form("commission_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email Address")
        
        medium = st.selectbox("Preferred Medium", ["Digital Painting", "Acrylic Canvas", "Watercolors", "Oil on Canvas"])
        
        size = st.select_slider(
            "Select Canvas Size (Inches)",
            options=["12x12", "16x20", "24x36", "36x48", "Custom Huge"]
        )
        
        description = st.text_area("Describe your vision (Colors, mood, references...)")
        
        submit_btn = st.form_submit_button("Send Commission Inquiry")
        
        if submit_btn:
            if name and email and description:
                st.success(f"Thank you, {name}! Your commission request for a {size} {medium} has been sent. I will email you at {email} within 48 hours.")
            else:
                st.warning("Please fill out your name, email, and description so I can contact you!")

# 4. CONTACT SECTION
elif menu_choice == "Contact":
    st.title("✉️ Get in Touch")
    st.write("For exhibitions, licensing, or general inquiries, please contact me through the details below:")
    
    st.markdown("""
    * 📧 **Email:** contact@alexvanceart.com
    * 📸 **Instagram:** [@AlexVanceArt](https://instagram.com)
    * 🐦 **Twitter/X:** [@AlexVanceArt](https://twitter.com)
    * 📍 **Studio Location:** Pier 56, Seattle, WA
    """)
    
    # Guestbook feature
    st.subheader("✍️ Leave a Note in the Guestbook")
    note = st.text_input("Type your message here:")
    if st.button("Sign Guestbook"):
        if note:
            st.info(f"Guestbook Entry Added: \"{note}\" — Thanks for stopping by!")
        else:
            st.error("Please enter a message before submitting!")