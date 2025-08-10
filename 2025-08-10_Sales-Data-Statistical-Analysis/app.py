# ---------------------------------------------------------
# Sales Data Analysis App
# Developed by: Mubasshir Ahmed (FSDS Project)
# ---------------------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="Sales Data Analysis", layout="wide")

# Professional Header
st.markdown("<h1 style='text-align: center; color: #FF6B6B;'>📊 Sales Data Analysis Dashboard</h1>", unsafe_allow_html=True)
st.markdown("""
<p style='text-align: right; font-size: 1rem; font-style: italic; color: #888; margin-top: -10px;'>
    ~ by <span style='color:#FF6B6B; font-weight:600;'>Mubasshir Ahmed</span>
</p>
""", unsafe_allow_html=True)
st.write("Analyze sales data using descriptive and inferential statistics with interactive visualizations.")

# ---------------------------
# Helper Functions
# ---------------------------
@st.cache_data
def generate_sample_data():
    np.random.seed(42)
    data = {
        'product_id': range(1, 21),
        'product_name': [f'Product {i}' for i in range(1, 21)],
        'category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports'], 20),
        'units_sold': np.random.poisson(lam=20, size=20),
        'sale_date': pd.date_range(start='2023-01-01', periods=20, freq='D')
    }
    return pd.DataFrame(data)

@st.cache_data
def load_csv(file):
    return pd.read_csv(file)

def calculate_descriptive_stats(df):
    desc_stats = df['units_sold'].describe()
    mean_val = df['units_sold'].mean()
    median_val = df['units_sold'].median()
    mode_val = df['units_sold'].mode().iloc[0] if not df['units_sold'].mode().empty else np.nan
    return desc_stats, mean_val, median_val, mode_val

def calculate_inferential_stats(df, confidence_level, test_mean):
    n = len(df['units_sold'])
    mean_val = df['units_sold'].mean()
    se = stats.sem(df['units_sold'], ddof=1)
    t_crit = stats.t.ppf((1 + confidence_level) / 2, n - 1)
    margin_of_error = t_crit * se
    ci_lower, ci_upper = mean_val - margin_of_error, mean_val + margin_of_error
    
    t_stat, p_val = stats.ttest_1samp(df['units_sold'], test_mean)
    return (ci_lower, ci_upper), (t_stat, p_val)

def plot_histogram(df, mean_val, median_val, mode_val):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df['units_sold'], bins=10, kde=True, ax=ax)
    ax.axvline(mean_val, color='red', linestyle='--', label=f'Mean: {mean_val:.2f}')
    ax.axvline(median_val, color='blue', linestyle='--', label=f'Median: {median_val:.2f}')
    ax.axvline(mode_val, color='green', linestyle='--', label=f'Mode: {mode_val:.2f}')
    ax.set_title('Distribution of Units Sold')
    ax.set_xlabel('Units Sold')
    ax.set_ylabel('Frequency')
    ax.legend()
    st.pyplot(fig)
    plt.close(fig)

def plot_boxplot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='category', y='units_sold', data=df, ax=ax)
    ax.set_title('Units Sold by Category')
    ax.set_xlabel('Category')
    ax.set_ylabel('Units Sold')
    st.pyplot(fig)
    plt.close(fig)

def plot_barplot(df):
    category_stats = df.groupby('category')['units_sold'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='category', y='units_sold', data=category_stats, ax=ax)
    ax.set_title('Total Units Sold by Category')
    ax.set_xlabel('Category')
    ax.set_ylabel('Total Units Sold')
    st.pyplot(fig)
    plt.close(fig)

def download_df(df):
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False)
    return csv_buffer.getvalue()

# ---------------------------
# Sidebar Controls
# ---------------------------
st.sidebar.header("⚙️ Controls")
upload_file = st.sidebar.file_uploader("Upload your sales CSV", type=['csv'])
confidence_level = st.sidebar.slider("Confidence Level", 0.80, 0.99, 0.95, 0.01)
test_mean = st.sidebar.number_input("Hypothesized Mean (t-test)", value=20.0)
filter_category = st.sidebar.multiselect("Filter by Category", options=['Electronics', 'Clothing', 'Home', 'Sports'])

