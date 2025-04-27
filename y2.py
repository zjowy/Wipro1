import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# قائمة للفئات
categories = ["Food", "Housing", "Entertainment", "Transportation", "Utilities", "Others"]

# تخزين البيانات
data = {
    "Date": [],
    "Category": [],
    "Amount": [],
    "Type": []  # نوع الإدخال: "Income" أو "Expense"
}

# دالة لإضافة البيانات
def add_data(date, category, amount, type_of_entry):
    data["Date"].append(date)
    data["Category"].append(category)
    data["Amount"].append(amount)
    data["Type"].append(type_of_entry)

# إضافة بعض البيانات بشكل يدوي (تأكد من إضافة بيانات)
add_data("2025-04-25", "Food", 50, "Expense")
add_data("2025-04-25", "Housing", 1000, "Expense")
add_data("2025-04-25", "Transportation", 100, "Expense")
add_data("2025-04-25", "Income", 2000, "Income")

# عنوان التطبيق
st.title("Personal Finance Tracker")

# إدخال البيانات
with st.form(key="finance_form"):
    date = st.date_input("Enter the Date")
    category = st.selectbox("Select Category", categories)
    amount = st.number_input("Enter Amount", min_value=0.0, step=0.01)
    entry_type = st.selectbox("Type of Entry", ["Income", "Expense"])

    submit_button = st.form_submit_button(label="Add Entry")

    # إذا تم الضغط على زر الإدخال
    if submit_button:
        add_data(date, category, amount, entry_type)
        st.success("Entry added successfully!")

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(data)

# حساب الإيرادات والنفقات
income = df[df["Type"] == "Income"]["Amount"].sum()
expenses = df[df["Type"] == "Expense"]["Amount"].sum()

# حساب الفائض أو العجز
balance = income - expenses

# عرض النتائج
st.write(f"Total Income: ${income}")
st.write(f"Total Expenses: ${expenses}")
st.write(f"Balance: ${balance}")

# رسم بياني للنفقات
expense_data = df[df["Type"] == "Expense"].groupby("Category")["Amount"].sum()

# رسم بياني
st.subheader("Expense Breakdown by Category")
fig, ax = plt.subplots()
expense_data.plot(kind="bar", ax=ax, color='skyblue')
ax.set_title("Expenses by Category")
ax.set_ylabel("Amount")
st.pyplot(fig)

# عرض البيانات كجدول
st.subheader("Transaction History")
st.dataframe(df)