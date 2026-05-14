from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import csv
import os

"""
        {
        "URUN_NO": 1,
        "SPOR_DALI": "kosu",
        "MARKA": "Decathlon",
        "FIYAT": 2190,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-kosu-arazi-kosusu-ayakkabisi-siyah-pembe-jf190-grip/_/R-p-348767?mc=8913975&c=PEMBE_GR%C4%B0_BEYAZ"
    },
    {
        "URUN_NO": 2,
        "SPOR_DALI": "kosu",
        "MARKA": "Asics",
        "FIYAT": 3290,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-kosu-ayakkabisi-siyah-mercan-rengi-asics-gel-windhawk/_/R-p-361395?mc=8930459&c=S%C4%B0YAH_BEJ"
    },
    {
        "URUN_NO": 3,
        "SPOR_DALI": "kosu",
        "MARKA": "Asics",
        "FIYAT": 6990,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/erkek-kosu-ayakkabisi-beyaz-asics-gel-ziruss-8/_/R-p-357713?mc=8927364&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 4,
        "SPOR_DALI": "kosu",
        "MARKA": "Kalenji",
        "FIYAT": 1290,
        "TUM_YILDIZ": 4.5,
        "URL": "https://www.decathlon.com.tr/r/erkek-kosu-ayakkabisi-siyah-gri-jogflow-100-1/_/R-p-337693?mc=8733464&c=S%C4%B0YAH_BEYAZ"
    },
    {
        "URUN_NO": 5,
        "SPOR_DALI": "kosu",
        "MARKA": "Kalenji",
        "FIYAT": 1290,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-kosu-ayakkabisi-gri-kiprun-jogflow-100-1/_/R-p-337743?mc=8913940&c=GR%C4%B0_BEYAZ"
    },
    {
        "URUN_NO": 6,
        "SPOR_DALI": "kosu",
        "MARKA": "Kalenji",
        "FIYAT": 1690,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-kosu-ayakkabisi-yesil-jogflow-500-1/_/R-p-325939?mc=8588973&c=S%C4%B0YAH_TURUNCU"
    },
    {
        "URUN_NO": 7,
        "SPOR_DALI": "kosu",
        "MARKA": "Kiprun",
        "FIYAT": 1790,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/erkek-kosu-ayakkabisi-siyah-jogflow-190-1/_/R-p-339940?mc=8757334&c=S%C4%B0YAH_GR%C4%B0"
    },
    {
        "URUN_NO": 8,
        "SPOR_DALI": "kosu",
        "MARKA": "Kiprun",
        "FIYAT": 2190,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/erkek-kosu-arazi-kosusu-ayakkabisi-mavi-kiprun-jf-190-grip/_/R-p-348850?mc=8883621&c=S%C4%B0YAH_GR%C4%B0"
    },
    {
        "URUN_NO": 9,
        "SPOR_DALI": "kosu",
        "MARKA": "Kiprun",
        "FIYAT": 1390,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/cocuk-kosu-ayakkabisi-0-drop-yesil-sari-siyah-kiprun-kn500/_/R-p-342258?mc=8832634&c=YE%C5%9E%C4%B0L"
    },
"""
urun_listesi=[

    {
        "URUN_NO": 10,
        "SPOR_DALI": "kosu",
        "MARKA": "Kiprun",
        "FIYAT": 2590,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/erkek-kosu-ayakkabisi-gri-kiprun-kipcore/_/R-p-353286?mc=8873071&c=S%C4%B0YAH_BEYAZ"
    },
    {
        "URUN_NO": 11,
        "SPOR_DALI": "kosu",
        "MARKA": "Kiprun",
        "FIYAT": 2990,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/erkek-arazi-tipi-kosu-ayakkabisi-karbon-gri-tr2/_/R-p-312120?mc=8827180&c=KAHVERENG%C4%B0_GR%C4%B0"
    },
    {
        "URUN_NO": 12,
        "SPOR_DALI": "kosu",
        "MARKA": "Kiprun",
        "FIYAT": 1790,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-kosu-ayakkabisi-siyah-pembe-jogflow-190-1/_/R-p-339950?mc=8832420&c=BEYAZ_MOR"
    },
    {
        "URUN_NO": 13,
        "SPOR_DALI": "kosu",
        "MARKA": "Kiprun",
        "FIYAT": 2250,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/cocuk-kosu-ayakkabisi-siyah-beyaz-kiprun-k500-fast/_/R-p-338409?mc=8826358&c=MAV%C4%B0"
    },
    {
        "URUN_NO": 14,
        "SPOR_DALI": "kosu",
        "MARKA": "Kiprun",
        "FIYAT": 2590,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-kosu-ayakkabisi-siyah-kiprun-kipcore/_/R-p-353287?mc=8931013&c=S%C4%B0YAH_PEMBE_GR%C4%B0"
    },
    {
        "URUN_NO": 15,
        "SPOR_DALI": "kosu",
        "MARKA": "Kiprun",
        "FIYAT": 4990,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/kadin-arazi-tipi-kosu-ayakkabisi-gri-pembe-kiprun-mt-cushion-2/_/R-p-334419?mc=8914038&c=PEMBE_GR%C4%B0_BEYAZ"
    },
    {
        "URUN_NO": 16,
        "SPOR_DALI": "kosu",
        "MARKA": "Kiprun",
        "FIYAT": 3890,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-arazi-tipi-kosu-ayakkabisi-turkuaz-xt8/_/R-p-312160?mc=8914065&c=YE%C5%9E%C4%B0L_SARI"
    },
    {
        "URUN_NO": 17,
        "SPOR_DALI": "kosu",
        "MARKA": "Kiprun",
        "FIYAT": 3890,
        "TUM_YILDIZ": 4.1,
        "URL": "https://www.decathlon.com.tr/r/erkek-arazi-tipi-kosu-ayakkabisi-turkuaz-race-light/_/R-p-312132?mc=8737404&c=TURUNCU"
    },
    {
        "URUN_NO": 18,
        "SPOR_DALI": "kosu",
        "MARKA": "Kiprun",
        "FIYAT": 4190,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/kadin-kosu-ayakkabisi-siyah-pembe-kiprun-ks900-2/_/R-p-341717?mc=8930711&c=S%C4%B0YAH_PEMBE_BEYAZ"
    },
    {
        "URUN_NO": 19,
        "SPOR_DALI": "kosu",
        "MARKA": "Kiprun",
        "FIYAT": 5090,
        "TUM_YILDIZ": 4.4,
        "URL": "https://www.decathlon.com.tr/r/kadin-kosu-ayakkabisi-beyaz-sari-kiprun-kd900-2/_/R-p-347106?mc=8917220&c=BEYAZ_MOR"
    },

]

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    })
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver


