# 🎙️ Voice-Enabled Health Assistant 🏥

**Your personal health companion with voice commands!**  
Speak name, age, disease → Get medicines, yoga, diet advice instantly! [file:1][file:3]

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Voice](https://img.shields.io/badge/Voice-Enabled-00D4AA?style=for-the-badge&logo=microphone&logoColor=white)](https://streamlit.io/)

## ✨ **Key Features**

| Feature | Description |
|---------|-------------|
| 🎤 **Voice Input** | Speak name, age, disease using browser mic |
| 🩺 **Health Advice** | 50+ diseases with medicines/yoga/diet [file:3] |
| 👨‍⚕️ **Doctor Finder** | Specialists with contact details |
| 🛒 **Medical Shop** | Thermometer(₹249), Mask(₹49), BP Monitor(₹1499) |
| 😂 **Hinglish Jokes** | Santa-Banta medical humor |
| 📚 **Fun Facts** | Heart beats 100,000 times daily! |

## 🚀 **5 Minute Setup**

git clone https://github.com/YOUR_USERNAME/voice-health-assistant
cd voice-health-assistant
pip install -r requirements.txt
streamlit run app.py

text

**Open**: `http://localhost:8501` → Allow mic → Ready!

## 📁 **Project Structure**
├── app.py # Main app (22K+ lines)​
├── dataset.csv # 50+ diseases database​
├── patients_data.csv # User health history​
└── requirements.txt

text

## 🩺 **Sample Outputs**

**Input**: Amit, 19, Fatty Liver [file:2]  
**Output**:
✅ Medicines: Lifestyle modification
✅ Yoga: Bhujangasana
✅ Diet: Low fat, high fiber
✅ Advice: Avoid alcohol

text

**Malaria Example**:
✅ Medicines: ACTs + Paracetamol
✅ Yoga: Anulom Vilom
✅ Diet: Khichdi, coconut water
✅ Advice: Consult doctor immediately!

text

## 🛒 **Shopping Cart Demo**
N95 Mask → ₹49 ✅ Added
Thermometer → ₹249 ✅ Added
Pulse Oximeter → ₹1699 ✅ Added
Total: ₹1997 → Place Order!

text

## 🎉 **Usage Flow**
Sidebar → Speak: "Amit" → "21" → "Cough Cold"

Health tab → Syrups + Warm soup recommendations

Doctors tab → Condition-specific specialists

Shop → Add products → Checkout

Jokes → "Santa to doctor..." 😂​

text

## 📊 **Dataset Coverage** [file:3]
- **Common**: Cold, Fever, Cough, Diabetes, Hypertension
- **Serious**: Dengue, Malaria, COVID-19, Heart Disease 
- **Skin**: Eczema, Psoriasis, Ringworm
- **Total**: 50+ medical conditions!

## 🛠️ **Tech Stack**

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit + Custom CSS |
| **Voice** | streamlit-micrecorder + pyttsx3 |
| **Data** | Pandas + CSV files |
| **Storage** | Local CSV (privacy-first) |

## 🤝 **How to Contribute**
1. Add new diseases to `dataset.csv`
2. Improve voice recognition accuracy
3. Add medical products to shopping cart
4. Enhance UI/UX design

## 📈 **Live Demo** (Optional)
Deploy free on GitHub Pages:
1. Settings → Pages → Deploy from "main" branch
2. Get live URL: `https://YOUR_USERNAME.github.io/voice-health-assistant`

## ⚠️ **Disclaimer**
**Educational app only. Not medical advice.** Always consult doctors. All data stored locally - no cloud upload. [file:1]

## 👨‍💻 **Author**
**Amit Sharma**  
💻 Computer Science Student | 🎓 Algorithm Enthusiast  
📧 support@yourhealthassistant.com  
📞 +91 9712345670

---

**⭐ Star if helpful!** **🚀 Fork & contribute!** **📱 Share with friends!** [file:1][file:2][file:3][web:4]
