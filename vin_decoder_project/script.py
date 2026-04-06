import sqlite3

def inject_test_data():
    conn = sqlite3.connect("vin_database.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT OR REPLACE INTO wmi_data (wmi, manufacturer, country) VALUES ('JT1', 'Toyota', 'Japan')")
    cursor.execute("INSERT OR REPLACE INTO vds_data (wmi, vds, model, engine, body_style) VALUES ('JT1', 'L0EE9', 'Corolla E90', '1.3L 2E', 'Sedan/Hatchback')")
    
    conn.commit()
    conn.close()
    print("Test data inserted.")

if __name__ == "__main__":
    inject_test_data()