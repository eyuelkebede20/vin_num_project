import sqlite3

def get_year_from_code(year_code):
    year_map = {
        'A': '1980/2010', 'B': '1981/2011', 'C': '1982/2012', 'D': '1983/2013', 'E': '1984/2014',
        'F': '1985/2015', 'G': '1986/2016', 'H': '1987/2017', 'J': '1988/2018', 'K': '1989/2019',
        'L': '1990/2020', 'M': '1991/2021', 'N': '1992/2022', 'P': '1993/2023', 'R': '1994/2024',
        'S': '1995/2025', 'T': '1996/2026', 'V': '1997/2027', 'W': '1998/2028', 'X': '1999/2029',
        'Y': '2000/2030', '1': '2001/2031', '2': '2002/2032', '3': '2003/2033', '4': '2004/2034',
        '5': '2005/2035', '6': '2006/2036', '7': '2007/2037', '8': '2008/2038', '9': '2009/2039'
    }
    return year_map.get(year_code.upper(), "Unknown/Non-Standard")

def decode_vin(vin, db_path="vin_database.db"):
    if len(vin) != 17:
        return "Invalid VIN length"

    wmi = vin[0:3]
    vds = vin[3:8]
    year_code = vin[9]
    plant_code = vin[10]
    serial_number = vin[11:17]

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT manufacturer, country FROM wmi_data WHERE wmi = ?", (wmi,))
    wmi_result = cursor.fetchone()

    cursor.execute("SELECT model, engine, body_style FROM vds_data WHERE wmi = ? AND vds = ?", (wmi, vds))
    vds_result = cursor.fetchone()

    conn.close()

    return {
        "Manufacturer Data": wmi_result,
        "Vehicle Descriptor": vds_result,
        "Model Year Code": year_code,
        "Model Year": get_year_from_code(year_code),
        "Plant Code": plant_code,
        "Serial Number": serial_number
    }