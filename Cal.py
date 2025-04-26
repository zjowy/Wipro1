import streamlit as st
import pandas as pd

# Small database for foods and calories per 100 grams
data = {
    "Food": ["White Rice", "Grilled Chicken", "Green Salad", "Whole Wheat Bread", "Grilled Fish"],
    "Calories per 100g": [130, 165, 20, 250, 200]
}

df = pd.DataFrame(data)

st.title("Calories Calculator")

# Select food type
food = st.selectbox("Choose a food:", df["Food"])

# Enter quantity
quantity = st.number_input("Enter the amount (grams):", min_value=0.0, step=10.0)

# Calculate calories
if quantity > 0:
    calories_per_100g = df[df["Food"] == food]["Calories per 100g"].values[0]
    total_calories = (calories_per_100g * quantity) / 100
    st.success(f"Approximate calories: {total_calories:.2f} kcal")

