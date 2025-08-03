import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Configure Streamlit page
st.set_page_config(page_title="Image Channel Visualizer - by Mubasshir", layout="wide")

# Title
st.title("🖼️ Personal Image - RGB Channel Visualizer & Colormapper")
st.markdown(
    """
    This app demonstrates:
    - RGB channel separation (Red, Green, Blue)
    - Grayscale transformation
    - Application of various **Matplotlib colormaps**
    
    Built with ❤️ by **Mubasshir Ahmed**
    """
)

# Function to load and resize image
@st.cache_data
def load_and_resize_image(max_width=500):
    path = r"C:\Users\MUBASSHIR\OneDrive\Pictures\media\theogme.jpg"
    img = Image.open(path).convert("RGB")
    img.thumbnail((max_width, max_width))  # Resize image while maintaining aspect ratio
    return img

# Load and resize image
mubasshir_img = load_and_resize_image()

# Display the original image
st.image(mubasshir_img, caption="The OG Mubasshir Ahmed - Unfiltered & Unmatched 🔥", use_container_width=False)

# Convert to NumPy array
mubasshir_np = np.array(mubasshir_img)

# Extract RGB channels
R = mubasshir_np[:, :, 0]
G = mubasshir_np[:, :, 1]
B = mubasshir_np[:, :, 2]

# Create isolated RGB channel images
red_only = np.zeros_like(mubasshir_np)
green_only = np.zeros_like(mubasshir_np)
blue_only = np.zeros_like(mubasshir_np)

red_only[:, :, 0] = R
green_only[:, :, 1] = G
blue_only[:, :, 2] = B

# Display RGB channels
st.subheader("🔍 RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_only, caption="🔴 Red Channel", use_container_width=True)
with col2:
    st.image(green_only, caption="🟢 Green Channel", use_container_width=True)
with col3:
    st.image(blue_only, caption="🔵 Blue Channel", use_container_width=True)

# Convert to grayscale
mubasshir_gray = mubasshir_img.convert("L")
mubasshir_gray_np = np.array(mubasshir_gray)

# User-selected colormap
st.subheader("🎨 Grayscale Image with Custom Colormap")
colormap = st.selectbox(
    "Select a Matplotlib colormap:",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

# Plot grayscale with selected colormap
fig, ax = plt.subplots(figsize=(6, 4))
ax.imshow(mubasshir_gray_np, cmap=colormap)
ax.axis("off")
st.pyplot(fig)
