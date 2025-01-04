from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Konfiguracija WebDriver-a
service = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)
try:
    # Otvori stranicu za placanje
    driver.get("file:///C:/Users/Zarko/Documents/SeleniumPrimer/checkout.html")
    print("Otvorena stranica za placanje")

    # Popuni formu
    driver.find_element(By.ID, "name").send_keys("Zarko Nedeljkovic")
    driver.find_element(By.ID, "address").send_keys("Bulevar Kralja Aleksandra 73, Beograd")
    driver.find_element(By.ID, "payment").send_keys("Credit Card")
    driver.find_element(By.ID, "submit_order").click()
    print("Forma za placanje uspesno poslata")

    # Obradi alert (ako postoji)
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = Alert(driver)
        alert.accept()  # Prihvati alert
        print("Alert prihvacen: Order placed successfully!")
    except:
        print("Nema alert-a")

    # Proveri preusmeravanje
    WebDriverWait(driver, 10).until(EC.url_contains("thank_you.html"))
    print("Uspesno preusmeravanje na stranicu sa zahvalnicom")
    
finally:
    driver.quit()
