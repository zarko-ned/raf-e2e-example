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
    # Otvori stranicu proizvoda
    driver.get("file:///C:/Users/Zarko/Documents/SeleniumPrimer/products.html")
    print("Otvorena stranica proizvoda")

    # Pretraži proizvode
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search_box")))
    search_box.send_keys("Laptop")
    driver.find_element(By.ID, "search_button").click()
    print("Pretraga zavrsena")

    # Proveri rezultat pretrage
    product_list = driver.find_elements(By.CSS_SELECTOR, "#product_list li")
    visible_products = [p.text for p in product_list if p.is_displayed()]
    assert "Laptop" in visible_products, "Laptop nije pronadjen u pretrazi!"
    print("Rezultat pretrage validan")
    
finally:
    driver.quit()
