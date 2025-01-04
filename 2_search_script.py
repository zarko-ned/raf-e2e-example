import tkinter as tk
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
html_file = os.path.join(current_dir, "products.html")
# Funkcija za unos pojma preko Tkinter
def get_search_term():
    def on_submit():
        global search_term
        search_term = entry.get()
        window.destroy()

    window = tk.Tk()
    window.title("Unesite pojam za pretragu")

    label = tk.Label(window, text="Unesite pojam za pretragu proizvoda:")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    submit_button = tk.Button(window, text="Potvrdi", command=on_submit)
    submit_button.pack()

    window.mainloop()

# Pokreni funkciju za unos
search_term = ""
get_search_term()

# Konfiguracija WebDriver-a
service = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

try:
    # Otvori stranicu proizvoda
    driver.get(f"file:///{html_file}")
    print("Otvorena stranica proizvoda")

    # Pretraži proizvode
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search_box")))
    search_box.clear()  # Očisti prethodni unos
    search_box.send_keys(search_term)  # Unesi pojam za pretragu
    driver.find_element(By.ID, "search_button").click()
    print(f"Pretraga za '{search_term}' zavrsena")

    # Proveri rezultat pretrage
    product_list = driver.find_elements(By.CSS_SELECTOR, "#product_list li")
    visible_products = [p.text for p in product_list if p.is_displayed()]
    assert search_term in visible_products, f"Proizvod sa pojmom '{search_term}' nije pronađen u pretrazi!"
    print("Rezultat pretrage validan")

finally:
    driver.quit()
