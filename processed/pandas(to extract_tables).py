import os
import pandas as pd
import pdfplumber

# List of years to process
for year in ["2021", "2022"]:
    pdf_folder = f"/Users/lohith/Desktop/ncbr-Report/raw/{year}"
    output_folder = f"{year}_processed"
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
                            # Filter out rows where all cells are empty or whitespace
                            filtered_rows = [row for row in table[1:] if any(cell and str(cell).strip() for cell in row)]
                            if filtered_rows:
                                df = pd.DataFrame(filtered_rows, columns=table[0])
                                output_csv = os.path.join(output_folder, f"{file[:-4]}_page{i}.csv")
                                df.to_csv(output_csv, index=False)

            except Exception as e:
                print(f"Error processing {file} in {year}: {e}")