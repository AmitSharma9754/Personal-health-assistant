#  Personal Health Assistant  
*A Voice-Enabled Smart Healthcare Support System*

This project is a **Streamlit-based Personal Health Assistant** that provides:  
✔ Personalized health advice  
✔ Doctor recommendations  
✔ Medical product shopping with cart system  
✔ Voice input support  
✔ Jokes, facts, riddles & creativity zone  
✔ Local patient data storage  

The system uses **voice recognition**, **CSV datasets**, and **real-time UI components** to create an interactive healthcare experience.

---

##  Features

-  **Voice-enabled input** (Name, Age, Disease)  
-  **Personalized health advice** from dataset  
-  **Doctor recommendations** by disease  
-  **Shop & Order medical products**  
-  Saves order history locally  
-  Patient data stored in CSV  
-  Jokes, riddles & creativity section  
-  Beautiful UI with gradient theme  
-  No cloud data — **fully offline privacy**

---

##  Project Structure

```
Personal_Health_Assistant/
│
├── app.py
├── dataset.csv
├── doctorset.csv
├── patients_data.csv
├── shoperslist.csv
└── README.md
```

---

## 🛠 Tech Stack

- **Python 3.x**
- **Streamlit**
- **Pandas**
- **Speech-to-Text (streamlit_mic_recorder)**
- **Pyttsx3 (Text-to-Speech)**
- **CSS for UI styling**

---

##  Installation & Setup

### 1️⃣ Clone the repository  

**Repository Link:**  
👉 https://github.com/AmitSharma9754/Personal-health-assistant  

**Clone using Git:**  
git clone https://github.com/AmitSharma9754/Personal-health-assistant.git
cd Personal-health-assistant


### 2️⃣ Install dependencies  
```
pip install -r requirements.txt
```

### 3️⃣ Run the App

Run the Streamlit application using:

```bash
streamlit run app.py
```


---

##  Features & Modules

| Module / Section     | Description |
|----------------------|-------------|
| Health Advice        | Personalized advice: Medicines, Yoga, Diet, Tips |
| Doctors Suggestion   | Shows best doctors related to the disease |
| Shop & Order         | Add items to cart → generate order list (CSV) |
| Voice Input          | Speak your Name, Age, Disease |
| Jokes & Riddles      | Fun medical-based jokes, riddles, facts |
| Creativity Zone      | Interesting facts & quotes |
| Local Data Storage   | patient history + orders saved as CSV |

---

##  Technologies Used
- Python  
- Streamlit  
- Pandas  
- Pyttsx3 (Text-to-Speech)  
- Speech-to-Text (Mic Recorder)  
- Custom CSS UI  

---

##  How to Use

1️⃣ Enter or Speak:
- Name  
- Age  
- Disease  

2️⃣ Click **Get Advice**  
You will receive:
- Medicines  
- Yoga (based on age)  
- Diet  
- Important medical advice  

3️⃣ Doctor recommendations appear automatically  
4️⃣ Shop any product and place order  
5️⃣ Enjoy jokes, facts, riddles, and more!  

---

##  Project Structure

```
Personal_Health_Assistant/
│
├── app.py
├── dataset.csv
├── doctorset.csv
├── patients_data.csv
├── shoperslist.csv
└── README.md
```

---

##  Screenshots

### 🔹 Home Page  
![Homepage](https://github.com/user-attachments/assets/1128cdd7-e2ca-42ec-9222-a3a600f2031b)

### 🔹 Health Advice Form  
![HealthAdvice](https://github.com/user-attachments/assets/155cabd7-85d8-4782-b7b5-0ff5937bb593)

### 🔹 Doctor Recommendation  
![DoctorRecommendation](https://github.com/user-attachments/assets/62e6a5da-6745-4048-8390-7999ee727e9b)


---

##  Disclaimer

This application is created **strictly for educational and informational purposes only**.  
It is **NOT a medical device** and does **NOT** provide professional medical diagnosis, treatment, or prescriptions.

All suggestions and outputs are based on pre-recorded datasets and simple logic.  
For any real health concerns, always consult a **qualified healthcare professional**.

The developer is **not responsible** for any decisions made based on this application's results.


---

##  Contribution

You can contribute by:
- Adding new diseases  
- Improving UI  
- Enhancing voice features  
- Fixing bugs  

Pull requests are welcome!

---

##  Contact

**Amit Sharma**   
📩 Email: Amitsharma97545@gmail.com  
🐙 GitHub: [https://github.com/AmitSharma9754/Personal-health-assistant](https://github.com/AmitSharma9754)
