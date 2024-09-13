import os
import shutil
import random
from collections import OrderedDict

script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, "reveal_test_data")
output_path = os.path.join(script_dir, "reveal_balanced")
reveal_files = os.listdir(input_path)

vul_files = [f for f in reveal_files if f.endswith("_1.c")]
non_vul_files = [f for f in reveal_files if f.endswith("_0.c")]

b_vul_files = random.sample(vul_files, 300)
b_non_vul_files = random.sample(non_vul_files, 1500)

for file in b_vul_files:
    source_path = os.path.join(input_path, file)
    destination_path = os.path.join(output_path, file)
    try:
        shutil.copy(source_path, destination_path)
    except Exception as e:
        print(f"Error copying {file}: {e}")
        continue

for file in b_non_vul_files:
    source_path = os.path.join(input_path, file)
    destination_path = os.path.join(output_path, file)
    try:
        shutil.copy(source_path, destination_path)
    except Exception as e:
        print(f"Error copying {file}: {e}")
        continue

print(len(os.listdir(output_path)))