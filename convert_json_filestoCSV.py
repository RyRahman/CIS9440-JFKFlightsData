import pandas as pd

input_path = r"C:\Users\Rrahm\Downloads\Combined_JFK_Flights_Info.json"
output_path = r"C:\Users\Rrahm\Downloads\Combined_JFK_Flights_Info.csv"

df = pd.read_json(input_path)
df.to_csv(output_path, index=False)

print("Done. CSV saved.")
