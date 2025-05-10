import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_processing, prediction

st.header('Student Dropout Prediction')

data = pd.DataFrame()

marital_status_mapping = {
    "single": 1,
    "married": 2,
    "widower": 3,
    "divorced": 4,
    "facto_union": 5,
    "legally separated": 6 
}

Marital_status = st.selectbox(label="Marital Status", options=list(marital_status_mapping.keys()))
marital_status_value = marital_status_mapping[Marital_status]

data["Marital_status"] = [marital_status_value]

application_mode_mapping = {
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
    "Change of course": 43,
    "Technological specialization diploma holders": 44,
    "Change of institution/course": 51,
    "Short cycle diploma holders": 53,
    "Change of institution/course (International)": 57
}

Application_mode = st.selectbox(label="Application Mode", options=list(application_mode_mapping.keys()))
application_mode_value = application_mode_mapping[Application_mode]

data["Application_mode"] = [application_mode_value]

Application_order = int(st.number_input(label='Application_order', value=0))
data["Application_order"] = Application_order

course_mapping = {
    "Biofuel Production Technologies": 33,
    "Animation and Multimedia Design": 171,
    "Social Service (evening attendance)": 8014,
    "Agronomy": 9003,
    "Communication Design": 9070,
    "Veterinary Nursing": 9085,
    "Informatics Engineering": 9119,
    "Equinculture": 9130,
    "Management": 9147,
    "Social Service": 9238,
    "Tourism": 9254,
    "Nursing": 9500,
    "Oral Hygiene": 9556,
    "Advertising and Marketing Management": 9670,
    "Journalism and Communication": 9773,
    "Basic Education": 9853,
    "Management (evening attendance)": 9991
}

Course = st.selectbox(label="Course", options=list(course_mapping.keys()))
course_value = course_mapping[Course]

data["Course"] = [course_value]

attendance_mapping = {
    "Daytime": 1,
    "Evening": 0
}

Attendance = st.selectbox("Class Attendance Time", list(attendance_mapping.keys()))
data["Daytime_evening_attendance"] = [attendance_mapping[Attendance]]

previous_qualification_mapping = {
    "Secondary education": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "10th year of schooling - not completed": 15,
    "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
    "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43
}

Previous_qualification = st.selectbox("Previous Qualification", list(previous_qualification_mapping.keys()))
data["Previous_qualification"] = [previous_qualification_mapping[Previous_qualification]]

Previous_qualification_grade= float(st.number_input(label='Previous_qualification_grade', value=0.0))
data["Previous_qualification_grade"] = Previous_qualification_grade

nationality_mapping = {
    "Portuguese": 1,
    "German": 2,
    "Spanish": 6,
    "Italian": 11,
    "Dutch": 13,
    "English": 14,
    "Lithuanian": 17,
    "Angolan": 21,
    "Cape Verdean": 22,
    "Guinean": 24,
    "Mozambican": 25,
    "Santomean": 26,
    "Turkish": 32,
    "Brazilian": 41,
    "Romanian": 62,
    "Moldova (Republic of)": 100,
    "Mexican": 101,
    "Ukrainian": 103,
    "Russian": 105,
    "Cuban": 108,
    "Colombian": 109
}

nationality = st.selectbox("Nationality", list(nationality_mapping.keys()))
data["Nacionality"] = [nationality_mapping[nationality]]

mothers_qualification_mapping = {
    "Secondary Education - 12th Year of Schooling or Eq.": 1,
    "Higher Education - Bachelor's Degree": 2,
    "Higher Education - Degree": 3,
    "Higher Education - Master's": 4,
    "Higher Education - Doctorate": 5,
    "Frequency of Higher Education": 6,
    "12th Year of Schooling - Not Completed": 9,
    "11th Year of Schooling - Not Completed": 10,
    "7th Year (Old)": 11,
    "Other - 11th Year of Schooling": 12,
    "10th Year of Schooling": 14,
    "General commerce course": 18,
    "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
    "Technical-professional course": 22,
    "7th year of schooling": 26,
    "2nd cycle of the general high school course": 27,
    "9th Year of Schooling - Not Completed": 29,
    "8th year of schooling": 30,
    "Unknown": 34,
    "Can't read or write": 35,
    "Can read without having a 4th year of schooling": 36,
    "Basic education 1st cycle (4th/5th year) or equiv.": 37,
    "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Specialized higher studies course": 41,
    "Professional higher technical course": 42,
    "Higher Education - Master (2nd cycle)": 43,
    "Higher Education - Doctorate (3rd cycle)": 44
}

mothers_qualification = st.selectbox("Mother's Qualification", list(mothers_qualification_mapping.keys()))
data["Mothers_qualification"] = [mothers_qualification_mapping[mothers_qualification]]

