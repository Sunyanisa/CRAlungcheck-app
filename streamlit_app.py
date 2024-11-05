import streamlit as st  # ตรวจสอบให้แน่ใจว่าได้ import streamlit แล้ว

# ฟังก์ชันสำหรับล้างข้อมูลทั้งหมดใน session_state และกลับไปยัง step 1
def reset_state():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state["step"] = 1  # กลับไปที่ขั้นตอนแรก

# ตรวจสอบว่า session_state มีการกำหนดค่าเริ่มต้นหรือยัง
if "step" not in st.session_state:
    st.session_state["step"] = 1  # กำหนดค่าเริ่มต้นที่ step 1

# กำหนดการล้างข้อมูลทั้งหมดเมื่อรีโหลดหน้าเว็บ
if "reloaded" not in st.session_state:
    reset_state()
    st.session_state["reloaded"] = True
    st.session_state["step"] == 1  # กลับมาขั้นตอนที่ 1

# Initialize session state for navigation
if "step" not in st.session_state:
    reset_state()
    st.session_state["step"] = 1

# # Function to move to the next step
def next_step():
    st.session_state["step"] += 1

#back
def prev_step():
    st.session_state["step"] -= 1

#if "step" not in st.session_state:
    #st.session_state["step"] = 1


# Step 1 - General Information
if st.session_state["step"] == 1:
    st.title("CRA LungCheck")
    st.write("Please enter your information for pre-screening Restrictive defect")  # ข้อความที่คุณต้องการเพิ่ม
    st.write("**Step 1**")
    st.header("General Information")

    # Gender selection
    gender = st.radio("Gender", ["Male", "Female"], key="gender_step1")

    # Age input
    age = st.number_input("Age", min_value=0, max_value=120, value=25, key="age_step1")

    # Weight and Height inputs
    weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, value=70.0, key="weight_step1")
    height = st.number_input("Height (cm)", min_value=0.0, max_value=250.0, value=170.0, key="height_step1")

    # Educational Level selection
    educational_levels = [
        "No formal education (Primary level)", 
        "Primary level, grade 4",
        "Primary level, Grade 6",
        "Junior high school",
        "High school equivalent",
        "Associate degree",
        "Degree or higher"
    ]
    education = st.selectbox("Educational Level", educational_levels, key="education_step1")

    # Status selection
    status_options = ["Single", "Married", "Divorced", "Separated", "Widowed"]
    status = st.radio("Status", status_options, key="status_step1")

    # "Next" button to proceed to Step 2
    if st.button("Next"):
        next_step()

# Step 2 - Risky Behavior
elif st.session_state["step"] == 2:
    st.title("CRA LungCheck")
    st.write("Please enter your information for pre-screening Restrictive defect")  # ข้อความที่คุณต้องการเพิ่ม
    st.write("**Step 2**")
    st.header("Risky Behavior")

    # Current smoker
    current_smoker = st.radio("Current smoker", ["Yes", "No"], key="current_smoker_step2")

    # Smoked per day (only if current smoker is Yes)
    if current_smoker == "Yes":
        smoked_per_day = st.number_input("Smoked per day", min_value=1, max_value=100, value=10, key="smoked_per_day_step2")

    # Cigarette Type
    cigarette_type = st.radio("Cigarette Type", ["Never smoked", "Filtered", "Non-filtered", "Both"], key="cigarette_type_step2")

    # Lung Inhale Smoking
    lung_inhale = st.radio("Lung Inhale Smoking", ["Never smoked", "Inhaled deeply", "Not inhaled deeply", "Sometimes inhaled deeply"], key="lung_inhale_step2")

    # Alcohol
    alcohol = st.radio("Alcohol", ["Never drank before", "Used to drink but quit", "Still drinking"], key="alcohol_step2")

    # Drinking Frequency (only if still drinking)
    if alcohol == "Still drinking":
        drinking_frequency = st.radio("Drinking Frequency", ["Never drank", "Drink a little", "Once a week", "2-3 times a week", "4 times or more per week"], key="drinking_frequency_step2")

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            prev_step()
    with col2:
        if st.button("Next"):
            next_step()  # ไปยังขั้นตอนถัดไป (Step 3) 
    
    
