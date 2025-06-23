import os
import camelot

pdf_folder = "../raw/Incidence_and_Rate_of_Suicides_yearly"
output_folder = "processed_Incidence_and_Rate_of_Suicides_yearly"
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(pdf_folder):
    file_path = os.path.join(pdf_folder, file)
    print(f"processing: {file_path}...")
    try:
        tables = camelot.read_pdf(file_path, pages="all", flavor='stream')
        if tables.n == 0:
            continue;

        for i, table in enumerate(tables):
            out_file = os.path.join(output_folder, f"{file[:-4]}_table_{i + 1}.csv")
            table.to_csv(out_file)
    except Exception as e:
        print(f"Failed to process {file}:{e}")

