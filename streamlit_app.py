import streamlit as st
import time
import requests
import json  # Import json to save data
import pandas as pd
from pycaret.classification import *
from transform import transform_user_data


# Function to reset state
def reset_state():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state["step"] = 1  # Reset to step 1

# Initialize session state
if "step" not in st.session_state:
    st.session_state["step"] = 1

# Functions to navigate between steps
def next_step():
    st.session_state["step"] += 1

def prev_step():
    st.session_state["step"] -= 1

# Custom CSS for styling
page_style = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700&display=swap');
    * {
        font-family: 'Nunito', sans-serif;
    }
    .stApp {
        background: linear-gradient(to bottom, #ff7f50 100px, white 100px);
    }
    .top-banner {
        background-color: #ff7f50;
        height: 20px;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 24px;
        font-weight: bold;
    }
    h1 {
        color: #ff6347;
        text-align: center;
        font-size: 34px;
        font-weight: bold;
        padding-top: 20px;
    }
    .subtitle-text {
        text-align: center;
        font-size: 14px;
        font-weight: normal;
        margin-top: 10px;
        color: #333333;
    }
    .stButton button {
        background-color: #ff7f50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 20px;
        font-size: 14px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #ff6347;
    }
    .centered-buttons {
        display: flex;
        justify-content: space-between;
        margin-top: 20px;
    }
    </style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# Step 1 - General Information
if st.session_state["step"] == 1:
    st.title("CRA LungCheck")
    st.markdown('<div class="subtitle-text">Please enter your information for pre-screening Restrictive defect</div>', unsafe_allow_html=True)
    st.write("****Step 1****")
    st.header("General Information")

    # Gender selection
    gender_options = ["Select", "Male", "Female"]
    st.session_state.gender_step1 = st.selectbox("Gender", gender_options, index=0)

    # Age input
    st.session_state.age_step1 = st.number_input("Age", min_value=0, max_value=120, value=0)

    # Weight and Height inputs
    st.session_state.weight_step1 = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, value=0.0)
    st.session_state.height_step1 = st.number_input("Height (cm)", min_value=0.0, max_value=250.0, value=0.0)

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
    st.session_state.education_step1 = st.selectbox("Educational Level", educational_levels)

    # Status selection
    status_options = ["Please choose", "Single", "Married", "Divorced", "Separated", "Widowed"]
    st.session_state.status_step1 = st.radio("Status", status_options, index=0)

    # Validation check before proceeding to Step 2
    if st.button("Next"):
        if (st.session_state.gender_step1 == "Select" or st.session_state.age_step1 == 0 or
            st.session_state.weight_step1 == 0.0 or st.session_state.height_step1 == 0.0 or
            st.session_state.education_step1 == "" or st.session_state.status_step1 == "Please choose"):
            st.warning("Please fill out all the fields before proceeding.")
        else:
            next_step()

# Step 2 - Risky Behavior
elif st.session_state["step"] == 2:
    st.title("CRA LungCheck")
    st.markdown('<div class="subtitle-text">Please enter your information for pre-screening Restrictive defect</div>', unsafe_allow_html=True)
    st.write("****Step 2****")
    st.header("Risky Behavior")

    # Current smoker (required)
    st.session_state.current_smoker_step2 = st.radio("**Current smoker**", ["Please choose", "Yes", "No"], index=0)

    # Display fields based on user selections
    if st.session_state.current_smoker_step2 == "Yes":
        st.session_state.smoked_per_day_step2 = st.number_input("Smoked per day", min_value=1, max_value=100, value=1)
    else:
        st.session_state.smoked_per_day_step2 = 0  # Default value if not smoking

    # Cigarette Type (required)
    st.session_state.cigarette_type_step2 = st.radio("Cigarette Type", ["Please choose", "Never smoked", "Filtered", "Non-filtered", "Both"], index=0)

    # Lung Inhale Smoking (required)
    st.session_state.lung_inhale_step2 = st.radio("Lung Inhale Smoking", ["Please choose", "Never smoked", "Inhaled deeply", "Not inhaled deeply", "Sometimes inhaled deeply"], index=0)

    # Alcohol section (required)
    st.session_state.alcohol_step2 = st.radio("**Alcohol**", ["Please choose", "Never drank before", "Used to drink but quit", "Still drinking"], index=0)

    # Drinking Frequency (only if still drinking)
    if st.session_state.alcohol_step2 == "Still drinking" or st.session_state.alcohol_step2 == "Used to drink but quit":
        st.session_state.drinking_frequency_step2 = st.radio("Drinking Frequency", ["Please choose", "Drink a little", "Once a week", "2-3 times a week", "4 times or more per week"], index=0)
    else:
        st.session_state.drinking_frequency_step2 = "Not Applicable"

    # Navigation buttons with validation
    col1, col2 = st.columns(2)
    with col2:
        if (st.session_state.current_smoker_step2 != "Please choose" and
            st.session_state.cigarette_type_step2 != "Please choose" and
            st.session_state.lung_inhale_step2 != "Please choose" and
            st.session_state.alcohol_step2 != "Please choose" and
            (st.session_state.alcohol_step2 not in ["Still drinking", "Used to drink but quit"] or
             st.session_state.drinking_frequency_step2 != "Please choose")):
            if st.button("Next"):
                next_step()
        else:
            st.warning("Please fill in all required information before proceeding.")
    with col1:
        if st.button("Back"):
            prev_step()

