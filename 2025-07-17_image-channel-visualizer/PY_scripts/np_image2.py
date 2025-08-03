import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO 
import matplotlib.pyplot as plt

# Configure Streamlit page settings
st.set_page_config(page_title="Porsche Image Processor", layout="wide")

# Title and intro
st.title("🚗 Porsche Image - RGB Channel Visualizer & Colormapper")
st.markdown("This app demonstrates RGB channel separation and colormap transformations on a Porsche image using **NumPy**, **Pillow**, and **Matplotlib**.")

# Function to load image from URL with caching
@st.cache_data
def load_image():
    url = "https://content-hub.imgix.net/6H8edXTmr2k2YESRNhr616/9d44e2e239cefb4c0198660f37d823b2/the-20most-20iconic-20porsche-20colours.jpg?w=2064"
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGB")

# Load image
porsche_img = load_image()

# Display original image
st.image(porsche_img, caption="Original Porsche Image", use_container_width=True)

# Convert image to NumPy array
porsche_np = np.array(porsche_img)

# Extract RGB channels
R, G, B = porsche_np[:, :, 0], porsche_np[:, :, 1], porsche_np[:, :, 2]

# Create separate channel images
red_channel = np.zeros_like(porsche_np)
green_channel = np.zeros_like(porsche_np)
blue_channel = np.zeros_like(porsche_np)

red_channel[:, :, 0] = R
green_channel[:, :, 1] = G
blue_channel[:, :, 2] = B

# Display RGB channel images side by side
st.subheader("🔴🟢🔵 RGB Channel Separation")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_channel, caption="Red Channel", use_container_width=True)
with col2:
    st.image(green_channel, caption="Green Channel", use_container_width=True)
with col3:
    st.image(blue_channel, caption="Blue Channel", use_container_width=True)

# Convert to grayscale
porsche_gray = porsche_img.convert("L")
porsche_gray_np = np.array(porsche_gray)

# User selects colormap
st.subheader("🎨 Grayscale Image with Matplotlib Colormap")
colormap = st.selectbox(
    "Choose a Matplotlib colormap:",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

# Plot grayscale with selected colormap
fig, ax = plt.subplots(figsize=(6, 4))
ax.imshow(porsche_gray_np, cmap=colormap)
ax.axis("off")
st.pyplot(fig)
