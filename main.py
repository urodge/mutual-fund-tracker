import pandas as pd
import os

# File path
file_path = r"C:\Users\lenovo\Downloads\ZN250 - Monthly Portfolio September 2024.xlsx"

# Check if the file exists
if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}")
else:
    try:
        # Load the data and skip metadata rows
        df = pd.read_excel(file_path, skiprows=6)  # Adjust 'skiprows' as necessary based on file structure

        # Debug: Print loaded columns to inspect structure
        print("Preview of loaded data:")
        print(df.head())

        # Rename columns to expected names
        column_mapping = {
            'EQUITY & EQUITY RELATED': 'Fund Name',
            'Unnamed: 6': 'Allocation',
            # Add other mappings as needed
        }
        df.rename(columns=column_mapping, inplace=True)

        # Drop rows where required fields are missing
        df.dropna(subset=['Fund Name', 'Allocation'], inplace=True)

        # Convert Allocation to numeric and handle potential errors
        df['Allocation'] = pd.to_numeric(df['Allocation'], errors='coerce')

        # Define the function to track fund changes
        def track_fund_changes(fund_name, start_date, end_date):
            # Filter data by fund name and date range
            filtered_df = df[df['Fund Name'] == fund_name]

            if filtered_df.empty:
                return {"Error": "No data found for the specified fund name"}

            # Generate insights (dummy Date handling, as no Date is in the file)
            insights = {
                "Total Allocation": filtered_df['Allocation'].sum(),
                "Fund Details": filtered_df[['Fund Name', 'Allocation']].to_dict(orient='records')
            }
            return insights

        # Example usage
        fund_name = "HDFC Bank Limited"
        results = track_fund_changes(fund_name, None, None)  # Date handling omitted due to lack of column
        print("Fund Allocation Insights:")
        print(results)

    except ValueError as ve:
        print(f"Data Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