# Step 3 - Working Information
elif st.session_state["step"] == 3:
    st.title("CRA LungCheck")
    st.markdown('<div class="subtitle-text">Please enter your information for pre-screening Restrictive defect</div>', unsafe_allow_html=True)
    st.write("****Step 3****")
    st.header("Working Information")

    # Fetch data from the API
    try:
        response = requests.get("https://cra-lungcheck-backend.vercel.app/data")
        response.raise_for_status()
        data = response.json()
        latest_pm25 = data[0]["pm25"] if data else None
    except Exception as e:
        st.error(f"Failed to fetch dust level data: {e}")
        latest_pm25 = None

    # Factory Name and Department
    col1, col2 = st.columns(2)
    with col1:
        factory_names = ["Please choose", "Factory A", "Factory B", "Factory C", "Factory D", "Factory E", "Factory F"]
        st.session_state.factory_name_step3 = st.selectbox("Factory Name", factory_names)
    with col2:
        if latest_pm25 is not None:
            st.session_state.dust_level_factory_step3 = st.text_input("Dust Level (Fac.)", value=latest_pm25, disabled=True)
        else:
            st.warning("No dust level data available. Please check the API connection.")
            st.session_state.dust_level_factory_step3 = None

    # Previous Department
    st.session_state.hazardous_exposure_step3 = st.radio("Previous Department", ["Please choose", "Yes", "No"], index=0)

    # Duration Working (Year and Month)
    col5, col6 = st.columns(2)
    with col5:
        st.session_state.working_years_step3 = st.number_input("Duration Working - Years", min_value=0, max_value=50, value=1)
    with col6:
        st.session_state.working_months_step3 = st.number_input("Duration Working - Months", min_value=0, max_value=11, value=0)

    # Additional Working Details
    col7, col8 = st.columns(2)
    with col7:
        st.session_state.working_hours_day_step3 = st.number_input("Working hours per day", min_value=0.0, max_value=24.0, value=0.0)
    with col8:
        st.session_state.working_days_week_step3 = st.number_input("Working days per week", min_value=0, max_value=7, value=0)

    col9, col10 = st.columns(2)
    with col9:
        st.session_state.ot_hours_week_step3 = st.number_input("OT hours per week", min_value=0.0, max_value=168.0, value=0.0)
    with col10:
        st.session_state.break_time_day_step3 = st.number_input("Break Time hours per day", min_value=0.0, max_value=24.0, value=0.0)

    # Sleep Time per day
    st.session_state.sleep_time_day_step3 = st.number_input("Sleep Time hours per day", min_value=0.0, max_value=24.0, value=0.0)

    # Navigation buttons with validation
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            prev_step()
    with col2:
        if (st.session_state.factory_name_step3 != "Please choose" and latest_pm25 is not None and
            st.session_state.hazardous_exposure_step3 != "Please choose" and
            st.session_state.working_years_step3 >= 0 and st.session_state.working_months_step3 >= 0 and
            st.session_state.working_hours_day_step3 >= 0 and st.session_state.working_days_week_step3 > 0 and
            st.session_state.ot_hours_week_step3 >= 0 and st.session_state.break_time_day_step3 >= 0 and
            st.session_state.sleep_time_day_step3 >= 0):
            if st.button("Next"):
                next_step()
        else:
            st.warning("Please fill in all required fields before proceeding.")

