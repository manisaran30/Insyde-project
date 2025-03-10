import streamlit as st
import numpy as np
import random
import matplotlib.pyplot as plt

# Function to optimize furniture layout
def optimize_furniture(room_size, furniture):
    room_width, room_height = room_size
    new_positions = []
    for item in furniture:
        width, height, _, _ = item
        new_x = random.uniform(0, room_width - width)
        new_y = random.uniform(0, room_height - height)
        new_positions.append([width, height, new_x, new_y])
    return new_positions

# Function to visualize layout
def plot_layout(room_size, furniture):
    fig, ax = plt.subplots()
    ax.set_xlim(0, room_size[0])
    ax.set_ylim(0, room_size[1])
    ax.set_title("Optimized Furniture Layout")
    ax.set_xlabel("Width (m)")
    ax.set_ylabel("Height (m)")
    ax.grid(True)

    for item in furniture:
        width, height, x, y = item
        rect = plt.Rectangle((x, y), width, height, color='blue', alpha=0.5)
        ax.add_patch(rect)

    st.pyplot(fig)

# Streamlit UI
st.title("🛋️ Layout Optimizer")
st.write("Optimize furniture arrangement within a given room size.")

# Room Input
room_width = st.number_input("Room Width (m)", min_value=3, max_value=20, value=6)
room_height = st.number_input("Room Height (m)", min_value=3, max_value=20, value=5)

# Furniture Input
furniture_count = st.slider("Number of Furniture Items", 1, 5, 2)
furniture = []

for i in range(furniture_count):
    col1, col2 = st.columns(2)
    with col1:
        width = st.number_input(f"Width of Item {i+1} (m)", min_value=0.5, max_value=3.0, value=1.0)
        x = st.slider(f"X Position of Item {i+1} (m)", 0.0, room_width - width, 0.0)
    with col2:
        height = st.number_input(f"Height of Item {i+1} (m)", min_value=0.5, max_value=3.0, value=1.0)
        y = st.slider(f"Y Position of Item {i+1} (m)", 0.0, room_height - height, 0.0)
    
    furniture.append([width, height, x, y])

# Run Optimization
if st.button("Optimize Layout"):
    optimized_furniture = optimize_furniture([room_width, room_height], furniture)
    st.success("Layout optimized successfully!")
    plot_layout([room_width, room_height], optimized_furniture)
