<div align="center">

# 🌾 Crop Recommendation System

### *AI-Powered Smart Farming for Better Crop Selection*

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render&logoColor=white)](https://render.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**[🚀 Live Demo](https://crop-recommendation-system.onrender.com)** | **[📊 Dataset](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset)**

</div>

---

## 📑 Table of Contents

- [Demo](#-demo)
- [Overview](#-overview)
- [Motivation](#-motivation)
- [Technical Aspect](#-technical-aspect)
- [Installation](#-installation)
- [Run](#-run)
- [Deployment on Render](#-deployment-on-render)
- [Directory Tree](#-directory-tree)
- [To Do](#-to-do)
- [Bug / Feature Request](#-bug--feature-request)
- [Technologies Used](#-technologies-used)
- [Team](#-team)
- [License](#-license)
- [Credits](#-credits)
- [Badges](#-badges)

---

## 🎥 Demo

🔗 **Live Application:** [https://crop-recommendation-system.onrender.com]([https://crop-recommendation-system.onrender.com](https://crop-recommenderr.onrender.com/))

<div align="center">
<img width="1297" height="701" alt="Image" src="https://github.com/user-attachments/assets/8c873884-abed-434b-9442-4b9674ed2d92" />
  <p><em>Screenshot of the Crop Recommendation System in action</em></p>
</div>

---

## 🌾 Overview

The **Crop Recommendation System** is an intelligent machine learning application designed to help farmers and agricultural professionals make data-driven decisions about crop selection. By analyzing soil and environmental parameters, the system recommends the most suitable crops to cultivate, maximizing yield potential and resource efficiency.

### 🎯 Key Features

- **Smart Predictions**: Recommends optimal crops based on soil and climate conditions
- **7 Input Parameters**: 
  - Nitrogen (N) content
  - Phosphorus (P) content
  - Potassium (K) content
  - Temperature (°C)
  - Humidity (%)
  - pH value
  - Rainfall (mm)
- **22 Crop Varieties**: Supports recommendations for rice, wheat, maize, cotton, and 18 other crops
- **User-Friendly Interface**: Built with Streamlit for seamless interaction
- **High Accuracy**: Achieves 99.5% prediction accuracy using Random Forest algorithm

### 📊 Dataset

The model is trained on the **[Kaggle Crop Recommendation Dataset](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset)**, which contains 2,200 samples of agricultural data with soil nutrients, climate conditions, and corresponding optimal crops.

---

## 💡 Motivation

Agriculture is the backbone of many economies, yet farmers often struggle with selecting the right crops for their specific soil and climate conditions. Poor crop selection can lead to:

- 📉 Reduced yields and income
- 💰 Wasted resources (water, fertilizers, labor)
- 🌍 Environmental degradation
- 📊 Economic instability for farming communities

**The Solution**: By leveraging machine learning and data science, we can analyze historical agricultural data to identify patterns and provide accurate crop recommendations tailored to specific environmental conditions. This system empowers farmers to:

✅ Make informed decisions  
✅ Optimize resource utilization  
✅ Increase crop yields  
✅ Promote sustainable farming practices  

This project demonstrates how AI and data science can transform traditional agriculture into smart, data-driven farming.

---

## ⚙️ Technical Aspect

### 🤖 Machine Learning Model

- **Algorithm**: Random Forest Classifier
- **Accuracy**: **99.5%** on test data
- **Features**: 7 input parameters (N, P, K, Temperature, Humidity, pH, Rainfall)
- **Target**: 22 crop categories
- **Preprocessing**: StandardScaler for feature normalization, LabelEncoder for target encoding

### 🛠️ Technology Stack

- **Programming Language**: Python 3.8+
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-Learn
- **Visualization**: Matplotlib, Seaborn
- **Web Framework**: Streamlit
- **Deployment**: Render Cloud Platform
- **Development**: Jupyter Notebook, PyCharm IDE

### 📈 Model Performance

The Random Forest Classifier was chosen after comparing multiple algorithms. It achieved:
- **Training Accuracy**: 99.8%
- **Test Accuracy**: 99.5%
- **Cross-Validation Score**: 99.4%

---

## 🧰 Installation

Follow these steps to set up the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/krishna-gurjar/crop-recommendation-system.git
cd crop-recommendation-system
```

### 2️⃣ Create a Virtual Environment

**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run

Once the installation is complete, launch the Streamlit application:
```bash
streamlit run app/app.py
```

**Expected Output:**
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.1.100:8501
```

Open the **Local URL** in your browser to interact with the application! 🎉

---

## ☁️ Deployment on Render

This application is deployed on **Render**, a modern cloud platform for hosting web applications.

### 🚀 Deployment Steps

1. **Create a Render Account**: Sign up at [render.com](https://render.com)

2. **Connect GitHub Repository**: Link your GitHub account and select this repository

3. **Configure Build Settings**:
   - **Build Command**: 
```bash
     pip install -r requirements.txt
```
   - **Start Command**: 
```bash
     streamlit run app/app.py --server.port=$PORT --server.address=0.0.0.0
```

4. **Set Environment Variables** (if needed):
   - Add any API keys or configuration variables

5. **Deploy**: Click "Create Web Service" and Render will automatically deploy your app

<div align="center">
<img width="1470" height="956" alt="Image" src="https://github.com/user-attachments/assets/71760028-4b44-43d1-ab0f-757a5d1a5196" />
  <p><em>Render deployment dashboard</em></p>
</div>

### 🔄 Automatic Redeployment

Render automatically redeploys your application whenever you push changes to the main branch on GitHub. No manual intervention required! 🎯

---

## 🌲 Directory Tree
```
Crop_recommender/
├── app/
│   └── app.py                    # Streamlit web application
├── models/
│   ├── rf_model.pkl              # Trained Random Forest model
│   ├── scaler.pkl                # Feature scaler
│   └── label_encoder.pkl         # Target label encoder
├── notebooks/
│   └── 01_EDA_and_modeling.ipynb # Exploratory Data Analysis and model training
├── screenshots/
│   ├── app_screenshot.png        # Application screenshot
│   └── render_dashboard.png      # Render deployment screenshot
├── data/
│   └── Crop_recommendation.csv   # Dataset
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore file
├── LICENSE                       # MIT License
└── README.md                     # Project documentation
```

---

## 📋 To Do

- [ ] Add more crop varieties to the recommendation system
- [ ] Implement crop rotation suggestions
- [ ] Add multilingual support (Hindi, Spanish, French)
- [ ] Create a mobile-responsive progressive web app (PWA)
- [ ] Integrate real-time weather API for automatic climate data
- [ ] Add soil testing guide for farmers
- [ ] Implement user authentication and history tracking
- [ ] Create data visualization dashboard for crop trends
- [ ] Add fertilizer recommendation feature
- [ ] Develop REST API for third-party integrations

---

## 🐞 Bug / Feature Request

If you find a bug or have a feature request, please open an issue on GitHub:

👉 **[Create an Issue](https://github.com/krishna-gurjar/crop-recommendation-system/issues)**

**To report a bug:**
1. Navigate to the Issues tab
2. Click "New Issue"
3. Provide a clear description of the bug
4. Include steps to reproduce
5. Add screenshots if applicable

**To request a feature:**
1. Open a new issue with the "enhancement" label
2. Describe the feature and its benefits
3. Explain your use case

I appreciate your feedback and contributions! 🙏

---

## 🧠 Technologies Used

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)

</div>

### 📊 Technology Categories

| Category | Tools |
|----------|-------|
| **Programming** | Python 3.8+ |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-Learn (Random Forest Classifier) |
| **Visualization** | Matplotlib, Seaborn |
| **Web Framework** | Streamlit |
| **Deployment** | Render Cloud Platform |
| **Development Environment** | Jupyter Notebook, PyCharm IDE |
| **Version Control** | Git, GitHub |

---

## 👨‍💻 Team

<div align="center">

### **Krishna Gurjar**

*"Turning data into decisions for smarter farming."*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/krishna-gurjar)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/krishna-gurjar)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:krishna@gmail.com)

</div>

---

## ⚖️ License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
```
Copyright (c) 2024 Krishna Gurjar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

📄 Full license text available in the [LICENSE](LICENSE) file.

---

## 🙌 Credits

This project was made possible by the following resources and technologies:

| Resource | Description | Link |
|----------|-------------|------|
| **Kaggle** | Crop Recommendation Dataset | [Visit](https://www.kaggle.com/atharvaingle/crop-recommendation-dataset) |
| **Scikit-Learn** | Machine Learning library for model training | [Visit](https://scikit-learn.org/) |
| **Streamlit** | Web framework for building the application | [Visit](https://streamlit.io/) |
| **Render** | Cloud platform for deployment | [Visit](https://render.com/) |
| **Python** | Core programming language | [Visit](https://www.python.org/) |
| **Ella** | AI tutor for Data Science guidance | [Visit](https://ella.ai/) |

Special thanks to the open-source community for their invaluable tools and resources! 🙏

---

## 🏆 Badges

<div align="center">

![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f?style=for-the-badge&logo=python)
![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![PyCharm](https://img.shields.io/badge/IDE-PyCharm-000000?style=for-the-badge&logo=pycharm)

</div>

---

<div align="center">

### ⭐ If you like this project, give it a star on GitHub!

**Happy Farming! 🌾🚜**

</div>
