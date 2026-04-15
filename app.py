import streamlit as st
import numpy as np
import joblib
import os

# =========================
# Load model
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "../model", "rf_model.pkl"))

st.title("🎓 Student Performance Prediction")

# st.sidebar.header("📥 Input Data Mahasiswa")

# # =========================
# # DEMOGRAPHIC
# # =========================

marital_options = {
    "Single": 1,
    "Married": 2,
    "Widower": 3,
    "Divorced": 4,
    "Facto Union": 5,
    "Legally Separated": 6
}
# selected_marital = st.sidebar.selectbox("Marital Status", list(marital_options.keys()))
# marital_status = marital_options[selected_marital]

application_options = {
    "1st phase - general contingent": 1,
    "Ordinance No. 612/93": 2,
    "1st phase - special contingent (Azores Island)": 5,
    "Holders of other higher courses": 7,
    "Ordinance No. 854-B/99": 10,
    "International student (bachelor)": 15,
    "1st phase - special contingent (Madeira Island)": 16,
    "2nd phase - general contingent": 17,
    "3rd phase - general contingent": 18,
    "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
    "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
    "Over 23 years old": 39,
    "Transfer": 42,
    "Change of Course": 43,
    "Technological specialization diploma holders": 44,
    "Change of institution/course": 51,
    "Short cycle diploma holders": 53,
    "Change of institution/course (International)": 57
}
# selected_application = st.sidebar.selectbox("Application Mode", list(application_options.keys()))
# application_mode = application_options[selected_application]

# application_order = st.sidebar.slider("Application Order", 0, 9)

course_options = {
    "33 - Biofuel Production Technologies": 33,
    "171 - Animation and Multimedia Design": 171,
    "8014 - Social Service (evening attendance)": 8014,
    "9003 - Agronomy": 9003,
    "9070 - Communication Design": 9070,
    "9085 - Veterinary Nursing": 9085,
    "9119 - Informatics Engineering": 9119,
    "9130 - Equinculture": 9130,
    "9147 - Management": 9147,
    "9238 - Social Service": 9238,
    "9254 - Tourism": 9254,
    "9500 - Nursing": 9500,
    "9556 - Oral Hygiene": 9556,
    "9670 - Advertising and Marketing Management": 9670,
    "9773 - Journalism and Communication": 9773,
    "9853 - Basic Education": 9853,
    "9991 - Management (evening attendance)": 9991
}
# selected_course = st.sidebar.selectbox("Course", list(course_options.keys()))
# course = course_options[selected_course]

attendance_map = {"Daytime": 1, "Evening": 0}
# attendance = attendance_map[st.sidebar.selectbox("Attendance", attendance_map.keys())]

previous_qualification_options = {
    "1 - Secondary education": 1,
    "2 - Higher education - bachelor's degree": 2,
    "3 - Higher education - degree": 3,
    "4 - Higher education - master's": 4,
    "5 - Higher education - doctorate": 5,
    "6 - Frequency of higher education": 6,
    "9 - 12th year of schooling - not completed": 9,
    "10 - 11th year of schooling - not completed": 10,
    "12 - Other - 11th year of schooling": 12,
    "14 - 10th year of schooling": 14,
    "15 - 10th year of schooling - not completed": 15,
    "19 - Basic education 3rd cycle (9th/10th/11th year) or equiv": 19,
    "38 - Basic education 2nd cycle (6th/7th/8th year) or equiv": 38,
    "39 - Technological specialization course": 39,
    "40 - Higher education - degree (1st cycle)": 40,
    "42 - Professional higher technical course": 42,
    "43 - Higher education - master (2nd cycle)": 43
}
# selected_prev_qualification = st.sidebar.selectbox("Previous Qualification", list(previous_qualification_options.keys()))
# previous_qualification = previous_qualification_options[selected_prev_qualification]

# prev_grade = st.sidebar.slider("Previous Qualification Grade", 0, 200)

nationality_options = {
    "1 - Portuguese": 1,
    "2 - German": 2,
    "6 - Spanish": 6,
    "11 - Italian": 11,
    "13 - Dutch": 13,
    "14 - English": 14,
    "17 - Lithuanian": 17,
    "21 - Angolan": 21,
    "22 - Cape Verdean": 22,
    "24 - Guinean": 24,
    "25 - Mozambican": 25,
    "26 - Santomean": 26,
    "32 - Turkish": 32,
    "41 - Brazilian": 41,
    "62 - Romanian": 62,
    "100 - Moldova (Republic of)": 100,
    "101 - Mexican": 101,
    "103 - Ukrainian": 103,
    "105 - Russian": 105,
    "108 - Cuban": 108,
    "109 - Colombian": 109
}
# selected_nationality = st.sidebar.selectbox("Nationality", list(nationality_options.keys()))
# nacionality = nationality_options[selected_nationality]

# mother_qualification = st.sidebar.slider("Mother's Qualification", 0, 50)
# father_qualification = st.sidebar.slider("Father's Qualification", 0, 50)

