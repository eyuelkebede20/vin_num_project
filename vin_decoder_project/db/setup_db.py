import sqlite3
import os

def setup_database():
    db_path = "vin_database.db"
    schema_path = "db/schema.sql"
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    with open(schema_path, 'r') as file:
        cursor.executescript(file.read())
        
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()