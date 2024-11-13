import streamlit as st  # ตรวจสอบให้แน่ใจว่าได้ import streamlit แล้ว
# Custom CSS for styling
import time


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
# Custom CSS for styling
page_style = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700&display=swap');
    
    /* Apply Nunito font to the entire app */
    * {
        font-family: 'Nunito', sans-serif;
    }
    
    /* Background color and layout adjustments */
    .stApp {
        background: linear-gradient(to bottom, #ff7f50 100px, white 100px);
    }
    
    /* Top banner styling */
    .top-banner {
        background-color: #ff7f50;  /* Orange color */
        height: 20px;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 24px;
        font-weight: bold;
    }

    /* Main title styling */
    h1 {
        color: #ff6347;
        text-align: center;
        font-size: 34px;
        font-weight: bold;
        padding-top: 20px;  /* Pushes the title below the banner */
    }
    
    /* Centering the subtitle text */
    .subtitle-text {
        text-align: center;
        font-size: 16px;
        font-weight: normal;
        margin-top: 10px;
        color: #333333;
    }

    /* Button styling */
    .stButton button {
        background-color: #ff7f50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #ff6347;
    }

    /* Centering buttons for navigation */
    .centered-buttons {
        display: flex;
        justify-content: space-between;
        margin-top: 20px;
    }
    </style>
"""

# Apply the CSS
st.markdown(page_style, unsafe_allow_html=True)

# Your app logic goes here...

# Rest of your Streamlit code including steps


#st.markdown('<div class="top-banner">CRA LungCheck</div>', unsafe_allow_html=True)

# Step 1 - General Information
if st.session_state["step"] == 1:
    st.title("CRA LungCheck")
    st.markdown('<div class="subtitle-text">Please enter your information for pre-screening Restrictive defect</div>', unsafe_allow_html=True)
    st.write("****Step 1****")
    st.header("General Information")
##แบบปุ่ม3ปุ่ม มีปุ่มว่าง ถ้าไม่กดเลือกเพศ จะบอกให้ User กด
        # แสดงปุ่ม radio โดยให้ตัวเลือกแรกเป็นค่าว่าง
    #gender_options = ["", "Male", "Female"]
    #gender = st.radio("Gender", gender_options, key="gender_step1")
    # ตรวจสอบว่าผู้ใช้เลือกเพศหรือยัง
    #if gender:
        #st.write(f"Gender selected: {gender}")
    #else:
        #st.write("Please select your gender.")
    # แสดงตัวเลือกเพศโดยมีค่าเริ่มต้นเป็น "Select" (ค่าว่าง)
##แบบเลือกช่องสี่เหลี่ยม
    gender_options = ["Select", "Male", "Female"]
    gender = st.selectbox("Gender", gender_options, key="gender_step1")

    # ตรวจสอบว่าผู้ใช้เลือกเพศหรือยัง
    if gender != "Select":
        st.write(f"Gender selected: {gender}")
    else:
        st.write("Please select your gender.")

##แบบกดเลือก 2 ปุ่ม
    #Gender selection
    #gender = st.radio("Gender", ["Male", "Female"], key="gender_step1")

    # Age input
    age = st.number_input("Age", min_value=0, max_value=120, value=0, key="age_step1")

    # Weight and Height inputs
    weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, value=0.0, key="weight_step1")
    height = st.number_input("Height (cm)", min_value=0.0, max_value=250.0, value=0.0, key="height_step1")

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
    status_options = ["Please choose","Single", "Married", "Divorced", "Separated", "Widowed"]
    status = st.radio("Status", status_options, key="status_step1",index=0)

     # Validation check before proceeding to Step 2
    if st.button("Next"):
        # Check if any of the required fields are missing
        if gender == "Select" or age == 0 or weight == 0.0 or height == 0.0 or education == "" or status == "Please choose":
            st.warning("Please fill out all the fields before proceeding.")
        else:
            # Proceed to Step 2 if all fields are completed
            next_step()



# Step 2 - Risky Behavior
# ตัวอย่างการตั้งค่าให้มี "None" หรือ "Please choose" เป็นค่าเริ่มต้นในทุกขั้นตอนของ step2
elif st.session_state["step"] == 2:
    st.title("CRA LungCheck")
    st.markdown('<div class="subtitle-text">Please enter your information for pre-screening Restrictive defect</div>', unsafe_allow_html=True)
    st.write("****Step 2****")
    st.header("Risky Behavior")

    # Current smoker (required)
    current_smoker = st.radio("**Current smoker**", ["Please choose", "Yes", "No"], key="current_smoker_step2", index=0)

    # Display fields based on user selections
    if current_smoker == "Yes":
        smoked_per_day = st.number_input("Smoked per day", min_value=1, max_value=100, value=1, key="smoked_per_day_step2")

    # Cigarette Type (required)
    cigarette_type = st.radio("Cigarette Type", ["Please choose", "Never smoked", "Filtered", "Non-filtered", "Both"], key="cigarette_type_step2", index=0)

    # Lung Inhale Smoking (required)
    lung_inhale = st.radio("Lung Inhale Smoking", ["Please choose", "Never smoked", "Inhaled deeply", "Not inhaled deeply", "Sometimes inhaled deeply"], key="lung_inhale_step2", index=0)

    # Alcohol section (required)
    alcohol = st.radio("**Alcohol**", ["Please choose", "Never drank before", "Used to drink but quit", "Still drinking"], key="alcohol_step2", index=0)

    # Drinking Frequency (only if still drinking)
    if alcohol == "Still drinking" or alcohol == "Used to drink but quit":
        drinking_frequency = st.radio("Drinking Frequency", ["Please choose","Drink a little", "Once a week", "2-3 times a week", "4 times or more per week"], key="drinking_frequency_step2", index=0)

    col1, col2 = st.columns(2)
    with col2:
    # Check if all required fields are filled
        if (current_smoker != "Please choose" and cigarette_type != "Please choose" and 
            lung_inhale != "Please choose" and alcohol != "Please choose" and 
            (alcohol != "Still drinking" or (alcohol == "Still drinking" and drinking_frequency != "Please choose"))):
            # Display Next button only when all fields are completed
            if st.button("Next"):
                next_step()
        else:
            st.warning("Please fill in all required information before proceeding.")
    with col1:
    # Back button
        if st.button("Back"):
            prev_step()
    
    

 
# Step 3 - Working Information
elif st.session_state["step"] == 3:
    st.title("CRA LungCheck")
    st.markdown('<div class="subtitle-text">Please enter your information for pre-screening Restrictive defect</div>', unsafe_allow_html=True)
    st.write("****Step 3****")
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
        dust_level_factory = st.number_input("Dust Level (Fac.)", min_value=0.0, max_value=1000.0, value=0.0, key="dust_level_factory_step3")
    with col4:
        dust_level_department = st.number_input("Dust Level (Dep.)", min_value=0.0, max_value=1000.0, value=0.0, key="dust_level_department_step3")

    # Question with Yes/No option
    question = st.radio("Previous Department", ["Please choose", "Yes", "No"], key="hazardous_exposure_step3", index=0)

    # Duration Working (Year and Month)
    col5, col6 = st.columns(2)
    with col5:
        working_years = st.number_input("Duration Working - Years", min_value=0, max_value=50, value=1, key="working_years_step3")
    with col6:
        working_months = st.number_input("Duration Working - Months", min_value=0, max_value=11, value=0, key="working_months_step3")

    # Additional Working Details
    col7, col8 = st.columns(2)
    with col7:
        working_hours_per_day = st.number_input("Working hours per day", min_value=0.0, max_value=24.0, value=0.0, key="working_hours_day_step3")
    with col8:
        working_days_per_week = st.number_input("Working days per week", min_value=0, max_value=7, value=0, key="working_days_week_step3")

    col9, col10 = st.columns(2)
    with col9:
        ot_hours_per_week = st.number_input("OT hours per week", min_value=0.0, max_value=168.0, value=0.0, key="ot_hours_week_step3")
    with col10:
        break_time_per_day = st.number_input("Break Time hours per day", min_value=0.0, max_value=24.0, value=0.0, key="break_time_day_step3")

    # Sleep Time per day
    sleep_time_per_day = st.number_input("Sleep Time hours per day", min_value=0.0, max_value=24.0, value=0.0, key="sleep_time_day_step3")

    # Navigation buttons with validation
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            prev_step()
    with col2:
        # Validate required fields before allowing navigation
        if (factory_name and department and question != "Please choose" and 
            dust_level_factory >= 0 and dust_level_department >= 0 and
            working_years >= 0 and working_months >= 0 and
            working_hours_per_day >= 0 and working_days_per_week > 0 and
            ot_hours_per_week >= 0 and break_time_per_day >= 0 and 
            sleep_time_per_day >= 0):
            if st.button("Next"):
                next_step()
        else:
            st.warning("Please fill in all required fields before proceeding.")


#step4
elif st.session_state["step"] == 4:
    st.title("CRA LungCheck")
    st.markdown('<div class="subtitle-text">Please enter your information for pre-screening Restrictive defect</div>', unsafe_allow_html=True)
    st.write("****Step 4****")
    st.header("Health Information")
    
    # Using st.form to avoid automatic updates on each change
    with st.form(key="health_info_form"):
        st.write("***In the past 5 years***")
        tuberculosis = st.radio("Tuberculosis", ["Yes", "No", "Unsure"], key="tuberculosis_5years")
        asthma = st.radio("Asthma", ["Yes", "No", "Unsure"], key="asthma_5years")
        pulmonary_tb = st.radio("Pulmonary TB", ["Yes", "No", "Unsure"], key="pulmonary_5years")

# Current illness section
        st.write("***Current Illness***")
        current_illness = st.radio("Do you have any current illness? ""**(If not, please select No for the next question.)**", ["Yes", "No"], key="current_illness")
        if current_illness == "Yes":
            asthma_current = st.radio("Asthma", ["Yes", "No"], key="asthma_current")
            emphysema_current = st.radio("Emphysema", ["Yes", "No"], key="emphysema_current")
            Bronchitis_current = st.radio("Bronchitis", ["Yes","No"], key="Bronchitis_current_illness")
            Sinusitis_current = st.radio("Sinusitis", ["Yes","No"], key="Sinusitis_current_illness")
            InjurySurgery_current = st.radio("Injury/Surgery", ["Yes","No"], key="InjurySurgery_current_illness")
            Allergies_current = st.radio("Allergies", ["Yes","No"], key="Allergies_current_illness")
            Tuberculosis_current = st.radio("Tuberculosis", ["Yes","No"], key="Tuberculosis_current_illness")
            Heart_current = st.radio("Heart Disease", ["Yes","No"], key="Heart Disease_current_illness")
            Pneumonia_current = st.radio("Pneumonia", ["Yes","No"], key="Pneumonia_current_illness")
            Other_current = st.radio("Other", ["Yes","No"], key="Other_current_illness")


        # Submit button inside the form
        submitted = st.form_submit_button("Submit")
        if submitted:
            next_step()  # Move to the next step only after submitting the form

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            prev_step()

#step5 analysis in progress
elif st.session_state["step"] == 5:
    import time
    # Background video setup
    background_video_url = "https://www.dropbox.com/scl/fi/dzxtr5hucba891bysghcn/CRALungCheck_analysis.mp4?rlkey=p6u1mzytur5ljuo9lstk94m4m&dl=1"

    page_bg_video = f"""
    <style>
    .stApp {{
        position: relative;
        overflow: hidden;
    }}
    .background-video {{
        position: fixed;
        right: 0;
        bottom: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: -1;
    }}
    </style>
    <video autoplay muted loop class="background-video">
        <source src="{background_video_url}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    """

    st.markdown(page_bg_video, unsafe_allow_html=True)

    # Timer for waiting before moving to the next step
    st.write("Please wait... Redirecting to the next page in 10 seconds.")

    # Initialize session state timer
    if "start_time" not in st.session_state:
        st.session_state["start_time"] = time.time()

    # Calculate elapsed time
    elapsed_time = time.time() - st.session_state["start_time"]

    # Automatically move to the next step after 5 seconds
    if elapsed_time > 1:
        st.session_state["step"] = 6  # Move to the next step
        st.experimental_rerun()  # Rerun the page to reflect the change
    else:
        # Display remaining time
        st.write(f"Redirecting in {int(10 - elapsed_time)} seconds...")



# Step 6 - Health Information
elif st.session_state["step"] == 6:
    import streamlit as st
    import streamlit as st

    # Custom JavaScript for detecting device type
    detect_device_type = """
        <script>
        function detectDeviceType() {
            let deviceType = (window.innerWidth <= 768) ? "mobile" : "desktop";
            // Communicate this to Streamlit (without visible input)
            window.parent.postMessage({deviceType: deviceType}, '*');
        }
        window.onload = detectDeviceType;
        window.onresize = detectDeviceType;
    </script>
    """

    # Add JavaScript detection logic to the page
    st.markdown(detect_device_type, unsafe_allow_html=True)

    # Listening for messages from the JavaScript
    device_type_placeholder = st.empty()  # This placeholder can be used to display data if needed but is empty for now
    if "device_type" not in st.session_state:
        st.session_state["device_type"] = "desktop"  # Default value

    # Apply a background image based on detected device type
    if st.session_state["device_type"] == "mobile":
        background_image_url2 = "https://www.dropbox.com/scl/fi/u5hpnakxokiz74hwk5sje/Normal_phone.png?rlkey=115rowkzjrx01zalvx7lu3wwg&st=2mck304a&raw=1"
    else:
        background_image_url2 = "https://www.dropbox.com/scl/fi/z46r68ij0pqaldp0ba0vk/Normal_computer.png?rlkey=a4kqijjsw8vgb50na3mo1mkds&st=tdl43df9&raw=1"

    # Apply background image
    page_bg_img = f"""
        <style>
        .stApp {{
            background-image: url("{background_image_url2}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
        }}
        .return-button {{
            display: flex;
            justify-content: center;
            align-items: center;
            position: absolute;
            bottom: 10px;
            width: 100%;
        }}
        .stButton {{
            position: fixed;
            bottom: 6px;
            right: 20px;
            z-index: 10; /* To ensure the button is above other elements */
            color: white; /* White text color */
            border: none; /* Remove border */
            padding: 10px 10px; /* Button padding */
            font-size: 16px; /* Font size */
            border-radius: 5px; /* Rounded corners */
        }}
        
        </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Navigation button to reset state (centered at the bottom)
    button_container = st.container()
    with button_container:
        st.markdown('<div class="return-button">', unsafe_allow_html=True)
        if st.button("Return to Home"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.session_state["reloaded"] = True
            st.query_params.clear() # Refresh page
        st.markdown('</div>', unsafe_allow_html=True)
