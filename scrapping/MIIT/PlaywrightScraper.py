from playwright.sync_api import sync_playwright
import mysql.connector

def scrape_miit_mirror():
    db = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="password", 
        database="car_specs"
    )
    cursor = db.cursor()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Target AutoHome EV index (MIIT mirror)
        page.goto("https://car.autohome.com.cn/newenergy/")
        page.wait_for_selector('.list-cont') 
        
        cars = page.query_selector_all('.list-cont-bg')
        for car in cars:
            try:
                make_model = car.query_selector('.main-title').inner_text()
                motor_power = car.query_selector('.info-power').inner_text() 
                
                sql = "INSERT INTO vehicles (make_model, motor_peak_power_kw) VALUES (%s, %s)"
                cursor.execute(sql, (make_model, motor_power))
                db.commit()
            except AttributeError:
                continue 
            
        browser.close()

if __name__ == "__main__":
    scrape_miit_mirror()