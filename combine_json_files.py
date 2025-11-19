import json
import os

folder_path = "D://RRahman/Downloads"
all_data = []

for file in os.listdir(folder_path):
    if file.endswith(".json"):
        with open(os.path.join(folder_path, file), "r") as f:
            data = json.load(f)
            all_data.extend(data)

with open("merged.json", "w") as f:
    json.dump(all_data, f, indent=2)

print("Merged", len(all_data), "records.")
