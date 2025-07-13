import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------------------------------
# 💡 Project: Seaborn Visualization Dashboard
# 📊 Dataset: Tips (built-in seaborn dataset)
# 🧑‍💻 Prepared by: Mubasshir Ahmed
# ------------------------------------------

# Apply seaborn theme for consistent visuals
sns.set_theme(style="whitegrid")

# Load the 'tips' dataset
tips_data = sns.load_dataset("tips")

# Streamlit App Title and Description
st.title("🧾 Tips Data Visualization App - Seaborn Bootcamp")
st.markdown("This interactive app showcases various **Seaborn plots** built on the classic `tips` dataset. Select a plot from the dropdown to visualize restaurant tipping trends.")

# ------------------------------------------
# 🧩 Plotting Functions (one for each plot)
# ------------------------------------------

def plot_scatter(axis):
    """Scatter plot: Total Bill vs Tip"""
    sns.scatterplot(data=tips_data, x="total_bill", y="tip", hue="time", size="size", palette="deep", ax=axis)
    axis.set_title("Scatter Plot: Total Bill vs Tip (Grouped by Time & Party Size)")

def plot_line(axis):
    """Line plot: Total Bill by Party Size & Gender"""
    sns.lineplot(data=tips_data, x="size", y="total_bill", hue="sex", marker="o", ax=axis)
    axis.set_title("Line Plot: Total Bill by Party Size & Gender")

def plot_bar(axis):
    """Bar plot: Average Total Bill by Day & Gender"""
    sns.barplot(data=tips_data, x="day", y="total_bill", hue="sex", palette="muted", ax=axis)
    axis.set_title("Bar Plot: Average Total Bill by Day & Gender")

def plot_box(axis):
    """Box plot: Tip Distribution by Day & Smoking Status"""
    sns.boxplot(data=tips_data, x="day", y="tip", hue="smoker", palette="Set2", ax=axis)
    axis.set_title("Box Plot: Tip Amount by Day & Smoker Status")

def plot_violin(axis):
    """Violin plot: Total Bill Distribution by Day & Time"""
    sns.violinplot(data=tips_data, x="day", y="total_bill", hue="time", split=True, palette="pastel", ax=axis)
    axis.set_title("Violin Plot: Total Bill by Day & Time")

def plot_count(axis):
    """Count plot: Number of Customers by Day & Smoker Status"""
    sns.countplot(data=tips_data, x="day", hue="smoker", palette="dark", ax=axis)
    axis.set_title("Count Plot: Number of Customers by Day & Smoker Status")

def plot_regression(axis):
    """Regression plot: Total Bill vs Tip with Trend Line"""
    sns.regplot(data=tips_data, x="total_bill", y="tip", scatter_kws={"s": 50}, line_kws={"color": "red"}, ax=axis)
    axis.set_title("Regression Plot: Total Bill vs Tip")

def plot_histogram(axis):
    """Histogram with KDE: Total Bill Distribution"""
    sns.histplot(data=tips_data, x="total_bill", bins=20, kde=True, color="blue", ax=axis)
    axis.set_title("Histogram: Total Bill Distribution with KDE")

def plot_strip(axis):
    """Strip plot: Tips by Day & Gender"""
    sns.stripplot(data=tips_data, x="day", y="tip", hue="sex", jitter=True, palette="Set1", ax=axis)
    axis.set_title("Strip Plot: Tips by Day & Gender")

def plot_kde(axis):
    """KDE plot: Total Bill Density by Gender"""
    sns.kdeplot(data=tips_data, x="total_bill", hue="sex", fill=True, palette="tab10", ax=axis)
    axis.set_title("KDE Plot: Total Bill Density by Gender")

# Dictionary to map plot names to functions
plot_options = {
    "Scatter Plot": plot_scatter,
    "Line Plot": plot_line,
    "Bar Plot": plot_bar,
    "Box Plot": plot_box,
    "Violin Plot": plot_violin,
    "Count Plot": plot_count,
    "Regression Plot": plot_regression,
    "Histogram Plot": plot_histogram,
    "Strip Plot": plot_strip,
    "KDE Plot": plot_kde
}

# ------------------------------------------
# 🎛️ Streamlit UI: Select and Render Plot
# ------------------------------------------

selected_plot = st.selectbox("Select a plot to visualize:", list(plot_options.keys()))

# Display selected plot
st.subheader(f"📈 {selected_plot}")
fig, axis = plt.subplots(figsize=(6, 4.5))
plot_function = plot_options[selected_plot]
plot_function(axis)
st.pyplot(fig)
plt.close(fig)

# Footer (optional)
st.markdown("---")
st.caption("Made with ❤️ using Seaborn & Streamlit | By Mubasshir Ahmed")
