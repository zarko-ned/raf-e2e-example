Instalacija Python-a i Selenium biblioteka

Ovaj README sadrži uputstva za instalaciju Python-a i Selenium biblioteka kako biste započeli rad na projektima automatizovanog testiranja.

1. Provera instalacije Python-a

Pre nego što nastavite, proverite da li je Python već instaliran na vašem sistemu:

python --version

Ako dobijete grešku ili Python nije instaliran, nastavite sa sledećim korakom.

2. Instalacija Python-a

Na Windows-u

Koristite sledeću komandu u terminalu (koristeći winget):

winget install -e --id Python.Python.3

Nakon instalacije, zatvorite i ponovo otvorite terminal kako bi promene bile primenjene.

Na macOS-u

Instalirajte Python pomoću Homebrew alatke. Ako Homebrew nije instaliran, prvo ga instalirajte:

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Zatim instalirajte Python:

brew install python

Na Linux-u

Za distribucije kao što su Ubuntu ili Debian, koristite:

sudo apt update
sudo apt install python3 python3-pip -y

Za Fedora ili Red Hat:

sudo dnf install python3 -y

3. Instalacija Selenium biblioteka

Nakon što ste osigurali da je Python instaliran, instalirajte potrebne biblioteke koristeći pip:

Instalacija Selenium-a

pip install selenium

Instalacija WebDriver Manager-a

Biblioteka webdriver_manager pojednostavljuje upravljanje WebDriver-ima za različite pretraživače:

pip install webdriver_manager

4. Provera instalacije biblioteka

Proverite da li su Selenium i WebDriver Manager uspešno instalirani:

pip show selenium
pip show webdriver_manager

Ako vidite informacije o verziji i lokaciji instalacije, instalacija je uspešno završena.

5. Spremni za rad

Nakon uspešne instalacije, možete započeti rad sa Selenium-om. Kreirajte novi Python fajl i isprobajte osnovni primer koda:

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Pokretanje Chrome pretraživača
browser = webdriver.Chrome(ChromeDriverManager().install())

# Otvaranje stranice
browser.get("https://www.example.com")

# Zatvaranje pretraživača
browser.quit()

Ovaj primer koristi Chrome WebDriver za otvaranje web stranice i zatim zatvara pretraživač.

Dodatne informacije

Ako naiđete na probleme ili želite da saznate više o Selenium-u, posetite zvaničnu dokumentaciju.