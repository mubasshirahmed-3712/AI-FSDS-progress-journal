# 🌟 seabornXstreamlit-visualizer

An interactive data visualization app built with **Seaborn** and deployed using **Streamlit**.  
This project showcases insightful patterns in restaurant tipping behavior using the classic `tips` dataset.

> 📌 Developed as part of a professional bootcamp under the guidance of *Kodigit*, this project demonstrates practical data visualization and dashboarding skills expected in real-world data roles.

---

## 📸 App Previews

| Streamlit App UI | Example Plot |
|------------------|--------------|
| ![UI Screenshot](assets/ui-overview.png) | ![Bar Plot](assets/barplot-example.png) |

---

## 📁 Project Structure

```
seabornXstreamlit-visualizer/
├── app/
│   └── sns_app_cleaned.py          # Streamlit dashboard
├── notebooks/
│   └── Seaborn_Tips_Data_Visualization.ipynb  # Jupyter EDA
├── assets/
│   └── ui-overview.png             # Screenshots (for README)
│   └── barplot-example.png
├── requirements.txt                # Python dependencies
└── README.md
```

---

## 🔍 About the Project

This project explores various visualizations on the `tips` dataset using **Seaborn** and displays them interactively using **Streamlit**. It allows users to analyze how tip amounts relate to factors like:

- Total bill amount
- Time of day (Lunch/Dinner)
- Day of week
- Gender
- Smoking status
- Party size

It is structured to reflect **real-time industry standards**, including:
- Modular and documented code
- Interactive UI with plot selection
- Clear and consistent chart titles, labels, and themes
- Deployment-ready setup with `requirements.txt`

---

## 🚀 Features

- 📊 **10+ Seaborn Visualizations**: Scatter, Bar, Violin, Box, KDE, and more
- 🎛️ **Dropdown-based Plot Explorer** in Streamlit
- 📁 **Well-organized Project Folder** (Modular, scalable)
- ✍️ **Code with Comments & Docstrings** for readability
- 📸 **Visual Mockups** for presentation & portfolio

---

## 📈 Visualizations Included

- Scatter Plot
- Line Plot
- Bar Plot
- Box Plot
- Violin Plot
- Count Plot
- Regression Plot
- Histogram (with KDE)
- Strip Plot
- KDE Plot

---

## 🧠 Skills Demonstrated

- Python Visualization with Seaborn
- Interactive Dashboarding using Streamlit
- Functional Programming & Modular Code
- Real-time Coding Best Practices
- GitHub Project Documentation

---

## 🗃 Dataset

This project uses the built-in [`tips`](https://github.com/mwaskom/seaborn-data) dataset provided by Seaborn. It contains information about:

| Feature      | Description                                |
|--------------|--------------------------------------------|
| `total_bill` | Total bill amount (USD)                    |
| `tip`        | Tip given by the customer (USD)            |
| `sex`        | Gender of the customer                     |
| `smoker`     | Whether the customer was a smoker          |
| `day`        | Day of the week                            |
| `time`       | Lunch or Dinner                            |
| `size`       | Size of the party                          |

---

## ⚙️ How to Run Locally

### 📦 Step 1: Clone the Repository
```bash
git clone https://github.com/mubasshirahmed-3712/seabornXstreamlit-visualizer.git
cd seabornXstreamlit-visualizer
```

### 📦 Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### 🚀 Step 3: Run the Streamlit App
```bash
streamlit run app/sns_app_cleaned.py
```

---

## 🤝 Acknowledgements

- Guided by **Kodigit**
- Powered by **Seaborn**, **Matplotlib**, and **Streamlit**
- Developed with passion by **Mubasshir Ahmed**

---

## 📬 Contact

**Mubasshir Ahmed**  
Aspiring Data Scientist | FSDS Bootcamp Trainee  
🔗 [LinkedIn](https://www.linkedin.com/in/your-profile) *(update if needed)*

---

