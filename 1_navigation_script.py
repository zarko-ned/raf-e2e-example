from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os


# Dobijanje trenutnog direktorijuma
current_dir = os.path.dirname(os.path.abspath(__file__))

# Kreiranje relativne putanje do HTML fajla
html_file = os.path.join(current_dir, "index.html")

# Konfiguracija WebDriver-a, u ovom slucaju Edge
service = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

try:
    # Otvoranje HTML fajl akoristeci relativnu putanju
    driver.get(f"file:///{html_file}")
    print("Otvorena pocetna stranica")

    # Klikni na link ka stranici proizvoda
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "products_link"))).click()
    print("Navigirano na stranicu proizvoda")
    
finally:
    driver.quit()
