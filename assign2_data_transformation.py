
# DATA PROCESSING
import os
import json
import pandas as pd


# 1. LOAD RAW JSON FILES

folder = r"C:\Users\Rrahm\Downloads\raw-json\raw_json"
all_rows = []

print("Files in folder:", os.listdir(folder))

for file in os.listdir(folder):
    if file.lower().endswith(".json"):
        full_path = os.path.join(folder, file)
        print("Loading:", full_path)

        with open(full_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, list):
                all_rows.extend(data)
            elif isinstance(data, dict) and "data" in data:
                all_rows.extend(data["data"])
            else:
                print("Skipping unexpected JSON structure:", file)

df = pd.DataFrame(all_rows)
print("Loaded rows:", len(df))
print("INITIAL COLUMNS:", df.columns.tolist())


# 2. FLATTEN NESTED STRUCTURES

# Departure fields
df["departure_iata"] = df["departure"].apply(lambda x: x.get("iata") if isinstance(x, dict) else None)
df["departure_scheduled"] = df["departure"].apply(lambda x: x.get("scheduled") if isinstance(x, dict) else None)
df["departure_estimated"] = df["departure"].apply(lambda x: x.get("estimated") if isinstance(x, dict) else None)
df["departure_actual"] = df["departure"].apply(lambda x: x.get("actual") if isinstance(x, dict) else None)

# Arrival fields
df["arrival_iata"] = df["arrival"].apply(lambda x: x.get("iata") if isinstance(x, dict) else None)
df["arrival_scheduled"] = df["arrival"].apply(lambda x: x.get("scheduled") if isinstance(x, dict) else None)
df["arrival_estimated"] = df["arrival"].apply(lambda x: x.get("estimated") if isinstance(x, dict) else None)
df["arrival_actual"] = df["arrival"].apply(lambda x: x.get("actual") if isinstance(x, dict) else None)

# Airline fields
df["airline_name"] = df["airline"].apply(lambda x: x.get("name") if isinstance(x, dict) else None)
df["airline_iata"] = df["airline"].apply(lambda x: x.get("iata") if isinstance(x, dict) else None)
df["airline_icao"] = df["airline"].apply(lambda x: x.get("icao") if isinstance(x, dict) else None)

# Flight fields
df["flight_number"] = df["flight"].apply(lambda x: x.get("number") if isinstance(x, dict) else None)
df["codeshare"] = df["flight"].apply(lambda x: x.get("codeshare") if isinstance(x, dict) else None)

# Aircraft fields
df["aircraft_registration"] = df["aircraft"].apply(lambda x: x.get("registration") if isinstance(x, dict) else None)
df["aircraft_iata"] = df["aircraft"].apply(lambda x: x.get("iata") if isinstance(x, dict) else None)
df["aircraft_icao"] = df["aircraft"].apply(lambda x: x.get("icao") if isinstance(x, dict) else None)

print("Flattened Columns:", df.columns.tolist())


# 3. DROP THE ORIGINAL NESTED DICT COLUMNS

df = df.drop(columns=["departure", "arrival", "airline", "flight", "aircraft", "live"])


# 4. CONVERT TIMESTAMP FIELDS

timestamp_cols = [
    "departure_scheduled",
    "departure_estimated",
    "departure_actual",
    "arrival_scheduled",
    "arrival_estimated",
    "arrival_actual"
]

for col in timestamp_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce")


# 5. EXTRACT DATE PARTS

df["year"] = df["departure_scheduled"].dt.year
df["quarter"] = df["departure_scheduled"].dt.quarter
df["month"] = df["departure_scheduled"].dt.month
df["day"] = df["departure_scheduled"].dt.day
df["hour"] = df["departure_scheduled"].dt.hour
df["minute"] = df["departure_scheduled"].dt.minute


# 6. REMOVE DUPLICATES + NULL FILTERS

df.drop_duplicates(inplace=True)
df = df.dropna(subset=["airline_iata", "departure_iata", "arrival_iata"])


# 7. ADD REQUIRED DELAY FIELDS

df["is_delayed"] = (df["departure_actual"] > df["departure_scheduled"]).astype(int)

df["delay_minutes"] = (
    (df["departure_actual"] - df["departure_scheduled"])
    .dt.total_seconds() / 60
).fillna(0)

df["total_delay"] = df["delay_minutes"]
df["is_codeshare"] = df["codeshare"].notna().astype(int)


# 8. SAVE CLEANED FILE

output_path = r"C:\Users\Rrahm\Downloads\raw-json\clean_flights.csv"
df.to_csv(output_path, index=False)

print("Saved transformed file to:", output_path)
print("Final Columns:", df.columns.tolist())
