import streamlit as st
import pandas as pd
import random
import os
from datetime import datetime
import pyttsx3
import threading
from streamlit_mic_recorder import speech_to_text
import difflib
import re

def clear_order_inputs():
    st.session_state['order_name'] = ""
    st.session_state['order_address'] = ""

engine = None
try:
    engine = pyttsx3.init()
except Exception:
    engine = None

def speak(text):
    if engine is None:
        return
    def run_speak():
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass
    threading.Thread(target=run_speak).start()

if 'welcome_done' not in st.session_state:
    st.session_state.welcome_done = True
    speak("Welcome to your personal health assistant!")

st.markdown("""
<style>
body { background: #f5f7fa; font-family: 'Inter', sans-serif; }
.stApp {
    background: linear-gradient(135deg,#acecf7 0%, #ffe0e9 50%, #fff9e6 100%);
    min-height: 100vh;
}
.block-container {
    background: rgba(255,255,255,0.93);
    border-radius: 20px;
    padding: 32px 22px;
    margin: 24px auto;
    box-shadow: 0 12px 40px rgba(100,180,220,0.10);
    max-width: 900px;
}
.health-banner {
    background: radial-gradient(circle at 40% 100%, #adf8ff 0%, #ffdee9 100%);
    box-shadow: 0 6px 38px #e8cfff77, 0 2px 12px #b1e5fc80;
    border-radius: 3em;
    text-align: center;
    margin-bottom: 26px;
    padding: 42px 0 32px 0;
    border: 2px solid #6fb1fc;
    position: relative;
    overflow: hidden;
}
.health-banner h1 {
    color: #3468d1 !important;
    font-size: 2.8em;
    font-weight: 770;
    margin-bottom: 8px;
    text-shadow: 2px 2px 12px #fff6, 0 1px 12px #adf8ffaa;
    letter-spacing: 2px;
}
.health-banner p {
    font-size: 1.22em;
    color: #264579;
    letter-spacing: 2px;
    margin-top: 11px;
}
.emoji-bar span {
    font-size:32px; margin:0 14px; cursor: pointer;
}
h3 {
    color: #2a4d69;
}
.cart-item {
    border-bottom: 1px solid #eee;
    padding: 18px 0 10px 0;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="health-banner">
    <h1>💊 Voice-Enabled Health Assistant</h1>
    <p>"Your Wellness Partner, Anytime, Anywhere."</p>
</div>
""", unsafe_allow_html=True)

# Load data
df = pd.read_csv("dataset.csv", encoding='latin1')
doctor_df = pd.read_csv("doctorset.csv", encoding='latin1', delimiter=',', on_bad_lines='skip')
doctor_df.columns = doctor_df.columns.str.strip()
disease_options = sorted(df["Disease"].unique())

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2936/2936956.png", width=90)
    if 'name_text_input' not in st.session_state:
        st.session_state['name_text_input'] = ''
    st.markdown("Or, say your name:")
    spoken_name = speech_to_text(language='en',start_prompt="🎤 Start Recording Name",stop_prompt="⏹️ Stop",just_once=True,use_container_width=True,key='name_voice')
    if spoken_name:
        st.success(f"You said: {spoken_name}")
        st.session_state['name_text_input'] = spoken_name
    name = st.text_input("Your Name", key="name_text_input")
    if 'age_number_input' not in st.session_state:
        st.session_state['age_number_input'] = 0
    st.markdown("Or, say your age (number only):")
    spoken_age = speech_to_text(language='en',start_prompt="🎤 Start Recording Age",stop_prompt="⏹️ Stop",just_once=True,use_container_width=True,key='age_voice')
    if spoken_age:
        st.success(f"You said: {spoken_age}")
        digits = re.findall(r'\d+', spoken_age)
        if digits:
            spoken_age_int = int(digits[0])
            if 0 <= spoken_age_int <= 110:
                st.session_state['age_number_input'] = spoken_age_int
            else:
                st.warning("Age out of valid range.")
        else:
            st.warning("Could not detect age as a number. Please try again.")
    age = st.number_input("Your Age", min_value=0, max_value=110, step=1, key="age_number_input")
    if 'disease_dropdown' not in st.session_state:
        st.session_state['disease_dropdown'] = disease_options[0]
    st.markdown("Or, say the disease name:")
    spoken_disease = speech_to_text(
        language='en',
        start_prompt="🎤 Start Recording Disease",
        stop_prompt="⏹️ Stop",
        just_once=True,
        use_container_width=True,
        key='disease_voice'
    )
    if spoken_disease:
        st.success(f"You said: {spoken_disease}")
        closest = difflib.get_close_matches(spoken_disease.title(), disease_options, n=1)
        if closest:
            st.session_state['disease_dropdown'] = closest[0]
            st.info(f"Disease selected: {closest[0]}")
        else:
            st.error("Spoken disease not found in database. Please try again or use the dropdown.")
    disease = st.selectbox("Select or search Disease", options=disease_options, key="disease_dropdown")
    st.caption("Tip: Start typing, use dropdown, or your voice for any field.")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Health Advice", "Doctors", "Shop & Order", "Joke Corner", "Medical Creativity", "About / Terms"
])

