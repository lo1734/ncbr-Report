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

    # Extract year from filename
    year_match = re.search(r"(\d{4})", file)
    if not year_match:
        print(f"Skipping file (no year found): {file}")
        continue
    year = int(year_match.group(1))

    df = pd.read_csv(os.path.join(csv_folder, file))
    df.dropna(how='all', inplace=True)

    # Remove everything after "UNION TERRITORIES"
    stop_index = df[df.iloc[:, 1].astype(str).str.contains("UNION TERRITORIES", case=False, na=False)].index
    if not stop_index.empty:
        df = df.loc[:stop_index[0] - 1]

    # Drop "TOTAL" rows
    df = df[~df.iloc[:, 1].astype(str).str.contains("TOTAL", case=False, na=False)]

    # Keep only rows with numeric serial numbers
    df = df[df.iloc[:, 0].astype(str).str.match(r"^\d+$")]

    # Assign column names
    df.columns = ["Serial No", "Area", "Number of Suicides", "% Share", "Population (Lakh)", "Rate of Suicides"]

    # Add year column
    df["Year"] = year

    # Rename "Area" to "State"
    df.rename(columns={"Area": "State"}, inplace=True)

    # Reorder columns
    df = df[["Year", "State", "Number of Suicides", "% Share", "Population (Lakh)", "Rate of Suicides"]]

    # Convert data types
    df["Number of Suicides"] = pd.to_numeric(df["Number of Suicides"], errors='coerce').fillna(0).astype(int)
    df["% Share"] = pd.to_numeric(df["% Share"], errors='coerce').fillna(0.0).astype(float)
    df["Population (Lakh)"] = pd.to_numeric(df["Population (Lakh)"], errors='coerce').fillna(0.0).astype(float)
    df["Rate of Suicides"] = pd.to_numeric(df["Rate of Suicides"], errors='coerce').fillna(0.0).astype(float)

    combined_df.append(df)

# Combine all years
final_df = pd.concat(combined_df, ignore_index=True)

# Convert to tidy format
df_long = pd.melt(
    final_df,
    id_vars=["Year", "State"],
    value_vars=["Number of Suicides", "% Share", "Population (Lakh)", "Rate of Suicides"],
    var_name="Category",
    value_name="Value"
)

# Define unit mappings
unit_map = {
    "Number of Suicides": "Persons",
    "% Share": "Percent",
    "Population (Lakh)": "Lakh",
    "Rate of Suicides": "Rate"
}

df_long["Unit"] = df_long["Category"].map(unit_map)

# Reorder columns
df_long = df_long[["Year", "State", "Category", "Value", "Unit"]]

# Save to CSV
output_path = os.path.join(cleaned_folder, "NCRB_Statewise_Tidy_Cleaned.csv")
df_long.to_csv(output_path, index=False)

print(f"\n All files processed and saved to: {output_path}")
