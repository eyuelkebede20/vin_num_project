import sqlite3
import csv
import os

def load_csv_to_db(db_path, wmi_csv, vds_csv):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if os.path.exists(wmi_csv):
        with open(wmi_csv, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                wmi = row.get('WMI')
                manufacturer = row.get('ManufacturerName', row.get('Manufacturer Name', ''))
                country = row.get('Country', '')
                
                if wmi:
                    cursor.execute(
                        "INSERT OR IGNORE INTO wmi_data (wmi, manufacturer, country) VALUES (?, ?, ?)", 
                        (wmi.strip(), manufacturer.strip(), country.strip())
                    )
        print(f"Loaded WMI data from {wmi_csv}")
    else:
        print(f"File not found: {wmi_csv}")

    if os.path.exists(vds_csv):
        with open(vds_csv, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                wmi = row.get('WMI')
                vds = row.get('VDS')
                model = row.get('Model', '')
                engine = row.get('EngineConfiguration', row.get('Engine', ''))
                body = row.get('BodyClass', row.get('Body Style', ''))
                
                if wmi and vds:
                    cursor.execute(
                        "INSERT OR IGNORE INTO vds_data (wmi, vds, model, engine, body_style) VALUES (?, ?, ?, ?, ?)", 
                        (wmi.strip(), vds.strip(), model.strip(), engine.strip(), body.strip())
                    )
        print(f"Loaded VDS data from {vds_csv}")
    else:
        print(f"File not found: {vds_csv}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    db = "vin_database.db"
    wmi_file = "data/nhtsa_wmi.csv"
    vds_file = "data/nhtsa_vds.csv"
    
    load_csv_to_db(db, wmi_file, vds_file)