# Step 4 - Health Information
elif st.session_state["step"] == 4:
    st.title("CRA LungCheck")
    st.markdown('<div class="subtitle-text">Please enter your information for pre-screening Restrictive defect</div>', unsafe_allow_html=True)
    st.write("****Step 4****")
    st.header("Health Information")

    # Using st.form to avoid automatic updates on each change
    with st.form(key="health_info_form"):
        st.write("***In the past 5 years***")
        st.session_state.tuberculosis_5years = st.radio("Tuberculosis", ["Yes", "No", "Unsure"])
        st.session_state.asthma_5years = st.radio("Asthma", ["Yes", "No", "Unsure"])
        st.session_state.pulmonary_5years = st.radio("Pulmonary TB", ["Yes", "No", "Unsure"])

        st.write("***Current Illness***")
        st.session_state.current_illness = st.radio("Do you have any current illness? (If not, please select No for the next question.)", ["Yes", "No"])
        if st.session_state.current_illness == "Yes":
            st.session_state.asthma_current = st.radio("Asthma", ["Yes", "No"])
            st.session_state.emphysema_current = st.radio("Emphysema", ["Yes", "No"])
            st.session_state.bronchitis_current = st.radio("Bronchitis", ["Yes", "No"])
            st.session_state.sinusitis_current = st.radio("Sinusitis", ["Yes", "No"])
            st.session_state.injury_surgery_current = st.radio("Injury/Surgery", ["Yes", "No"])
            st.session_state.allergies_current = st.radio("Allergies", ["Yes", "No"])
            st.session_state.tuberculosis_current = st.radio("Tuberculosis", ["Yes", "No"])
            st.session_state.heart_disease_current = st.radio("Heart Disease", ["Yes", "No"])
            st.session_state.pneumonia_current = st.radio("Pneumonia", ["Yes", "No"])
            st.session_state.other_current = st.radio("Other", ["Yes", "No"])
        else:
            # Set default values if no current illness
            st.session_state.asthma_current = "No"
            st.session_state.emphysema_current = "No"
            st.session_state.bronchitis_current = "No"
            st.session_state.sinusitis_current = "No"
            st.session_state.injury_surgery_current = "No"
            st.session_state.allergies_current = "No"
            st.session_state.tuberculosis_current = "No"
            st.session_state.heart_disease_current = "No"
            st.session_state.pneumonia_current = "No"
            st.session_state.other_current = "No"

        # Submit button inside the form
        submitted = st.form_submit_button("Submit")
        if submitted:
            next_step()  # Move to the next step only after submitting the form

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            prev_step()

# Step 5 - Analysis in progress
elif st.session_state["step"] == 5:
    # Background video setup
    background_video_url = "https://www.dropbox.com/scl/fi/64srq2nf8kx9pajncsj6s/CRA-LUNGCHECK.mp4?rlkey=5r792fexbzhr4s8nj16qe94t9&st=n0q49dq6&raw=1"

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

    import random

    # Initialize session state timer
    if "start_time" not in st.session_state:
        st.session_state["start_time"] = time.time()
        # Generate a random value and store it
        st.session_state["random_value"] = random.randint(0, 2)

    # Calculate elapsed time
    elapsed_time = time.time() - st.session_state["start_time"]

    # Display a progress bar or message
    st.write("Please wait... Redirecting to the next page in 5 seconds.")
    st.progress(min(int(elapsed_time / 5 * 100), 100))

    # Automatically move to the next step after 5 seconds
    if elapsed_time > 5:
        st.session_state["step"] = 6  # Move to the next step
        st.session_state.pop("start_time")  # Reset the timer
        st.rerun()  # Force the app to rerun
    else:
        time.sleep(0.1)  # Short sleep to prevent rapid looping
        st.rerun()  # Force the app to rerun

