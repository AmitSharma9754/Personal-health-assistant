# Personal Health Assistant

A Streamlit-based web application providing educational health information, doctor recommendations, and medical product catalog through voice-enabled interface.

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)

## Project Overview

This application provides general health information for over 50 medical conditions, including recommendations for medication, yoga practices, dietary guidelines, and wellness advice sourced from `dataset.csv`. Features include voice input processing, doctor database lookup, medical shopping cart, and local data storage.

## Core Features

| Module | Functionality |
|--------|---------------|
| Voice Interface | Speech-to-text conversion for name, age, and condition input |
| Health Database | 50+ conditions with medication, yoga, diet, and advice |
| Doctor Directory | Condition-specific specialist listings with contact information |
| Product Catalog | Medical supplies inventory with shopping functionality |
| Educational Content | Medical facts, wellness information, and quotes |
| Data Management | Local CSV storage for privacy |

## Technical Implementation

### System Architecture

Personal-health-assistant/
├── app.py # Primary Streamlit application
├── dataset.csv # Medical condition database
├── patients_data.csv # Patient consultation history
├── shoperslist.csv # Shopping transaction records
└── requirements.txt # Python dependencies


### Technology Stack

| Component          | Technology                          |
|--------------------|-------------------------------------|
| Frontend Framework | Streamlit with custom CSS           |
| Voice Processing   | streamlit-micrecorder, pyttsx3      |
| Data Processing    | pandas for CSV operations           |
| Storage            | Local file system (CSV format)      |
| Deployment         | Streamlit Cloud / GitHub Pages      |

## Deployment Instructions

git clone https://github.com/AmitSharma9754/Personal-health-assistant.git
cd Personal-health-assistant
pip install -r requirements.txt
streamlit run app.py

**Access URL**: `http://localhost:8501`  
**Browser Requirements**: Microphone permissions required for voice functionality

## Sample Usage Scenarios

### Case Study 1: Fatty Liver Consultation
Patient: Amit Sharma, Age 19
Input: "Fatty Liver"
Recommendations:

Medications: Lifestyle modification

Yoga: Bhujangasana

Diet: Low fat, high fiber

Advice: Avoid alcohol consumption

### Case Study 2: Malaria Information
Recommendations:

Medications: ACTs + paracetamol (consult physician)

Yoga: Anulom Vilom post-recovery

Diet: Khichdi, coconut water, easily digestible foods

## Data Privacy & Security

- Local Storage Only: All patient data stored in `patients_data.csv` on user device
- No Cloud Transmission: Zero data upload to external servers
- No Authentication Required: Anonymous usage without account creation
- CSV Format: Transparent, editable data storage

## Dataset Coverage

**Medical Conditions (50+)**: Cold, Fever, Cough, Influenza, Asthma, Pneumonia, Tuberculosis, COVID-19, Diabetes, Hypertension, High Cholesterol, Obesity, Thyroid Disorders, Vitamin Deficiencies, Anemia, Gastrointestinal disorders, Skin conditions, Infectious diseases (Dengue, Malaria, Typhoid), Neurological conditions, Cardiovascular diseases.

## Contribution Guidelines

1. Dataset Expansion: Add conditions following `Disease,Medicines,Yoga,Diet,Advice` format in `dataset.csv`
2. Voice Enhancement: Improve speech recognition accuracy
3. Product Catalog: Expand medical supplies inventory
4. UI Improvements: Enhance responsive design and accessibility

## Legal & Medical Disclaimer

**CRITICAL NOTICE**: This application is developed solely for educational and demonstration purposes.

### Non-Medical Use Only
- Not a medical diagnosis tool
- Not a treatment recommendation system
- Not a substitute for professional medical advice
- Not intended for emergency medical situations

### Legal Limitations
1. All health information is general educational content only
2. Medication, yoga, and diet suggestions are informational references
3. Users must consult licensed healthcare professionals for any medical condition
4. Developer assumes no liability for health decisions made using this application
5. In case of medical emergency, contact qualified emergency services immediately

### Data Responsibility
- Users are responsible for data stored locally on their devices
- No personal data collection or transmission occurs
- Backup patient data (`patients_data.csv`) recommended

## Support Contact

**Amit Sharma**  
*Artificial Intelligence Student*  
Email: support@yourhealthassistant.com  
Phone: +91 972345670 (Mon-Fri, 9 AM - 6 PM IST)

---

Repository maintained for academic and portfolio demonstration purposes only.