# mother_occupation = st.sidebar.slider("Mother's Occupation", 0, 200)
# father_occupation = st.sidebar.slider("Father's Occupation", 0, 200)

# admission_grade = st.sidebar.slider("Admission Grade", 0, 200)

displaced_map = {"Yes": 1, "No": 0}
# displaced = displaced_map[st.sidebar.selectbox("Displaced", displaced_map.keys())]

education_special_needs_map = {"Yes": 1, "No": 0}
# education_special_needs = education_special_needs_map[st.sidebar.selectbox("Education Special Needs", education_special_needs_map.keys())]

debtor_map = {"Yes": 1, "No": 0}
# debtor = debtor_map[st.sidebar.selectbox("Debtor", debtor_map.keys())]

tuition_fee_map = {"Yes": 1, "No": 0}
# tuition_fee = tuition_fee_map[st.sidebar.selectbox("Tuition Fees Up to Date", tuition_fee_map.keys())]

gender_map = {"Male": 1, "Female": 0}
# gender = gender_map[st.sidebar.selectbox("Gender", gender_map.keys())]

scholarship_map = {"Yes": 1, "No": 0}
# scholarship = scholarship_map[st.sidebar.selectbox("Scholarship Holder", scholarship_map.keys())]

# age = st.sidebar.number_input("Age at Enrollment", 15, 70)

inter_map = {"Yes": 1, "No": 0}
# international = inter_map[st.sidebar.selectbox("International Student", inter_map.keys())]

# curricular_units_1st_sem_credit = st.sidebar.slider("Curricular Units 1st Sem (Credited)", 0, 20)
# curricular_units_1st_sem_enrolled = st.sidebar.slider("Curricular Units 1st Sem (Enrolled)", 0, 26)
# curricular_units_1st_sem_evaluations = st.sidebar.slider("Curricular Units 1st Sem (Evaluations)", 0, 45)
# curricular_units_1st_sem_approved = st.sidebar.slider("Curricular Units 1st Sem (Approved)", 0, 26)
# curricular_units_1st_sem_grade = st.sidebar.slider("Curricular Units 1st Sem (Grade)", 0, 20)
# curricular_units_1st_sem_without_evaluations = st.sidebar.slider("Curricular Units 1st Sem (without evaluations)", 0, 12)

# curricular_units_2st_sem_credit = st.sidebar.slider("Curricular Units 2st Sem (Credited)", 0, 20)
# curricular_units_2st_sem_enrolled = st.sidebar.slider("Curricular Units 2st Sem (Enrolled)", 0, 26)
# curricular_units_2st_sem_evaluations = st.sidebar.slider("Curricular Units 2st Sem (Evaluations)", 0, 45)
# curricular_units_2st_sem_approved = st.sidebar.slider("Curricular Units 2st Sem (Approved)", 0, 26)
# curricular_units_2st_sem_grade = st.sidebar.slider("Curricular Units 2st Sem (Grade)", 0, 20)
# curricular_units_2st_sem_without_evaluations = st.sidebar.slider("Curricular Units 2st Sem (without evaluations)", 0, 12)

# unemployment = st.sidebar.slider("Unemployment Rate (%)", 0.0, 20.0)
# inflation = st.sidebar.slider("Inflation Rate (%)", 0.0, 20.0)
# gdp = st.sidebar.number_input("GDP", 0.0)

# if st.sidebar.button("🎯 Predict"):

#     input_data = np.array([[
#         marital_status,
#         application_mode,
#         application_order,
#         course,
#         attendance,
#         previous_qualification,
#         prev_grade,
#         nacionality,
#         mother_qualification,
#         father_qualification,
#         mother_occupation,
#         father_occupation,
#         admission_grade,
#         displaced,
#         education_special_needs,
#         debtor,
#         tuition_fee,
#         gender,
#         scholarship,
#         age,
#         international,
#         curricular_units_1st_sem_credit,
#         curricular_units_1st_sem_enrolled,
#         curricular_units_1st_sem_evaluations,
#         curricular_units_1st_sem_approved,
#         curricular_units_1st_sem_grade,
#         curricular_units_1st_sem_without_evaluations,
#         curricular_units_2st_sem_credit,
#         curricular_units_2st_sem_enrolled,
#         curricular_units_2st_sem_evaluations,
#         curricular_units_2st_sem_approved,
#         curricular_units_2st_sem_grade,
#         curricular_units_2st_sem_without_evaluations,
#         unemployment,
#         inflation,
#         gdp
#     ]])

#     result = model.predict(input_data)


st.set_page_config(layout="wide")

st.header("📥 Input Data Mahasiswa")

# =========================
# DEMOGRAPHIC
# =========================
col1, col2 = st.columns(2)

