import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
# Dobijanje trenutnog direktorijuma
current_dir = os.path.dirname(os.path.abspath(__file__))

# Kreiranje relativne putanje do HTML fajla
html_file = os.path.join(current_dir, "checkout.html")
# Funkcija za unos podataka preko Tkinter
def get_checkout_details():
    def on_submit():
        global name, address, payment_method
        name = entry_name.get()
        address = entry_address.get()
        payment_method = entry_payment.get()
        window.quit()

    window = tk.Tk()
    window.title("Unesite podatke za placanje")

    label_name = tk.Label(window, text="Ime:")
    label_name.pack()
    entry_name = tk.Entry(window)
    entry_name.pack()

    label_address = tk.Label(window, text="Adresa:")
    label_address.pack()
    entry_address = tk.Entry(window)
    entry_address.pack()

    label_payment = tk.Label(window, text="Metoda Placanja:")
    label_payment.pack()
    entry_payment = tk.Entry(window)
    entry_payment.pack()

    submit_button = tk.Button(window, text="Potvrdi", command=on_submit)
    submit_button.pack()

    window.mainloop()

# Pokreni funkciju za unos podataka
name = ""
address = ""
payment_method = ""
get_checkout_details()

# Konfiguracija WebDriver-a
service = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

try:
    # Otvori stranicu za placanje
    driver.get(f"file:///{html_file}")
    print("Otvorena stranica za placanje")

    # Popuni formu sa podacima iz Tkintera
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.ID, "address").send_keys(address)
    driver.find_element(By.ID, "payment").send_keys(payment_method)
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