for urun in urun_listesi:
    URUN_NO     = urun["URUN_NO"]
    SPOR_DALI   = urun["SPOR_DALI"]
    MARKA       = urun["MARKA"]
    FIYAT       = urun["FIYAT"]
    TUM_YILDIZ  = urun["TUM_YILDIZ"]
    product_url = urun["URL"]

    csv_dosya = f"{SPOR_DALI}_{URUN_NO}.csv"

    if os.path.exists(csv_dosya):
        print(f"⏭️  {csv_dosya} zaten mevcut, atlanıyor...")
        continue

    print(f"\n{'='*60}")
    print(f"Çekiliyor → URUN_NO={URUN_NO} | {MARKA} | {SPOR_DALI}")
    print(f"{'='*60}")

    driver = get_driver()
    reviews_data = []
    processed_review_ids = set()

    try:
        driver.get(product_url)
        print("Sayfa yuklendi...")
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        page_number = 1
        max_pages = 50
        consecutive_no_button = 0
        consecutive_no_turkey_reviews = 0

        while page_number <= max_pages:
            print(f"\nSayfa {page_number} isleniyor...")
            time.sleep(4)

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.review-item"))
                )
            except TimeoutException:
                print("Yorumlar yuklenemedi, bekleniyor...")
                time.sleep(5)

            review_articles = driver.find_elements(By.CSS_SELECTOR, "article.review-item")
            print(f"Sayfada gorunen toplam yorum sayisi: {len(review_articles)}")

            page_review_count = 0
            page_turkey_review_count = 0

            for article in review_articles:
                try:
                    article_text = article.text
                    has_turkey = "Türkiye" in article_text or "Turkey" in article_text
                    if has_turkey:
                        page_turkey_review_count += 1
                    if not has_turkey:
                        continue

                    try:
                        review_date = article.find_element(By.TAG_NAME, "time").get_attribute("datetime")
                    except:
                        review_date = ""
                    try:
                        review_title = article.find_element(By.CSS_SELECTOR, "h3.review-title").text.strip()
                    except:
                        review_title = ""
                    try:
                        review_text = article.find_element(By.CSS_SELECTOR, "p.review-item__body").text.strip()
                    except:
                        review_text = ""

                    review_id = f"{review_date}_{review_title}_{review_text[:50]}"
                    if review_id in processed_review_ids:
                        continue
                    processed_review_ids.add(review_id)

                    try:
                        usage_time = article.find_element(By.CSS_SELECTOR, "div.product-usage").text.strip()
                    except:
                        usage_time = ""
                    try:
                        rating_text = article.find_element(By.CSS_SELECTOR, "span.vtmn-rating_comment--primary").text.strip()
                        overall_rating = rating_text.replace("/5", "").strip()
                    except:
                        overall_rating = ""

                    reviews_data.append({
                        'URUN_NO':               URUN_NO,
                        'LINK_AD':               product_url,
                        'SPOR_DALI':             SPOR_DALI,
                        'MARKA':                 MARKA,
                        'FIYAT':                 FIYAT,
                        'TUM_YILDIZ':            TUM_YILDIZ,
                        'YORUM_YILDIZ':          overall_rating,
                        'YORUM_KULLANIM_SURESI': usage_time,
                        'YORUM':                 review_text,
                        'YORUMUN_POLARITESI':    "",
                    })
                    page_review_count += 1
                    print(f"Yeni yorum: {review_text[:40]}...")

                except (StaleElementReferenceException, Exception):
                    continue

            print(f"Sayfa {page_number}: {page_turkey_review_count} TR yorumu | {page_review_count} yeni | Toplam: {len(reviews_data)}")

            if page_turkey_review_count == 0:
                consecutive_no_turkey_reviews += 1
            else:
                consecutive_no_turkey_reviews = 0

            if consecutive_no_turkey_reviews >= 3:
                print("3 sayfa üst üste TR yorumu yok, sonlandırılıyor...")
                break

            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 500);")
                time.sleep(2)
                next_button = None
                for button in driver.find_elements(By.TAG_NAME, "button"):
                    try:
                        aria_label = button.get_attribute("aria-label") or ""
                        aria_disabled = button.get_attribute("aria-disabled")
                        if "sonraki inceleme" in aria_label.lower() and aria_disabled != "true":
                            next_button = button
                            break
                    except:
                        continue

                if next_button:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", next_button)
                    time.sleep(5)
                    page_number += 1
                    consecutive_no_button = 0
                else:
                    consecutive_no_button += 1
                    if consecutive_no_button >= 3:
                        break
                    time.sleep(3)
                    page_number += 1
            except:
                consecutive_no_button += 1
                if consecutive_no_button >= 3:
                    break

    except Exception as e:
        print(f"Hata: {e}")
    finally:
        driver.quit()

    if reviews_data:
        df_final = pd.DataFrame(reviews_data)
        df_final.to_csv(csv_dosya, index=False, encoding="utf-8-sig", quoting=csv.QUOTE_ALL)
        print(f"✅ Kaydedildi: {csv_dosya} ({len(df_final)} yorum)")
    else:
        print(f"⚠️  {URUN_NO} için TR yorumu bulunamadı.")

print("\n🎉 Tüm ürünler tamamlandı!")
