import pandas as pd

def transform_user_data(user_df, reference_df):
    """
    Transforms a user DataFrame based on predefined mappings and aligns it with a reference DataFrame structure.

    Parameters:
        user_df (pd.DataFrame): The user data DataFrame.
        reference_df (pd.DataFrame): The reference DataFrame defining the desired structure.

    Returns:
        pd.DataFrame: Transformed DataFrame aligned with the reference structure.
    """
    # Define mappings for categorical variables
    mappings = {
        "Sex": {"Male": 1, "Female": 2},
        "Education": {
            "Illiterate": 0,
            "Primary school": 1,
            "Junior high school": 2,
            "Senior high school": 3,
            "College or above": 4,
        },
        "Marital_status": {"Single": 1, "Married": 2, "Divorced": 3, "Widowed": 4},
        "Smoking_type": {"Not Applicable": 0, "Filtered": 1, "Unfiltered": 2, "Electronic": 3},
        "Prevalence_disease": {"Yes": 1, "No": 2},
        "Asthma": {"Yes": 1, "No": 2},
        "Emphysema": {"Yes": 1, "No": 2},
        "Sinusitis": {"Yes": 1, "No": 2},
        "Injury or surgery in the thorax": {"Yes": 1, "No": 2},
        "Allergy": {"Yes": 1, "No": 2},
        "TB": {"Yes": 1, "No": 2},
        "Heart disease": {"Yes": 1, "No": 2},
        "Pneumonia": {"Yes": 1, "No": 2},
        "Other lung disease": {"Yes": 1, "No": 2},
        "TB_history": {"Yes": 1, "No": 2},
        "Asthma_history": {"Yes": 1, "No": 2},
        "Other_chest_disease": {"Yes": 1, "No": 2},
        "Factory_number": {"Factory A": 1, "Factory B": 2, "Factory C": 3},
        "Drink_times": {"Not Applicable": 0},  # Add mapping for "Not Applicable"
        "Previous_sector_history": {"Yes": 1, "No": 0},  # Map "Yes" and "No"
    }

    # Create a copy of user_df for transformation
    transformed_data = user_df.copy()

    # Apply the mappings to convert categorical data to numerical
    for column, mapping in mappings.items():
        if column in transformed_data.columns:
            transformed_data[column] = (
                transformed_data[column]
                .map(mapping)
                .fillna(0)  # Handle unmapped values by assigning a default (e.g., 0)
            )

    # Check for remaining unmapped or problematic columns
    problematic_columns = [
        col
        for col in transformed_data.columns
        if transformed_data[col].dtype == object or transformed_data[col].isnull().any()
    ]
    if problematic_columns:
        print(f"Problematic columns with unmapped or unexpected values: {problematic_columns}")
        for col in problematic_columns:
            print(f"Unique values in {col}: {transformed_data[col].unique()}")

    # Align the transformed data with the reference DataFrame structure
    common_columns = set(transformed_data.columns).intersection(set(reference_df.columns))
    transformed_data = transformed_data[list(common_columns)]  # Preserve column order
    dtype_mapping = {col: reference_df[col].dtype for col in common_columns}

    # Attempt to cast data types to match the reference DataFrame
    try:
        transformed_data = transformed_data.astype(dtype_mapping)
    except ValueError as e:
        # Identify problematic columns and print for debugging
        problematic_columns = [
            col for col in transformed_data.columns if transformed_data[col].dtype != dtype_mapping[col]
        ]
        print(f"Data type mismatch in columns: {problematic_columns}")
        print(e)

    return transformed_data
