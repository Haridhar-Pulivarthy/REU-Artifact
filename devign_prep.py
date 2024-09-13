import os
import json

LLM = "VGX"
DATASET = "CVE-LLM"
# TYPE = "Single-line"

script_dir = os.path.dirname(__file__)

# Function for extracting the contents of a file as a string.
def file_to_str(file_path):
    try:
        with open(file_path, 'r', encoding = "utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {file_path}\n{e}")
        return None
    
def process_generated_vul_data():
    # Get the path to the LLM/baseline-generated files.
    generated_dataset_path = os.path.join(script_dir, LLM, DATASET)
    generated_dataset_file_names = os.listdir(generated_dataset_path)
    generated_dataset_list = []
    i = 0 # Counter for tracking the number of files processed.

    for file in generated_dataset_file_names:
        file_path = os.path.join(generated_dataset_path, file)
        data = {}
        data["project"] = f"{LLM}_{DATASET}"
        i += 1
        data["commit_id"] = f"{i}"
        data["file_name"] = file
        data["target"] = 1 # 0 means non-vulnerable, 1 means vulnerable.
        data["func"] = file_to_str(file_path)
        if data["func"] != None and data["func"] != "":
            generated_dataset_list.append(data)
    return generated_dataset_list

generated_dataset_list = process_generated_vul_data()

output_path = os.path.join(script_dir, "Devign_Data", f"{LLM}_{DATASET}.json")
with open(output_path, 'w') as output_file:
    json.dump(generated_dataset_list, output_file, indent=4)