with tab1:
    st.header("Personalized Health Advice")
    if st.button("Get Advice"):
        if name and disease:
            st.session_state.name = name
            st.session_state.age = abs(age)
            st.session_state.disease = disease
            st.session_state.user_input = disease.strip().lower()
            result = df[df['Disease'].str.lower() == st.session_state.user_input.lower()]
            if not result.empty:
                st.session_state.med = result.iloc[0]['Medicines']
                st.session_state.yoga = result.iloc[0]['Yoga']
                st.session_state.diet = result.iloc[0]['Diet']
                st.session_state.advice = result.iloc[0]['Advice']
                st.success("✅ Your data has been saved for future reference!")
                st.session_state.advice_done = True
                patient_data = {
                    "Name": name,
                    "Age": age,
                    "Disease": disease,
                    "Medicines": st.session_state.med,
                    "Yoga": st.session_state.yoga if (10 <= age <= 70) else "Not recommended",
                    "Diet": st.session_state.diet,
                    "Advice": st.session_state.advice,
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                patient_file = "patients_data.csv"
                if os.path.exists(patient_file) and os.path.getsize(patient_file) > 0:
                    patient_df = pd.read_csv(patient_file)
                    patient_df = pd.concat([patient_df, pd.DataFrame([patient_data])], ignore_index=True)
                else:
                    patient_df = pd.DataFrame([patient_data])
                patient_df.to_csv(patient_file, index=False)
            else:
                st.error("Sorry, this disease is not available in the dataset.")
                st.session_state.advice_done = False
        else:
            st.warning("Please fill Name and Disease.")
    if st.session_state.get("advice_done", False):
        st.markdown(f"### Hello, {st.session_state.name}. Your health plan:")
        st.info(f"Medicines: {st.session_state.med}")
        if 10 <= st.session_state.age <= 70:
            st.info(f"Yoga: {st.session_state.yoga}")
        else:
            st.info("Yoga not suitable for your age group.")
        st.info(f"Diet: {st.session_state.diet}")
        st.info(f"Advice: {st.session_state.advice}")

with tab2:
    st.header("Recommended Doctors")
    if st.session_state.get("user_input"):
        matched_docs = doctor_df[doctor_df["Disease"].str.lower() == st.session_state.user_input.lower()]
        doctor_df["Contact"] = doctor_df["Contact"].fillna("No contact available.")
        if not matched_docs.empty:
            for idx, row in matched_docs.iterrows():
                st.markdown(f"""
                <div style='background:#e1f5fe; padding:18px; border-radius:14px; margin:10px 0 18px 0; box-shadow:0 2px 6px #b1e5fc;'>
                <strong>👨‍⚕️ Doctor:</strong> {row['Doctor Name']}<br>
                <strong>Address:</strong> {row['Address']}<br>
                <strong>Contact:</strong> {row['Contact']}<br>
                <strong>Fees:</strong> ₹{row['Fees']}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No doctors found for this disease.")
    else:
        st.info("Get advice first to see doctor recommendations.")

with tab3:
    st.header("🛒 Shop & Order Medical Products")

    product_catalog = [
        {"name": "Paracetamol (Tablet Pack)", "desc": "Pain relief and fever reducer",
         "img": "https://5.imimg.com/data5/SELLER/Default/2022/9/IV/UY/CG/75459511/500mg-paracetamol-tablet-500x500.jpg", "price": 19},
        {"name": "Digital Thermometer", "desc": "Checks body temperature quickly",
         "img": "https://m.media-amazon.com/images/I/711TA1qCEmL._AC_SL1500_.jpg", "price": 249},
        {"name": "N95 Face Mask", "desc": "High-filtration face mask for safety",
         "img": "https://m.media-amazon.com/images/I/71imkuWDnqL.jpg", "price": 49},
        {"name": "Digital Blood Pressure Monitor", "desc": "For measuring blood pressure at home",
         "img": "https://m.media-amazon.com/images/I/71o-naxDnXL._AC_SL1500_.jpg", "price": 1499},
        {"name": "Disposable Syringes (Box)", "desc": "Sterile for single-use medication",
         "img": "https://tse4.mm.bing.net/th/id/OIP.b2l1NDy_2YikCDaFWgE3BwAAAA?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3", "price": 99},
        {"name": "Stethoscope", "desc": "For listening to heartbeat and lungs",
         "img": "https://cdn.britannica.com/29/123229-050-4EE13335/stethoscopes-rubber-tubing-sounds-patient-ears-physician.jpg", "price": 799},
        {"name": "Hand Sanitizer", "desc": "Portable hand sanitizer gel (bottle)",
         "img": "https://tse1.mm.bing.net/th/id/OIP.GZTTDgI3pKY5nDgFwq0whwHaHa?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3", "price": 79},
        {"name": "Glucose Testing Kit", "desc": "Monitoring blood sugar",
         "img": "https://i5.walmartimages.com/asr/d8a90b8e-51df-41fd-a4df-9565d883603a.ca10998800d3f8b870d3ed27b2c039c8.jpeg", "price": 129},
        {"name": "First Aid Kit", "desc": "Kit for small injuries",
         "img": "https://tse3.mm.bing.net/th/id/OIP.FKl7s-p8mGjKkRlg_Jz9PgHaGN?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3", "price": 349},
        {"name": "Antiseptic Solution", "desc": "For wound cleaning and hygiene",
         "img": "https://th.bing.com/th/id/OIP.Il0AgjfDT-mDEoCTtc4JTgHaHa?w=179&h=180&c=7&r=0&o=7&cb=12&dpr=1.3&pid=1.7&rm=3", "price": 89},
        {"name": "Cotton Rolls", "desc": "Soft cotton for medical use",
         "img": "https://th.bing.com/th/id/OIP.c-emSj-jEepSU0PS1AesQwHaF-?w=232&h=187&c=7&r=0&o=7&cb=12&dpr=1.3&pid=1.7&rm=3", "price": 299},
        {"name": "Alcohol Swabs", "desc": "Skin cleaning and sterilization",
         "img": "https://th.bing.com/th/id/OIP.2P0qTAgn7UmtLmlCUw-ftQHaHa?w=203&h=203&c=7&r=0&o=7&cb=12&dpr=1.3&pid=1.7&rm=3", "price": 399},
        {"name": "Medical Tape", "desc": "For securing dressings and bandages",
         "img": "https://tse3.mm.bing.net/th/id/OIP.O4f1XpTrl-3OXUb2XcgqtwHaHa?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3", "price": 49},
        {"name": "Elastic Crepe Bandage", "desc": "Support for sprains and strains",
         "img": "https://th.bing.com/th/id/OIP.4IkiTSNxedptoRj6qnteVgHaHa?w=196&h=196&c=7&r=0&o=7&cb=12&dpr=1.3&pid=1.7&rm=3", "price": 29},
        {"name": "Pulse Oximeter", "desc": "Measures oxygen level in blood",
         "img": "https://tse1.mm.bing.net/th/id/OIP.-BiDDYsRfEiDpk_b6eq4agHaHa?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3", "price": 1699},
        {"name": "Wheelchair", "desc": "Supports mobility for the disabled",
         "img": "https://shop.mobilityworks.com/wp-content/uploads/2017/12/Jazzy1450_Blue_Right.jpg", "price": 7999},
        {"name": "Crutches", "desc": "Aid for walking support",
         "img": "https://i5.walmartimages.com/asr/44a24b73-2544-453c-80a7-1c50ab0db462_1.50c143c69349680a61795eec6b69a728.jpeg", "price": 499},
        {"name": "Medical Gloves (Box)", "desc": "Disposable gloves for hygiene",
         "img": "https://tse4.mm.bing.net/th/id/OIP.N65PJMJVfOBAoQoTylH0YwHaGC?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3", "price": 49},
        {"name": "Ointment Tube", "desc": "Topical medicine for wounds",
         "img": "hhttps://th.bing.com/th/id/OIP.BJ7LAh0372AIM6Etz4fyCgHaE9?w=275&h=184&c=7&r=0&o=7&cb=12&dpr=1.3&pid=1.7&rm=3", "price": 99},
        {"name": "IV Infusion Set", "desc": "For IV medication delivery",
         "img": "https://5.imimg.com/data5/SELLER/Default/2023/12/370729918/PY/OY/QU/114523301/iv-infusion-set-500x500.jpg", "price": 89},
        {"name": "Hot Water Bag", "desc": "Relief from body aches",
         "img": "https://5.imimg.com/data5/SELLER/Default/2021/1/FL/BL/UP/120091826/71ijo1kqqdl-sl1500-.jpg", "price": 599}
    ]

    if 'cart' not in st.session_state:
        st.session_state.cart = []

    pidx = st.selectbox("Select Product", options=range(len(product_catalog)),
                        format_func=lambda x: product_catalog[x]['name'])

    col1, col2 = st.columns([1.4, 2])
    with col1:
        st.image(product_catalog[pidx]['img'], width=160)
        st.markdown(f"**{product_catalog[pidx]['name']}**")
        st.caption(product_catalog[pidx]['desc'])
        st.markdown(f"**Price: ₹{product_catalog[pidx]['price']}**")
    with col2:
        qty = st.number_input("Quantity", 1, 500, 1, key='qty_input')
        if st.button("Add to Cart"):
            st.session_state.cart.append({
                "Product": product_catalog[pidx]['name'],
                "Quantity": qty,
                "Img": product_catalog[pidx]['img'],
                "Price": product_catalog[pidx]['price']
            })
            st.success(f"{product_catalog[pidx]['name']} (x{qty}) added to cart!")

    st.markdown("---")
    st.markdown("### Cart Preview")
    cart_total = 0
    remove_idx = None
    for idx, item in enumerate(st.session_state.cart):
        item_total = item['Price'] * item['Quantity']
        cart_total += item_total
        cart_cols = st.columns([1, 3, 1])
        with cart_cols[0]:
            st.image(item['Img'], width=90)
        with cart_cols[1]:
            st.markdown(f"**{item['Product']}**")
            st.write(f"Quantity: {item['Quantity']} | Price: ₹{item['Price']} ea | Item total: ₹{item_total}")
        with cart_cols[2]:
            if st.button(f"Remove", key=f"remove_{idx}"):
                remove_idx = idx
    if remove_idx is not None:
        st.session_state.cart.pop(remove_idx)

    if len(st.session_state.cart) > 0:
        st.markdown(f"<h4 style='text-align:right; color:green;'>Total: ₹{cart_total}</h4>", unsafe_allow_html=True)
    else:
        st.info("Your cart is empty.")

    st.markdown("---")
    st.subheader("Place Order")

    with st.form("order_form", clear_on_submit=False):
        user_name = st.text_input("Your Name for Order", key="order_name")
        address = st.text_area("Your Delivery Address", key="order_address")
        submit_order = st.form_submit_button("Submit Order")

    if submit_order:
        if user_name.strip() != "" and address.strip() != "" and len(st.session_state.cart) > 0:
            order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            items_string = "; ".join(
                f"{item['Product']} x{item['Quantity']} (₹{item['Price']} ea)"
                for item in st.session_state.cart
            )
            order_data = {
                "Name": user_name,
                "Time": order_time,
                "Address": address,
                "Items": items_string,
                "TotalPrice": cart_total
            }
            file = "shoperslist.csv"
            try:
                if os.path.exists(file) and os.path.getsize(file) > 0:
                    old_df = pd.read_csv(file)
                    new_df = pd.DataFrame([order_data])
                    combined_df = pd.concat([old_df, new_df], ignore_index=True)
                    combined_df.to_csv(file, index=False)
                else:
                    pd.DataFrame([order_data]).to_csv(file, index=False)
                st.success("Order placed! Thank you.")
                st.session_state.cart.clear()
            except Exception as e:
                st.error(f"Error saving order: {e}")
        else:
            st.warning("Please fill all details and add at least one product to your cart.")

with tab4:
    st.header("Joke Corner 😆")
    jokes = [
        "Santa: Doctor saab, mera dimag itna slow hai ki kal se sab cheezen bhool raha hoon.\nBanta: Arre Santa,\ntum pariksha ki taiyari kar rahe ho ya exam ke darr se bhool rahe ho?",
        "Santa: Doctor saab, ek tum mujhe cure kar sakte ho?\nDoctor: Kyu nahi, kya problem hai?\nSanta: Jab bhi mein kisi se milta hoon, woh mere se door ho jaate hain.\nDoctor: Arre ye to pyar ka lakshan hai, tujhe girlfriend chahiye!",
        "Santa: Mujhe aisa dawa do jis se mein hamesha active rahoon.\nDoctor: Toh roz workout ka schedule banao.\nSanta: Doctor saab, main toh lene ki baat kar raha tha dawa!",
        "Banta: Doctor saab, bar bar pareshan karta hai mera dimag,\nkya karoon?\nDoctor: Thoda meditation karo.\nBanta: Acha, toh phone mein app download karta hoon, sahi hai?"
    ]
    if "joke" not in st.session_state:
        st.session_state.joke = random.choice(jokes)
    if st.button("Tell me a new Joke"):
        st.session_state.joke = random.choice(jokes)
    for line in st.session_state.joke.split('\n'):
        st.info(line)

with tab5:
    st.header("Medical Creativity Zone 🎨")
    facts = [
        "Your heart beats about 100,000 times a day!",
        "Humans are the only animals that shed emotional tears.",
        "Blood makes up about 8% of your body weight.",
        "An adult human body has 206 bones.",
        "The strongest muscle in the body is the tongue!"
    ]
    if st.button("Show Medical Fact"):
        st.session_state.fact = random.choice(facts)
    if "fact" not in st.session_state:
        st.session_state.fact = random.choice(facts)
    st.info(f"💡 {st.session_state.fact}")

    st.subheader("Health Riddles")
    riddles = [
        "I am always hungry, I will die if not fed, but whatever I touch will soon turn red. What am I?",
        "I can be cracked, made, told, and played. What am I?",
        "The more you take from me, the bigger I become. What am I?",
        "I get wetter the more I dry. What am I?",
        "What has hands but cannot clap?",
        "I have cities but no houses, forests but no trees, and rivers but no water. What am I?",
        "What can run but never walks, has a mouth but never talks?",
        "What has an eye but cannot see?",
        "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        "What begins with T, ends with T, and has T in it?"
    ]
    answers = [
        "Fire 🔥",
        "A joke 😄",
        "A hole 🕳️",
        "A towel 🧺",
        "A clock 🕰️",
        "A map 🗺️",
        "A river 🌊",
        "A needle 🪡",
        "An echo 📣",
        "A teapot 🍵"
    ]
    if "riddle_index" not in st.session_state:
        st.session_state.riddle_index = 0
    if st.button("Show Next Riddle"):
        st.session_state.riddle_index = (st.session_state.riddle_index + 1) % len(riddles)
    st.info(riddles[st.session_state.riddle_index])
    with st.expander("Show Answer"):
        st.write(answers[st.session_state.riddle_index])
    st.markdown("---")
    st.subheader("Inspirational Medical Quote")
    st.write("“The greatest wealth is health.” – Virgil")

with tab6:
    st.header("About, Terms & Disclaimer 📃")
    st.markdown("""
    <h3>About This App</h3>
    <p>This Voice-Enabled Health Assistant app is your friendly companion for personalized health advice, doctor recommendations, and good humor.<br>
    It brings creativity and medical knowledge together for a fun and educational experience.</p>
    <h3>How to Use</h3>
    <ol>
    <li>Enter your name, age, and disease in the sidebar.</li>
    <li>Get tailored health advice on the 'Health Advice' tab.</li>
    <li>Find doctors for your condition in the 'Doctors' tab.</li>
    <li>Shop medical products and place orders in 'Shop & Order'.</li>
    <li>Enjoy medical-hinglish jokes and other fun content in the 'Joke Corner'.</li>
    <li>Explore facts, riddles, and quotes in 'Medical Creativity'.</li>
    <li>Read about terms, conditions, and developer info here.</li>
    </ol>
    <h3>Terms & Conditions</h3>
    <p>This app is for informational purposes only and is NOT a substitute for professional medical advice.<br>
    Always consult a qualified healthcare provider for diagnosis and treatment.<br>
    The developer disclaims all liability arising from use of this app.</p>
    <h3>Privacy</h3>
    <p>No personal data leaves your device; patient info is saved locally in CSV files.<br>
    Use responsibly.</p>
    <h3>Disclaimer</h3>
    <p>Medical info presented here is for education and general wellness only.</p>
    <h3>Customer Care Contact Information</h3>
    <p><b>Phone: </b><br>Call us toll-free at <b>9754511500</b><br>Available Monday to Friday, 9 AM to 6 PM IST<br></p>
    <p><b>E-mail: </b><br>For support and queries, email us at: <br><b>support@yourhealthassistant.com</b></p>
    """, unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown("<p style='text-align:center; color:#3468d1; font-weight:bold; font-size:1.2em;'>Developed by Amit Sharma</p>", unsafe_allow_html=True)

