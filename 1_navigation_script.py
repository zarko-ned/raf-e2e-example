from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Konfiguracija WebDriver-a
service = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

try:
    # Otvori početnu stranicu
    driver.get("file:///C:/Users/Zarko/Documents/SeleniumPrimer/index.html")
    print("Otvorena pocetna stranica")

    # Klikni na link ka stranici proizvoda
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "products_link"))).click()
    print("Navigirano na stranicu proizvoda")
    
finally:
    driver.quit()
