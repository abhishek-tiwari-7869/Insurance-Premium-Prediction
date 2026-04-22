<h1 align="center"> Insurance Premium Prediction</h1>

<p align="center">
Machine Learning Web App using Streamlit <br>
Developed by <b>Abhishek Tiwari</b>
</p>

---

 Project Overview
This project predicts the **insurance premium cost** based on a person's health conditions and lifestyle factors using Machine Learning.

It helps insurance companies to:
- Assess customer risk accurately  
- Set fair premium pricing  
- Improve decision-making  

---

 Objective
To build a machine learning model that predicts insurance premiums using health and medical data.

---

 Tech Stack
- Python 🐍  
- Pandas & NumPy  
- Scikit-learn  
- Streamlit  

---

 Features Used
- Age  
- Diabetes  
- Blood Pressure  
- Transplant History  
- Chronic Disease  
- Height & Weight  
- BMI (calculated)  
- Allergies  
- Cancer History  
- Number of Surgeries  
- Risk Score  

---

Model Performance
- RMSE: **3494**  
- R² Score: **0.71**  

 Model explains around **71% variance**, which indicates good prediction capability.

---


---

 How It Works
1. User enters health details  
2. BMI & Risk Score are calculated  
3. Model predicts premium  
4. Result is shown instantly  

---

 💻 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
