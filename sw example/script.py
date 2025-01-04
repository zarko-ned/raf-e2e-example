from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
# Dobijanje trenutnog direktorijuma
current_dir = os.path.dirname(os.path.abspath(__file__))

# Kreiranje relativne putanje do HTML fajla
html_file = os.path.join(current_dir, "swapi_species_with_films.html")
# Kreiranje instanci Edge drajvera
edge_options = Options()
edge_options.use_chromium = True
edge_options.add_argument("--headless")  # Pokretanje u headless modu
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)

# Otvaranje lokalnog HTML fajla
driver.get(f"file:///{html_file}")

# Čekanje da se podaci učitaju (najbolje koristiti WebDriverWait u stvarnim scenarijima)
driver.implicitly_wait(10)

# Testiranje prikaza informacija o vrsti
species_info = driver.find_elements(By.CLASS_NAME, "info-item")
assert len(species_info) == 4, "Nedostaju neki podaci o vrsti!"

# Provera sadržaja podataka o vrsti
expected_data = {
    "Name": "Wookiee",
    "Classification": "Mammal",
    "Language": "Shyriiwook",
    "Average Lifespan": "400 years"
}

for item in species_info:
    key = item.find_element(By.TAG_NAME, "strong").text.rstrip(":")
    value = item.text.split(": ")[1]
    assert value.lower() == expected_data[key].lower(), f"Očekivano {expected_data[key]} za {key}, ali pronađeno {value}"

# Testiranje liste filmova
movies_list = driver.find_elements(By.CSS_SELECTOR, ".movies-list li")
assert len(movies_list) > 0, "Lista filmova je prazna!"

# Zatvaranje drajvera
driver.quit()

print("Svi testovi su prošli uspešno!")