with col1:
    selected_marital = st.selectbox("Marital Status", list(marital_options.keys()))
    marital_status = marital_options[selected_marital]

    selected_application = st.selectbox("Application Mode", list(application_options.keys()))
    application_mode = application_options[selected_application]

    application_order = st.slider("Application Order", 0, 9)

    selected_course = st.selectbox("Course", list(course_options.keys()))
    course = course_options[selected_course]

    attendance = attendance_map[st.selectbox("Attendance", attendance_map.keys())]

    selected_prev_qualification = st.selectbox("Previous Qualification", list(previous_qualification_options.keys()))
    previous_qualification = previous_qualification_options[selected_prev_qualification]

    prev_grade = st.slider("Previous Qualification Grade", 0, 200)

    gender = gender_map[st.selectbox("Gender", gender_map.keys())]
    scholarship = scholarship_map[st.selectbox("Scholarship Holder", scholarship_map.keys())]
    age = st.number_input("Age at Enrollment", 15, 70)
    international = inter_map[st.selectbox("International Student", inter_map.keys())]

with col2:
    selected_nationality = st.selectbox("Nationality", list(nationality_options.keys()))
    nacionality = nationality_options[selected_nationality]

    mother_qualification = st.slider("Mother's Qualification", 0, 50)
    father_qualification = st.slider("Father's Qualification", 0, 50)

    mother_occupation = st.slider("Mother's Occupation", 0, 200)
    father_occupation = st.slider("Father's Occupation", 0, 200)

    admission_grade = st.slider("Admission Grade", 0, 200)

    displaced = displaced_map[st.selectbox("Displaced", displaced_map.keys())]
    education_special_needs = education_special_needs_map[st.selectbox("Education Special Needs", education_special_needs_map.keys())]

    debtor = debtor_map[st.selectbox("Debtor", debtor_map.keys())]
    tuition_fee = tuition_fee_map[st.selectbox("Tuition Fees Up to Date", tuition_fee_map.keys())]

# =========================
# SEMESTER 1
# =========================
st.subheader("Semester 1")
col3, col4 = st.columns(2)

with col3:
    curricular_units_1st_sem_credit = st.slider("1st Sem Credited", 0, 20)
    curricular_units_1st_sem_enrolled = st.slider("1st Sem Enrolled", 0, 26)
    curricular_units_1st_sem_evaluations = st.slider("1st Sem Evaluations", 0, 45)

with col4:
    curricular_units_1st_sem_approved = st.slider("1st Sem Approved", 0, 26)
    curricular_units_1st_sem_grade = st.slider("1st Sem Grade", 0, 20)
    curricular_units_1st_sem_without_evaluations = st.slider("1nd Sem Without Evaluations", 0, 12)

# =========================
# SEMESTER 2
# =========================
st.subheader("Semester 2")

col5, col6 = st.columns(2)

with col5:
    curricular_units_2st_sem_credit = st.slider("2nd Sem Credited", 0, 20)
    curricular_units_2st_sem_enrolled = st.slider("2nd Sem Enrolled", 0, 26)
    curricular_units_2st_sem_evaluations = st.slider("2nd Sem Evaluations", 0, 45)

with col6:
    curricular_units_2st_sem_approved = st.slider("2nd Sem Approved", 0, 26)
    curricular_units_2st_sem_grade = st.slider("2nd Sem Grade", 0, 20)
    curricular_units_2st_sem_without_evaluations = st.slider("2nd Sem Without Evaluations", 0, 12)

# =========================
# ECONOMIC
# =========================
st.subheader("Economic Factors")

unemployment = st.slider("Unemployment Rate (%)", 0.0, 20.0)
inflation = st.slider("Inflation Rate (%)", 0.0, 20.0)
gdp = st.number_input("GDP", 0.0)

# =========================
# PREDICT BUTTON
# =========================
if st.button("🎯 Predict"):

    input_data = np.array([[ 
        marital_status, application_mode, application_order, course, attendance,
        previous_qualification, prev_grade, nacionality, mother_qualification,
        father_qualification, mother_occupation, father_occupation, admission_grade,
        displaced, education_special_needs, debtor, tuition_fee, gender,
        scholarship, age, international,
        curricular_units_1st_sem_credit, curricular_units_1st_sem_enrolled,
        curricular_units_1st_sem_evaluations, curricular_units_1st_sem_approved,
        curricular_units_1st_sem_grade, 
        # curricular_units_1st_sem_without_evaluations,
        curricular_units_2st_sem_credit, curricular_units_2st_sem_enrolled,
        curricular_units_2st_sem_evaluations, curricular_units_2st_sem_approved,
        curricular_units_2st_sem_grade, curricular_units_2st_sem_without_evaluations,
        unemployment, inflation, gdp
    ]])

    result = model.predict(input_data)
    st.write("Prediction:", result)

    st.subheader("📊 Prediction Result")

    # mapping = {
    #     0: "Dropout",
    #     1: "Enrolled",
    #     2: "Graduate"
    # }
    label = result
    # st.write(result)
    if label == "Graduate":
        st.success("🎓 Graduate")
    elif label == "Enrolled":
        st.info("📘 Enrolled")
    else:
        st.error("⚠️ Dropout")

    # if result[0] == "Graduate":
    #     st.success("🎓 Graduate")
    # elif result[0] == "Enrolled":
    #     st.info("📘 Enrolled")
    # else:
    #     st.error("⚠️ Dropout")