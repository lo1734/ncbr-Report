import os
import pandas as pd
import re

csv_folder = "../processed/processed_Incidence_and_Rate_of_Suicides_yearly/State_dir"
cleaned_folder = "../cleaner/cleaned_data"
os.makedirs(cleaned_folder, exist_ok=True)

all_files = [f for f in os.listdir(csv_folder) if f.endswith(".csv") and 'Incidence' in f]
combined_df = []

for file in all_files:
    print(f"Processing: {file}")

    year_match = re.search(r"(\d{4})", file)
    if not year_match:
        print(f"Skipping file (no year found): {file}")
        continue
    year = int(year_match.group(1))

    df = pd.read_csv(os.path.join(csv_folder, file))
    df.dropna(how='all', inplace=True)

    # Slice rows before UNION TERRITORIES
    stop_index = df[df.iloc[:, 1].astype(str).str.contains("UNION TERRITORIES", case=False, na=False)].index
    if not stop_index.empty:
        df = df.loc[:stop_index[0] - 1]

    # Drop TOTAL (STATES) row if present
    df = df[~df.iloc[:, 1].astype(str).str.contains("TOTAL", case=False, na=False)]

    # Keep only rows with a numeric serial number
    df = df[df.iloc[:, 0].astype(str).str.match(r"^\d+$")]

    # Standardize column names
    df.columns = ["Serial No", "Area", "Number of Suicides", "% Share", "Population (Lakh)", "Rate of Suicides"]

    # Add metadata and rename columns
    df["Year"] = year
    df.rename(columns={"Area": "State"}, inplace=True)

    # Final column order
    final_columns = ["Year", "State", "Number of Suicides", "% Share", "Population (Lakh)", "Rate of Suicides"]
    df = df[final_columns]

    combined_df.append(df)

# Combine all cleaned DataFrames
final_df = pd.concat(combined_df, ignore_index=True)

# Save to CSV
output_path = os.path.join(cleaned_folder, "NCRB_Statewise_Combined_Cleaned.csv")
final_df.to_csv(output_path, index=False)

print(f"\n All files processed and saved to: {output_path}")



