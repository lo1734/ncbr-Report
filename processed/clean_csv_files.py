import os
import pandas as pd
import glob

# Path to the folder containing CSV files
csv_folder = "processed_Incidence_and_Rate_of_Suicides_yearly"

# Get all CSV files in the folder
csv_files = glob.glob(os.path.join(csv_folder, "*.csv"))

for file_path in csv_files:
    print(f"Cleaning: {file_path}")
    
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Remove rows where all columns are empty or NaN
        df = df.dropna(how='all')
        
        # Remove rows where all columns are empty strings or whitespace
        df = df[~df.apply(lambda row: row.astype(str).str.strip().eq('').all(), axis=1)]
        
        # Remove rows that are just commas (empty data)
        df = df[~df.apply(lambda row: row.astype(str).str.strip().eq('').sum() >= len(row) - 1, axis=1)]
        
        # Handle header issues - if first column contains "Sl." or similar, merge with proper header
        if len(df) > 0 and 'SI.No' in df.columns:
            # Check if there are any rows with just "Sl." or similar in the first column
            sl_rows = df[df.iloc[:, 0].astype(str).str.contains('Sl\.', na=False)]
            if not sl_rows.empty:
                # Remove these rows
                df = df[~df.iloc[:, 0].astype(str).str.contains('Sl\.', na=False)]
        
        # Remove notes at the bottom (rows containing "Note:" or similar)
        df = df[~df.apply(lambda row: row.astype(str).str.contains('Note:', na=False).any(), axis=1)]
        
        # Reset index after cleaning
        df = df.reset_index(drop=True)
        
        # Save the cleaned file back to the same location
        df.to_csv(file_path, index=False)
        print(f"Cleaned and saved: {file_path}")
        
    except Exception as e:
        print(f"Error cleaning {file_path}: {e}")

print("CSV cleaning completed!") 