fathers_qualification_mapping = {
    "Secondary Education - 12th Year of Schooling or Eq.": 1,
    "Higher Education - Bachelor's Degree": 2,
    "Higher Education - Degree": 3,
    "Higher Education - Master's": 4,
    "Higher Education - Doctorate": 5,
    "Frequency of Higher Education": 6,
    "12th Year of Schooling - Not Completed": 9,
    "11th Year of Schooling - Not Completed": 10,
    "7th Year (Old)": 11,
    "Other - 11th Year of Schooling": 12,
    "2nd year complementary high school course": 13,
    "10th Year of Schooling": 14,
    "General commerce course": 18,
    "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
    "Complementary High School Course": 20,
    "Technical-professional course": 22,
    "Complementary High School Course - not concluded": 25,
    "7th year of schooling": 26,
    "2nd cycle of the general high school course": 27,
    "9th Year of Schooling - Not Completed": 29,
    "8th year of schooling": 30,
    "General Course of Administration and Commerce": 31,
    "Supplementary Accounting and Administration": 33,
    "Unknown": 34,
    "Can't read or write": 35,
    "Can read without having a 4th year of schooling": 36,
    "Basic education 1st cycle (4th/5th year) or equiv.": 37,
    "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Specialized higher studies course": 41,
    "Professional higher technical course": 42,
    "Higher Education - Master (2nd cycle)": 43,
    "Higher Education - Doctorate (3rd cycle)": 44
}

fathers_qualification = st.selectbox("Father's Qualification", list(fathers_qualification_mapping.keys()))
data["Fathers_qualification"] = [fathers_qualification_mapping[fathers_qualification]]

mothers_occupation_mapping = {
    "Student": 0,
    "Legislative/Executive Roles, Directors & Managers": 1,
    "Specialists in Intellectual and Scientific Activities": 2,
    "Intermediate Level Technicians and Professions": 3,
    "Administrative staff": 4,
    "Personal Services, Security, Safety Workers & Sellers": 5,
    "Farmers and Skilled Workers in Agriculture, Fisheries, Forestry": 6,
    "Skilled Workers in Industry, Construction and Craftsmen": 7,
    "Machine Operators and Assembly Workers": 8,
    "Unskilled Workers": 9,
    "Armed Forces Professions": 10,
    "Other Situation": 90,
    "(blank)": 99,
    "Health professionals": 122,
    "Teachers": 123,
    "ICT Specialists": 125,
    "Science and Engineering Technicians (Intermediate Level)": 131,
    "Health Technicians (Intermediate Level)": 132,
    "Technicians in Legal, Social, Sports, Cultural Services": 134,
    "Office workers, secretaries, data processing operators": 141,
    "Accounting, Statistical, Financial, Registry Operators": 143,
    "Other administrative support staff": 144,
    "Personal service workers": 151,
    "Sellers": 152,
    "Personal care workers": 153,
    "Skilled construction workers (excl. electricians)": 171,
    "Skilled workers in printing, instruments, jewelry, artisans": 173,
    "Workers in food, wood, clothing industries and crafts": 175,
    "Cleaning workers": 191,
    "Unskilled agricultural/fishery/forestry workers": 192,
    "Unskilled workers in construction, manufacturing, transport": 193,
    "Meal preparation assistants": 194
}

mothers_occupation = st.selectbox("Mother's Occupation", list(mothers_occupation_mapping.keys()))
data["Mothers_occupation"] = [mothers_occupation_mapping[mothers_occupation]]

fathers_occupation_mapping = {
    "Student": 0,
    "Legislative/Executive Roles, Directors & Managers": 1,
    "Specialists in Intellectual and Scientific Activities": 2,
    "Intermediate Level Technicians and Professions": 3,
    "Administrative staff": 4,
    "Personal Services, Security and Safety Workers and Sellers": 5,
    "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
    "Skilled Workers in Industry, Construction and Craftsmen": 7,
    "Machine Operators and Assembly Workers": 8,
    "Unskilled Workers": 9,
    "Armed Forces Professions": 10,
    "Other Situation": 90,
    "(blank)": 99,
    "Armed Forces Officers": 101,
    "Armed Forces Sergeants": 102,
    "Other Armed Forces personnel": 103,
    "Directors of administrative and commercial services": 112,
    "Hotel, catering, trade and other services directors": 114,
    "Specialists in physical sciences, math, engineering": 121,
    "Health professionals": 122,
    "Teachers": 123,
    "Finance, accounting, admin org, PR specialists": 124,
    "Science and engineering technicians (Intermediate Level)": 131,
    "Health Technicians (Intermediate Level)": 132,
    "Technicians in legal, social, sports, cultural services": 134,
    "ICT Technicians": 135,
    "Office workers, secretaries, data processing operators": 141,
    "Accounting, Statistical, Financial, Registry Operators": 143,
    "Other administrative support staff": 144,
    "Personal service workers": 151,
    "Sellers": 152,
    "Personal care workers": 153,
    "Protection and security services personnel": 154,
    "Market-oriented farmers and skilled agri workers": 161,
    "Subsistence farmers, fishermen, hunters, gatherers": 163,
    "Skilled construction workers (excl. electricians)": 171,
    "Skilled metallurgy, metalworking workers": 172,
    "Skilled electricity and electronics workers": 174,
    "Workers in food, wood, clothing industries and crafts": 175,
    "Fixed plant and machine operators": 181,
    "Assembly workers": 182,
    "Vehicle drivers and mobile equipment operators": 183,
    "Unskilled agri/fish/forestry workers": 192,
    "Unskilled workers in construction, manufacturing, transport": 193,
    "Meal preparation assistants": 194,
    "Street vendors (except food) & service providers": 195
}

