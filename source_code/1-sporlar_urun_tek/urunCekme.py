
import warnings
warnings.filterwarnings("ignore")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time, re, pandas as pd

SPOR_DALI = "voleybol"
URL = "https://www.decathlon.com.tr/tum-sporlar/voleybol/voleybol-ayakkabilari"
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

driver.get(URL)

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-supermodelid]'))
)

# Scroll — lazy load için
last_height = driver.execute_script("return document.body.scrollHeight")
for _ in range(15):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2.5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

cards = driver.find_elements(By.CSS_SELECTOR, 'div[data-supermodelid]')
products = []

for i, card in enumerate(cards, start=1):
    try:
        urun_no = card.get_attribute('data-supermodelid')
        marka   = card.find_element(By.CSS_SELECTOR, 'strong').text.strip()
        link    = card.find_element(By.CSS_SELECTOR, 'a[href*="/p/"]').get_attribute('href')

        # Fiyat
        fiyat = None
        try:
            fiyat_elem = card.find_element(By.CSS_SELECTOR, '[class*="vtmn-price"]')
            fiyat = fiyat_elem.text.strip()
        except:
            try:
                fiyat_elem = card.find_element(By.CSS_SELECTOR, 'span[class*="price"]')
                fiyat = fiyat_elem.text.strip()
            except:
                pass

        # Toplam yorum sayısı
        tum_yorum = 0
        try:
            rv = card.find_element(By.CSS_SELECTOR, 'span.vtmn-rating_comment--secondary').text
            m = re.search(r'\((\d+)\)', rv)
            if m:
                tum_yorum = int(m.group(1))
        except:
            pass

        # Genel yıldız ortalaması
        tum_yildiz = None
        try:
            r = card.find_element(By.CSS_SELECTOR, '[aria-label*="üzerinden"]')
            m2 = re.search(r'(\d+[.,]\d+)', r.get_attribute('aria-label'))
            if m2:
                tum_yildiz = float(m2.group(1).replace(',', '.'))
        except:
            pass

        products.append({
            'SIRA NO'   : i,
            'URUN NO'   : urun_no,
            'LINK-AD'   : link,
            'SPOR DALI' : SPOR_DALI,
            'MARKA'     : marka,
            'FIYAT'     : fiyat,
            'TUM YILDIZ': tum_yildiz,
            'TUM YORUM' : tum_yorum,
        })

    except Exception as e:
        print(f"Hata [{i}]: {e}")

driver.quit()

# Duplicate temizle
df = pd.DataFrame(products).drop_duplicates(subset=['URUN NO'], keep='first')
df['SIRA NO'] = range(1, len(df) + 1)  # Duplicate sonrası sırayı düzelt

# CSV olarak kaydet
df.to_csv('voleybol.csv', index=False, encoding='utf-8-sig')

# Kontroller
print(f"\nToplam çekilen : {len(products)}")
print(f"Duplicate      : {len(products) - len(df)}")
print(f"Benzersiz ürün : {len(df)}")
print(f"Boş değerler   :\n{df.isnull().sum()}")
print(f"\n✅ asama1_urunler.csv kaydedildi")
print(df[['SIRA NO', 'URUN NO', 'MARKA', 'FIYAT', 'TUM YILDIZ', 'TUM YORUM']].to_string())
