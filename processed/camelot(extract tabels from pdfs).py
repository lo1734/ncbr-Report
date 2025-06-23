import os
import camelot

for year in ["2021", "2022"]:
    pdf_folder = f"/Users/lohith/Desktop/ncbr-Report/raw/{year}"
    output_folder = f"{year}_processed"
    os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf") and "Table" in file:
        file_path=os.path.join(pdf_folder,file)
        print(f"processing: {file_path}...")
        try:
            tables=camelot.read_pdf(file_path,pages="all",flavor='stream')
            if tables.n == 0:
                continue;

            for i, table in enumerate(tables):
                out_file=os.path.join(output_folder, f"{file[:-4]}_table_{i+1}.csv")
                table.to_csv(out_file)
        except Exception as e:
            print(f"Failed to process {file}:{e}")