# Step 6 - Display Image Based on Random Value and Collect Data
elif st.session_state["step"] == 6:

    import pandas as pd
    import os

    # Collect all data from st.session_state into variables
    gender = st.session_state.get('gender_step1', '')
    age = st.session_state.get('age_step1', '')
    weight = st.session_state.get('weight_step1', '')
    height = st.session_state.get('height_step1', '')
    education = st.session_state.get('education_step1', '')
    status = st.session_state.get('status_step1', '')

    current_smoker = st.session_state.get('current_smoker_step2', '')
    smoked_per_day = st.session_state.get('smoked_per_day_step2', '')
    cigarette_type = st.session_state.get('cigarette_type_step2', '')
    lung_inhale = st.session_state.get('lung_inhale_step2', '')
    alcohol = st.session_state.get('alcohol_step2', '')
    drinking_frequency = st.session_state.get('drinking_frequency_step2', '')

    factory_name = st.session_state.get('factory_name_step3', '')
    dust_level_factory = st.session_state.get('dust_level_factory_step3', '')
    hazardous_exposure = st.session_state.get('hazardous_exposure_step3', '')
    working_years = st.session_state.get('working_years_step3', '')
    working_months = st.session_state.get('working_months_step3', '')
    working_hours_per_day = st.session_state.get('working_hours_day_step3', '')
    working_days_per_week = st.session_state.get('working_days_week_step3', '')
    ot_hours_per_week = st.session_state.get('ot_hours_week_step3', '')
    break_time_per_day = st.session_state.get('break_time_day_step3', '')
    sleep_time_per_day = st.session_state.get('sleep_time_day_step3', '')

    tuberculosis_5years = st.session_state.get('tuberculosis_5years', '')
    asthma_5years = st.session_state.get('asthma_5years', '')
    pulmonary_5years = st.session_state.get('pulmonary_5years', '')
    current_illness = st.session_state.get('current_illness', '')

    # For current illnesses, check if they exist in session_state
    asthma_current = st.session_state.get('asthma_current', '')
    emphysema_current = st.session_state.get('emphysema_current', '')
    bronchitis_current = st.session_state.get('bronchitis_current_illness', '')
    sinusitis_current = st.session_state.get('sinusitis_current_illness', '')
    injury_surgery_current = st.session_state.get('injury_surgery_current_illness', '')
    allergies_current = st.session_state.get('allergies_current_illness', '')
    tuberculosis_current = st.session_state.get('tuberculosis_current_illness', '')
    heart_disease_current = st.session_state.get('heart_current_illness', '')
    pneumonia_current = st.session_state.get('pneumonia_current_illness', '')
    other_current = st.session_state.get('other_current_illness', '')

    # Create a flat dictionary to hold all the data
    user_data = {
        "Sex": gender,
        "Age_group": age,
        "weight": weight,
        "height": height,
        "Education": education,
        "Marital_status": status,
        # "Smoking_current": current_smoker,
        "Smoking_per_day": smoked_per_day,
        "Smoking_type": cigarette_type,
        # "Lung Inhale Smoking": lung_inhale,
        # "Drink_history": alcohol,
        "Drink_times": drinking_frequency,
        "Factory_number": factory_name,
        "Dust_level_mean": dust_level_factory,
        "Previous_sector_history": hazardous_exposure,
        # "Working Years": working_years,
        "Work_months": working_months,
        "Average_work_hour_per_day": working_hours_per_day,
        "Working_day_per_week": working_days_per_week,
        "OT_hour_per_week": ot_hours_per_week,
        "Break_hour_per_day": break_time_per_day,
        "Sleep_hour_per_day": sleep_time_per_day,
        "TB_history": tuberculosis_5years,
        "Asthma_history": asthma_5years,
        "Other_chest_disease": pulmonary_5years,
        "Prevalence_disease": current_illness,
        "Asthma": asthma_current,
        "Emphysema": emphysema_current,
        # "Bronchitis": bronchitis_current,
        "Sinusitis": sinusitis_current,
        "Injury or surgery in the thorax": injury_surgery_current,
        "Allergy": allergies_current,
        "TB": tuberculosis_current,
        "Heart disease": heart_disease_current,
        "Pneumonia": pneumonia_current,
        "Other lung disease": other_current,
    }


    # Convert the user_data dictionary into a DataFrame
    user_df = pd.DataFrame([user_data])

    loaded_best_pipeline = load_model('best')

    # user_df = pd.read_csv('user_data.csv')
    reference_df = pd.read_csv('df_select.csv')

    # Transform the data
    transformed_df = transform_user_data(user_df, reference_df)

    predictions = predict_model(loaded_best_pipeline, data = transformed_df)
    result = predictions["prediction_label"].values[0]
    if factory_name == "Factory E":
        result = 2
    elif factory_name == "Factory F":
        result = 3
    else:
        result = result

    # Define the CSV file name
    csv_file = "user_data.csv"

    # Check if the CSV file exists
    if os.path.isfile(csv_file):
        # If it exists, append without writing the header
        user_df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        # If it does not exist, write the data with the header
        user_df.to_csv(csv_file, mode='w', header=True, index=False)


    # Define image URLs based on the random value
    image_urls = {
        1: "https://www.dropbox.com/scl/fi/pomdtvnlzsuacmzmce75m/Normal.png?rlkey=5cqznzleogpusgc30lyp6qdmc&st=ghxcowil&raw=1",
        2: "https://www.dropbox.com/scl/fi/3keh11prpokpytv9s1a06/Mild.png?rlkey=qxnlunz5yc2h01miwieq0wgro&st=5755o5l2&raw=1",
        3: "https://www.dropbox.com/scl/fi/g18t6ujd2sbv63rqn3xz0/High.png?rlkey=4l8118z19hqo6wvyl95uyqtc0&st=yjbld74w&raw=1",
    }

    # Get the background image URL based on the random value
    background_image_url2 = image_urls[result]

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
            z-index: 10;
            color: white;
            border: none;
            padding: 10px 10px;
            font-size: 16px;
            border-radius: 5px;
        }}
        </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)


    # Navigation button to reset state
    if st.button("Return to Home"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_set_query_params()