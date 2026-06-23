import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------
# Streamlit Page Configuration
# ------------------------------------------------------
st.set_page_config(page_title="🎓 Student Performance Dashboard", layout="wide")

st.title("🎓 Student Performance Dashboard")

# ------------------------------------------------------
# Sidebar Navigation
# ------------------------------------------------------
st.sidebar.title("📂 Navigation")
section = st.sidebar.radio(
    "Go to:",
    ["Upload Data", "Data Overview", "Statistics & Insights", "Visualizations"]
)

# ------------------------------------------------------
# File Upload
# ------------------------------------------------------
uploaded_file = st.sidebar.file_uploader("Upload Students CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Calculate Total and Average Marks
    df['Total Marks'] = df[['Math', 'Science', 'English', 'History', 'Computer']].sum(axis=1)
    df['Average'] = df[['Math', 'Science', 'English', 'History', 'Computer']].mean(axis=1)

    # ======================================================
    # 1️⃣ UPLOAD DATA SECTION
    # ======================================================
    if section == "Upload Data":
        st.subheader("📋 Uploaded Dataset Preview")
        st.dataframe(df.head(10))
        st.success("✅ File successfully loaded and processed!")

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Updated CSV",
            data=csv,
            file_name='Output.csv',
            mime='text/csv'
        )

    # ======================================================
    # 2️⃣ DATA OVERVIEW SECTION
    # ======================================================
    elif section == "Data Overview":
        st.subheader("🔍 Data Overview")

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Rows", df.shape[0])
        col2.metric("Total Columns", df.shape[1])
        col3.metric("Missing Values", df.isnull().sum().sum())

        st.markdown("### Data Types")
        st.dataframe(df.dtypes.rename("Data Type"))

        st.markdown("### Missing Values per Column")
        st.bar_chart(df.isnull().sum())

        st.markdown("### Summary Statistics")
        st.dataframe(df.describe())

    # ======================================================
    # 3️⃣ STATISTICS & INSIGHTS SECTION
    # ======================================================
    elif section == "Statistics & Insights":
        st.subheader("📈 Key Statistics & Insights")

        total_marks_all = df[['Math', 'Science', 'English', 'History', 'Computer']].sum(axis=1)
        min_marks = np.min(total_marks_all)
        max_marks = np.max(total_marks_all)
        avg_marks = np.mean(total_marks_all)
        std_marks = np.std(total_marks_all)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Min Marks", f"{min_marks:.2f}")
        col2.metric("Max Marks", f"{max_marks:.2f}")
        col3.metric("Average Marks", f"{avg_marks:.2f}")
        col4.metric("Std. Deviation", f"{std_marks:.2f}")

        # Top 3 students
        st.markdown("### 🏅 Top 3 Students by Average Marks")
        top_3 = df.sort_values(by='Average', ascending=False).head(3)
        st.dataframe(top_3[['Name', 'Average', 'Total Marks']])

        # Subject averages
        high_avg = df[['Math', 'Science', 'English', 'History', 'Computer']].mean()
        high_avg_sub = high_avg.idxmax()
        st.success(f"🌟 Subject with Highest Average: **{high_avg_sub}**")

        st.markdown("### 📚 Average Marks per Subject")
        st.bar_chart(high_avg)

    # ======================================================
    # 4️⃣ VISUALIZATION SECTION
    # ======================================================
    elif section == "Visualizations":
        st.subheader("📊 Visual Analysis")

        students = df['Name'].to_numpy()
        total_marks = df['Total Marks'].to_numpy()
        subjects = ['Math', 'Science', 'English', 'History', 'Computer']
        subject_avgs = df[subjects].mean()
        marks = df['Math'].to_numpy()

        fig, ax = plt.subplots(2, 2, figsize=(12, 8))

        # Total Marks Bar Chart
        ax[0, 0].bar(students, total_marks, color='orange', label='Students Marks')
        ax[0, 0].set_title("Total Marks")
        ax[0, 0].legend()
        ax[0, 0].grid(True)

        # Top 3 Students' Scores
        top_3 = df.sort_values(by='Average', ascending=False).head(3)
        for i, row in top_3.iterrows():
            ax[0, 1].plot(subjects, row[subjects], marker='o', label=row['Name'])
        ax[0, 1].set_title("Scores of Top 3 Students")
        ax[0, 1].legend()
        ax[0, 1].grid(True)

        # Average per Subject Pie Chart
        ax[1, 0].pie(subject_avgs, labels=subjects, autopct='%1.1f%%',
                     colors=['red', 'yellow', 'skyblue', 'orange', 'green'])
        ax[1, 0].set_title("Average per Subject")

        # Math Score Distribution
        ax[1, 1].hist(marks, bins=5, color='pink', edgecolor='black')
        ax[1, 1].set_xlabel('Scores Range')
        ax[1, 1].set_ylabel('Number of Students')
        ax[1, 1].set_title('Math Score Distribution')

        st.pyplot(fig)

else:
    st.info("👈 Please upload a `Students.csv` file from the sidebar to begin.")
