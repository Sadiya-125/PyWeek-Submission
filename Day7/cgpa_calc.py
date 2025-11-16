import streamlit as st
st.title("CGPA Calculater")
st.latex(r""" \text{CGPA} = \frac{\sum (\text{Credit} \times \text{Grade Point})}{\sum (\text{Credits})}""")
import pandas as pd
grade_table = {
    'Marks': ['91-100','81-90','71-80','61-70','51-60','41-50','0-40'],
    'Grade': ['S','A','B','C','D','E','F'],
    'Points':['10','9','8','7','6','5','0']
}
df = pd.DataFrame(grade_table)
st.write("Grade Table:")
st.table(df)
mode = st.sidebar.radio(
    "Choose Mode:",
    ["Full CGPA Calculator (All Semesters)", "Add Current Semester to Previous CGPA"]
)
  
if mode == "Full CGPA Calculator (All Semesters)":
    st.header("Enter Grades and Credits for All Semesters")

    num_semesters = st.number_input("Enter total number of semesters", min_value=1, step=1)

    semesters = []
    grade_points = []
    credits = []

    for sem in range(1, int(num_semesters) + 1):
        st.subheader(f"Semester {sem}")
        num_subjects = st.number_input(f"Number of subjects in Semester {sem}", min_value=1, step=1, key=f"subs_{sem}")

        sem_grade_points = []
        sem_credits = []

        for i in range(1, int(num_subjects) + 1):
            col1, col2 = st.columns(2)
            with col1:
                gp = st.number_input(f"Grade Point for Subject {i} (Sem {sem})", min_value=0, max_value=10, step=1, key=f"gp_{sem}_{i}")
            with col2:
                cr = st.number_input(f"Credits for Subject {i} (Sem {sem})", min_value=0.0, step=0.5, key=f"cr_{sem}_{i}")
            sem_grade_points.append(gp)
            sem_credits.append(cr)

        
        
            valid_pairs = [(g, c) for g, c in zip(sem_grade_points, sem_credits) if c > 0]

            if valid_pairs:
                sem_sgpa = sum(g * c for g, c in valid_pairs) / sum(c for _, c in valid_pairs)
            else:
                sem_sgpa = 0

        st.success(f"SGPA for Semester {sem}: {sem_sgpa:.2f}")

        semesters.append(f"Semester {sem}")
        grade_points.extend(sem_grade_points)
        credits.extend(sem_credits)
    if st.button("Calculate Overall CGPA"):
        total_credits = sum(credits)
        cgpa = sum([g * c for g, c in zip(grade_points, credits)]) / total_credits
        st.subheader(f" Your Overall CGPA is: {cgpa:.2f}")
else:
    st.header("Add Current Semester to Previous CGPA")

    prev_cgpa = st.number_input("Enter your Previous CGPA", min_value=0.0, max_value=10.0, step=0.01)
    prev_credits = st.number_input("Enter Total Credits till Previous Semester", min_value=0, step=1)

    st.subheader("Enter Current Semester Details")
    num_subjects = st.number_input("Number of subjects in current semester", min_value=1, step=1)

    grade_points = []
    credits = []

    for i in range(1, int(num_subjects) + 1):
        col1, col2 = st.columns(2)
        with col1:
            gp = st.number_input(f"Grade Point for Subject {i}", min_value=0, max_value=10, step=1, key=f"gp_{i}")
        with col2:
            cr = st.number_input(f"Credits for Subject {i}", min_value=0.0, step=0.5, key=f"cr_{i}")
        grade_points.append(gp)
        credits.append(cr)

    if st.button("Calculate Updated CGPA"):
        current_sem_gpa = sum([g * c for g, c in zip(grade_points, credits)]) / sum(credits)
        total_weighted = (prev_cgpa * prev_credits) + (current_sem_gpa * sum(credits))
        new_cgpa = total_weighted / (prev_credits + sum(credits))

        st.success(f"Current Semester GPA: {current_sem_gpa:.2f}")
        st.subheader(f" Updated CGPA: {new_cgpa:.2f}")
st.audio_input("Record")
