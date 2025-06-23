import os
import camelot

pdf_folder="/Users/lohith/Desktop/ncbr-Report/raw/2021"
output_folder="2021_processed"
os.makedirs(output_folder,exist_ok=True)

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf") and "Table" in file:
        file_path=os.path.join(pdf_folder,file)
        print(f"processing: {file_path}")
        try:
            tables=camelot.read_pdf(file_path,pages="all")
            for i, table in enumerate(tables):
                out_file=os.path.join(output_folder, f"{file[:-4]}_table_{i+1}.csv")
                table.to_csv(out_file)
        except Exception as e:
            print(f"Failed to process {file}:{e}")