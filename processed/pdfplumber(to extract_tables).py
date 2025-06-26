import os
import pandas as pd
import pdfplumber

# List of years to process
pdf_folder = f"../raw/Incidence_and_Rate_of_Suicides_yearly"
output_folder = "processed_Incidence_and_Rate_of_Suicides_yearly"
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf") and "Table" in file:
        file_path = os.path.join(pdf_folder, file)
        print(f"processing: {file} in {year}")

        try:
            with pdfplumber.open(file_path) as pdf:
                for i, page in enumerate(pdf.pages, start=1):
                    table = page.extract_table()
                    if table:
                        # Check if the first two rows are header rows (all strings, not data)
                        header_rows = table[:2]
                        # Heuristic: if both rows are mostly non-empty and contain strings, treat as split header
                        if len(header_rows) > 1 and all(isinstance(cell, str) for cell in header_rows[0]) and all(
                                isinstance(cell, str) for cell in header_rows[1]):
                            merged_header = [
                                (str(cell1).strip() + ' ' + str(cell2).strip()).strip() if cell2 else str(cell1).strip()
                                for cell1, cell2 in zip(header_rows[0], header_rows[1])
                            ]
                            data_rows = table[2:]
                        else:
                            merged_header = table[0]
                            data_rows = table[1:]

                        # Filter out rows where all cells are empty or whitespace
                        filtered_rows = [row for row in data_rows if any(cell and str(cell).strip() for cell in row)]
                        if filtered_rows:
                            df = pd.DataFrame(filtered_rows, columns=merged_header)
                            output_csv = os.path.join(output_folder, f"{file[:-4]}_page{i}.csv")
                            df.to_csv(output_csv, index=False)

        except Exception as e:
            print(f"Error processing {file} in {year}: {e}")