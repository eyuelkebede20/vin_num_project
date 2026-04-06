import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time
import pymongo

def scrape_vin_stealth(vin):
    url = f"https://www.vindecoderz.com/v/{vin}"
    
    options = uc.ChromeOptions()
    options.headless = False 
    
    driver = uc.Chrome(options=options)
    
    try:
        driver.get(url)
        time.sleep(40) 
        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        
        # This will tell us if you are blocked by Cloudflare
        print(f"DEBUG - Current Page Title: {driver.title}") 
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        vehicle_data = {}
        
        table_rows = soup.find_all('tr') 
        
        for row in table_rows:
            cols = row.find_all('td')
            if len(cols) == 2:
                key = cols[0].text.strip()
                value = cols[1].text.strip()
                vehicle_data[key] = value
                
        return vehicle_data
        
    finally:
        try:
            driver.quit()
        except OSError:
            pass # Suppresses the WinError 6 bug

test_vin = "MHKAA1BA5PJ051923"
print(scrape_vin_stealth(test_vin))



def insert_to_mongodb(cleaned_data):
    try:
        # Default local MongoDB connection string
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        
        # Creates database and collection automatically if they don't exist
        db = client["carDealership"]
        collection = db["vin_records"]

        # Insert the dictionary directly
        result = collection.insert_one(cleaned_data)
        return f"Inserted 1 document. ID: {result.inserted_id}"
        
    except pymongo.errors.PyMongoError as err:
        return f"Database Error: {err}"
    finally:
        if 'client' in locals():
            client.close()

# Execution Flow
raw_dict = scrape_vin_stealth(test_vin)
clean_dict = clean_vin_data(raw_dict)
print("Cleaned Data:", clean_dict)

db_status = insert_to_mongodb(clean_dict)
print(db_status)