# ---------------------------
# Load Data
# ---------------------------
if upload_file is not None:
    df_sales = load_csv(upload_file)
else:
    df_sales = generate_sample_data()

if filter_category:
    df_sales = df_sales[df_sales['category'].isin(filter_category)]

st.subheader("📂 Sales Data")
st.dataframe(df_sales)
st.download_button("Download Current Data as CSV", data=download_df(df_sales), file_name="sales_data.csv", mime="text/csv")

# ---------------------------
# Descriptive Statistics
# ---------------------------
st.subheader("📈 Descriptive Statistics")
desc_stats, mean_val, median_val, mode_val = calculate_descriptive_stats(df_sales)
st.dataframe(desc_stats)
col1, col2, col3 = st.columns(3)
col1.metric("Mean", f"{mean_val:.2f}")
col2.metric("Median", f"{median_val:.2f}")
col3.metric("Mode", f"{mode_val:.2f}")

# ---------------------------
# Inferential Statistics
# ---------------------------
st.subheader("📊 Inferential Statistics")
ci, ttest = calculate_inferential_stats(df_sales, confidence_level, test_mean)
st.write(f"**{confidence_level*100:.0f}% Confidence Interval:** ({ci[0]:.2f}, {ci[1]:.2f})")
st.write(f"**t-test Statistic:** {ttest[0]:.4f}, **p-value:** {ttest[1]:.4f}")

if ttest[1] < 0.05:
    st.success("Reject the null hypothesis: Mean is significantly different.")
else:
    st.info("Fail to reject the null hypothesis: Mean is not significantly different.")

# ---------------------------
# Visualizations
# ---------------------------
st.subheader("📉 Visualizations")
plot_histogram(df_sales, mean_val, median_val, mode_val)
plot_boxplot(df_sales)
plot_barplot(df_sales)

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); border-radius: 15px; margin: 2rem 0;">
    <h3 style="color: #FF6B6B; margin-bottom: 1rem;">👨‍💻 About the Developer</h3>
    <p style="color: #FAFAFA; font-size: 1.1rem; margin-bottom: 1.5rem;">
        <strong>Mubasshir Ahmed</strong><br>
        🧠 Data & AI Enthusiast | Python • SQL • ML • GenAI • BI Tools<br>
        🎓 BCA Graduate | Ex-Full Stack Dev | Est. 2004 | Proud Memon 🧬 | 📚 Lifelong Learner
    </p>
    <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
        <a href="https://github.com/mubasshirahmed-3712" target="_blank" style="text-decoration: none;">
            <button style="background: linear-gradient(135deg, #181717 0%, #333 100%); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">
                🐙 GitHub
            </button>
        </a>
        <a href="https://www.linkedin.com/in/mubasshir3712/" target="_blank" style="text-decoration: none;">
            <button style="background: linear-gradient(135deg, #0077B5 0%, #005885 100%); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">
                💼 LinkedIn
            </button>
        </a>
        <a href="https://www.instagram.com/badhshah._09" target="_blank" style="text-decoration: none;">
            <button style="background: linear-gradient(135deg, #E4405F 0%, #C13584 100%); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">
                📸 Instagram
            </button>
        </a>
        <a href="https://mubasshirsportfolio.vercel.app" target="_blank" style="text-decoration: none;">
            <button style="background: linear-gradient(135deg, #FF6B6B 0%, #FF5252 100%); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">
                🌐 Portfolio
            </button>
        </a>
    </div>
    <p style="color: #888; margin-top: 1.5rem; font-size: 0.9rem;">
        Made with ❤️ by Mubasshir Ahmed for the Data Science Community
    </p>
</div>
""", unsafe_allow_html=True)
