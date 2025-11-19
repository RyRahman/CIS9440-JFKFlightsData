CIS9440-JFKFlightsData/
│
├── README.md
│
├── data_sources/
│   ├── data_source_links.txt
│   └── data_dictionary_link.txt
│
├── raw_data/
│   ├── sample_json_structure.json
│   ├── example_csv_sample.csv
│   └── (empty or ignored if files stored in Cloud Storage)
│
├── scripts/
│   ├── sourcing/
│   │   ├── download_from_gcs.sh
│   │   ├── combine_json_files.py
│   │   └── convert_json_to_csv.py
│   │
│   ├── loading/
│   │   ├── load_to_mysql.py
│   │   └── verify_load.py
│   │
│   └── utils/
│       └── helpers.py   (optional)
│
├── sql/
│   ├── staging/
│   │   └── create_staging_table.sql
│   │
│   ├── warehouse/
│   │   ├── create_dim_airline.sql
│   │   ├── create_dim_aircraft.sql
│   │   ├── create_dim_airport.sql
│   │   ├── create_dim_date.sql
│   │   ├── create_fact_flight.sql
│   │   └── load_fact_and_dims.sql
│   │
│   └── validation/
│       └── quality_checks.sql
│
├── modeling/
│   ├── ERD.png
│   ├── star_schema.pdf
│   └── modeling_notes.md
│
└── .gitignore
