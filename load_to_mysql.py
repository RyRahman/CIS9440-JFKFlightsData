import mysql.connector
import csv

conn = mysql.connector.connect(
    host='35.xxx.xxx.xxx',
    user='root',
    password='mypassword',
    database='jfk_flights'
)

cursor = conn.cursor()

csv_file = 'C:/Users/Rrahm/Downloads/Combined_JFK_Flights.csv'

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    count = 0

    for row in reader:
        query = """
        INSERT INTO staging_flights (
            flight_date, flight_status, departure_airport, departure_iata,
            departure_icao, arrival_airport, arrival_iata, arrival_icao,
            airline_name, airline_iata, airline_icao, flight_number,
            aircraft_registration, aircraft_iata, aircraft_icao,
            scheduled_departure, estimated_departure, actual_departure,
            scheduled_arrival, estimated_arrival, actual_arrival,
            departure_delay, arrival_delay
        ) VALUES (
            %(flight_date)s, %(flight_status)s, %(departure_airport)s, %(departure_iata)s,
            %(departure_icao)s, %(arrival_airport)s, %(arrival_iata)s, %(arrival_icao)s,
            %(airline_name)s, %(airline_iata)s, %(airline_icao)s, %(flight_number)s,
            %(aircraft_registration)s, %(aircraft_iata)s, %(aircraft_icao)s,
            %(scheduled_departure)s, %(estimated_departure)s, %(actual_departure)s,
            %(scheduled_arrival)s, %(estimated_arrival)s, %(actual_arrival)s,
            %(departure_delay)s, %(arrival_delay)s
        );
        """
        cursor.execute(query, row)
        count += 1

        if count % 1000 == 0:
            print(count, "rows inserted...")
            conn.commit()

conn.commit()
cursor.close()
conn.close()

print("Done. Loaded:", count)
