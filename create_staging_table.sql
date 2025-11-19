CREATE DATABASE jfk_flights;
USE jfk_flights;

CREATE TABLE staging_flights (
    flight_date VARCHAR(50),
    flight_status VARCHAR(50),
    departure_airport VARCHAR(100),
    departure_iata VARCHAR(10),
    departure_icao VARCHAR(10),
    arrival_airport VARCHAR(100),
    arrival_iata VARCHAR(10),
    arrival_icao VARCHAR(10),
    airline_name VARCHAR(100),
    airline_iata VARCHAR(10),
    airline_icao VARCHAR(10),
    flight_number VARCHAR(20),
    aircraft_registration VARCHAR(50),
    aircraft_iata VARCHAR(50),
    aircraft_icao VARCHAR(50),
    scheduled_departure VARCHAR(50),
    estimated_departure VARCHAR(50),
    actual_departure VARCHAR(50),
    scheduled_arrival VARCHAR(50),
    estimated_arrival VARCHAR(50),
    actual_arrival VARCHAR(50),
    departure_delay INT,
    arrival_delay INT
);