fathers_occupation = st.selectbox("Father's Occupation", list(fathers_occupation_mapping.keys()))
data["Fathers_occupation"] = [fathers_occupation_mapping[fathers_occupation]]

Admission_grade= float(st.number_input(label='Admission_grade', value=0.0))
data["Admission_grade"] = Admission_grade

displaced_mapping = {
    "Yes": 1,
    "No": 0
}

displaced = st.selectbox("Is the student displaced?", list(displaced_mapping.keys()))
data["Displaced"] = [displaced_mapping[displaced]]

educational_needs_mapping = {
    "Yes": 1,
    "No": 0
}

educational_needs = st.selectbox("Does the student have special educational needs?", list(educational_needs_mapping.keys()))
data["Educational_special_needs"] = [educational_needs_mapping[educational_needs]]

debtor_mapping = {
    "Yes": 1,
    "No": 0
}

debtor = st.selectbox("Is the student a debtor?", list(debtor_mapping.keys()))
data["Debtor"] = [debtor_mapping[debtor]]

tuition_fees_mapping = {
    "Yes": 1,
    "No": 0
}

tuition_fees = st.selectbox("Are the student's tuition fees up to date?", list(tuition_fees_mapping.keys()))
data["Tuition_fees_up_to_date"] = [tuition_fees_mapping[tuition_fees]]

gender_mapping = {
    "Male": 1,
    "Female": 0
}

gender = st.selectbox("Gender of the student", list(gender_mapping.keys()))
data["Gender"] = [gender_mapping[gender]]

scholarship_mapping = {
    "Yes": 1,
    "No": 0
}

scholarship = st.selectbox("Is the student a scholarship holder?", list(scholarship_mapping.keys()))
data["Scholarship_holder"] = [scholarship_mapping[scholarship]]

Age_at_enrollment= int(st.number_input(label='Age_at_enrollment', value=0))
data["Age_at_enrollment"] = Age_at_enrollment

international_mapping = {
    "Yes": 1,
    "No": 0
}

international = st.selectbox("Is the student an international student?", list(international_mapping.keys()))
data["International"] = [international_mapping[international]]

Curricular_units_1st_sem_credited= int(st.number_input(label='Curricular_units_1st_sem_credited', value=0))
data["Curricular_units_1st_sem_credited"] = Curricular_units_1st_sem_credited

Curricular_units_1st_sem_enrolled= int(st.number_input(label='Curricular_units_1st_sem_enrolled', value=0))
data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled

Curricular_units_1st_sem_evaluations= int(st.number_input(label='Curricular_units_1st_sem_evaluations', value=0))
data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations

Curricular_units_1st_sem_approved= int(st.number_input(label='Curricular_units_1st_sem_approved', value=0))
data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved

Curricular_units_1st_sem_grade= float(st.number_input(label='Curricular_units_1st_sem_grade', value=0.0))
data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade

Curricular_units_1st_sem_without_evaluations= int(st.number_input(label='Curricular_units_1st_sem_without_evaluations', value=0))
data["Curricular_units_1st_sem_without_evaluations"] = Curricular_units_1st_sem_without_evaluations

Curricular_units_2nd_sem_credited= int(st.number_input(label='Curricular_units_2nd_sem_credited', value=0))
data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited

Curricular_units_2nd_sem_enrolled= int(st.number_input(label='Curricular_units_2nd_sem_enrolled', value=0))
data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled

Curricular_units_2nd_sem_evaluations= int(st.number_input(label='Curricular_units_2nd_sem_evaluations', value=0))
data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations

Curricular_units_2nd_sem_approved= int(st.number_input(label='Curricular_units_2nd_sem_approved', value=0))
data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved

Curricular_units_2nd_sem_grade= float(st.number_input(label='Curricular_units_2nd_sem_grade', value=0.0))
data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade

Curricular_units_2nd_sem_without_evaluations= int(st.number_input(label='Curricular_units_2nd_sem_without_evaluations', value=0))
data["Curricular_units_2nd_sem_without_evaluations"] = Curricular_units_2nd_sem_without_evaluations

Unemployment_rate= float(st.number_input(label='Unemployment_rate', value=0.0))
data["Unemployment_rate"] = Unemployment_rate

Inflation_rate= float(st.number_input(label='Inflation_rate', value=0.0))
data["Inflation_rate"] = Inflation_rate

GDP= float(st.number_input(label='GDP', value=0.0))
data["GDP"] = GDP

st.dataframe(data=data, width=1200, height=10)

if st.button('Predict'):
    new_data = data_processing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Status: {}".format(prediction(new_data)))