# Step 3 - Working Information
elif st.session_state["step"] == 3:
    st.title("CRA LungCheck")
    st.write("Please enter your information for pre-screening Restrictive defect")  # ข้อความที่คุณต้องการเพิ่ม
    st.write("**Step 3**")
    st.header("Working Information")

    # Factory Name and Department
    col1, col2 = st.columns(2)
    with col1:
        factory_name = st.text_input("Factory Name", key="factory_name_step3")
    with col2:
        department = st.text_input("Department", key="department_step3")

    # Dust Level (Factory and Department)
    col3, col4 = st.columns(2)
    with col3:
        dust_level_factory = st.number_input("Dust Level (Fac.)", min_value=0.0, max_value=1000.0, value=50.0, key="dust_level_factory_step3")
    with col4:
        dust_level_department = st.number_input("Dust Level (Dep.)", min_value=0.0, max_value=1000.0, value=50.0, key="dust_level_department_step3")

    # Question with Yes/No option
    question = st.radio("Previous Department", ["Yes", "No"], key="hazardous_exposure_step3")

    # Duration Working (Year and Month)
    col5, col6 = st.columns(2)
    with col5:
        working_years = st.number_input("Duration Working - Years", min_value=0, max_value=50, value=1, key="working_years_step3")
    with col6:
        working_months = st.number_input("Duration Working - Months", min_value=0, max_value=11, value=0, key="working_months_step3")

    # Additional Working Details
    col7, col8 = st.columns(2)
    with col7:
        working_hours_per_day = st.number_input("Working hours per day", min_value=0.0, max_value=24.0, value=8.0, key="working_hours_day_step3")
    with col8:
        working_days_per_week = st.number_input("Working days per week", min_value=0, max_value=7, value=5, key="working_days_week_step3")

    col9, col10 = st.columns(2)
    with col9:
        ot_hours_per_week = st.number_input("OT hours per week", min_value=0.0, max_value=168.0, value=0.0, key="ot_hours_week_step3")
    with col10:
        break_time_per_day = st.number_input("Break Time hours per day", min_value=0.0, max_value=24.0, value=1.0, key="break_time_day_step3")

    # Sleep Time per day
    sleep_time_per_day = st.number_input("Sleep Time hours per day", min_value=0.0, max_value=24.0, value=8.0, key="sleep_time_day_step3")

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            prev_step()
    with col2:
        if st.button("Next"):
            next_step()  # ไปยังขั้นตอนถัดไป (Step 4) หากมี

# Step 4 - Health Information
elif st.session_state["step"] == 4:
    st.title("CRA LungCheck")
    st.write("Please enter your information for pre-screening Restrictive defect")  # ข้อความที่คุณต้องการเพิ่ม
    st.write("**Step 4**")
    st.header("Health Information")

#In the past 5 years
    st.write("***In the past 5 years***")
##In the past 5 years Tuberculosis_5years
# Tuberculosis_5years selection
    Tuberculosis_5years_options = ["Yes", "No","Unsure"]
    Tuberculosis_5years = st.radio(" Tuberculosis",Tuberculosis_5years_options, key="Tuberculosis_5years")
    #Tuberculosis_5years = st.radio("Tuberculosis ", ["Yes", "No","Unsure"], key="Tuberculosis_5years") #Stay different the lines
##In the past 5 years Asthma_5years
    Asthma_5years = st.radio("Asthma", Tuberculosis_5years_options , key="Asthma_5years") 
##In the past 5 years Pulmonary_5years
    Pulmonary_5years = st.radio("Pulmonary TB", Tuberculosis_5years_options , key="Pulmonary_5years") 

#Current illness
# Current illness selection
    Current_illness_options = ["Yes", "No"]
    status2 = st.radio("***Current_illness***",Current_illness_options, key="Current_illness")
# Current (only if Yes Current illness)
    if status2 == "Yes":
        Asthma_current = st.radio("Asthma", ["Yes","No"], key="asthma_current_illness")
        Emphysema_current = st.radio("Emphysema", ["Yes","No"], key="Emphysema_current_illness")
        Bronchitis_current = st.radio("Bronchitis", ["Yes","No"], key="Bronchitis_current_illness")
        Sinusitis_current = st.radio("Sinusitis", ["Yes","No"], key="Sinusitis_current_illness")
        InjurySurgery_current = st.radio("Injury/Surgery", ["Yes","No"], key="InjurySurgery_current_illness")
        Allergies_current = st.radio("Allergies", ["Yes","No"], key="Allergies_current_illness")
        Tuberculosis_current = st.radio("Tuberculosis", ["Yes","No"], key="Tuberculosis_current_illness")
        Heart_current = st.radio("Heart Disease", ["Yes","No"], key="Heart Disease_current_illness")
        Pneumonia_current = st.radio("Pneumonia", ["Yes","No"], key="Pneumonia_current_illness")
        Other_current = st.radio("Other", ["Yes","No"], key="Other_current_illness")

 # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            prev_step()
    with col2:
        if st.button("Next"):
            next_step()  # ไปยังขั้นตอนถัดไปประมวล

# Step 5 - Predicting Page
elif st.session_state["step"] == 5:
    st.title("CRA LungCheck")
    st.subheader("Hello!")  # ชื่อผู้ใช้อาจตั้งค่าได้จากข้อมูลจริง
    st.write("How are you today?")
    
    # "Next" button to proceed to Step 2
    if st.button("Next"):
        next_step()
    # Button to reset everything and go back to step 1
    if st.button("Reset"):
        reset_state()


    # แสดงสัญลักษณ์ยิ้มขนาดใหญ่
    #st.markdown("<h1 style='text-align: center; color: orange;'>😊</h1>", unsafe_allow_html=True)

    # แสดงข้อความ Predicting...
    #st.markdown("<p style='text-align: center; color: orange;'>Predicting...</p>", unsafe_allow_html=True)

    # แสดงชื่อระบบที่ด้านล่าง
    #st.markdown("<h3 style='text-align: center; color: orange;'>CRA LungCheck</h3>", unsafe_allow_html=True)

    # ปุ่มกลับไปยังหน้าแรกหรือทำการประมวลผลใหม่ (ขึ้นอยู่กับการออกแบบของคุณ)
    #st.button("Return to Home", on_click=lambda: st.session_state.update(step=1))

    

