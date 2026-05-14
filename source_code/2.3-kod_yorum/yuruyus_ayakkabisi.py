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

urun_listesi=[
    {
        "URUN_NO": 1,
        "SPOR_DALI": "yuruyus_ayakkabisi",
        "MARKA": "Decathlon",
        "FIYAT": 1490,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/erkek-yuruyus-ayakkabisi-siyah-pw-160-slip-on/_/R-p-301054?mc=8774141&c=S%C4%B0YAH_KAHVERENG%C4%B0_BEYAZ"
    },
    {
        "URUN_NO": 2,
        "SPOR_DALI": "yuruyus_ayakkabisi",
        "MARKA": "Decathlon",
        "FIYAT": 1290,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/erkek-spor-ayakkabi-siyah-klnj-be-essential/_/R-p-347004?mc=8803075&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 3,
        "SPOR_DALI": "yuruyus_ayakkabisi",
        "MARKA": "Decathlon",
        "FIYAT": 1490,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-yuruyus-ayakkabisi-siyah-lila-pw-160-slip-on/_/R-p-304849?mc=8774167&c=S%C4%B0YAH_BEYAZ_MOR"
    },
    {
        "URUN_NO": 4,
        "SPOR_DALI": "yuruyus_ayakkabisi",
        "MARKA": "Decathlon",
        "FIYAT": 2350,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/erkek-deri-spor-ayakkabi-beyaz-cj80/_/R-p-346048?mc=8914243&c=BEYAZ_MAV%C4%B0"
    },
    {
        "URUN_NO": 5,
        "SPOR_DALI": "yuruyus_ayakkabisi",
        "MARKA": "Decathlon",
        "FIYAT": 2350,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-deri-spor-ayakkabi-beyaz-yesil-cj80/_/R-p-347095?mc=8803373&c=GR%C4%B0_BEYAZ"
    },
    {
        "URUN_NO": 6,
        "SPOR_DALI": "yuruyus_ayakkabisi",
        "MARKA": "Decathlon",
        "FIYAT": 2290,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/erkek-yuruyus-ayakkabisi-gri-walk-protect-mesh/_/R-p-337435?mc=8731851&c=KAHVERENG%C4%B0_GR%C4%B0_BEYAZ"
    },
    {
        "URUN_NO": 7,
        "SPOR_DALI": "yuruyus_ayakkabisi",
        "MARKA": "Decathlon",
        "FIYAT": 2990,
        "TUM_YILDIZ": 5.0,
        "URL": "https://www.decathlon.com.tr/r/erkek-spor-ayakkabi-siyah-lotto-norwell-5pr/_/R-p-382481?mc=9005864"
    },
    {
        "URUN_NO": 8,
        "SPOR_DALI": "yuruyus_ayakkabisi",
        "MARKA": "Decathlon",
        "FIYAT": 1290,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/kadin-spor-ayakkabi-siyah-klnj-be-essential/_/R-p-347051?mc=8803078&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 9,
        "SPOR_DALI": "yuruyus_ayakkabisi",
        "MARKA": "Decathlon",
        "FIYAT": 1490,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/erkek-spor-ayakkabi-mavi-lacivert-klnj-be-fresh/_/R-p-346939?mc=8803079&c=MAV%C4%B0"
    },
    {
        "URUN_NO": 10,
        "SPOR_DALI": "yuruyus_ayakkabisi",
        "MARKA": "Decathlon",
        "FIYAT": 1490,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/kadin-spor-ayakkabi-mavi-lacivert-klnj-be-fresh/_/R-p-347110?mc=8803378&c=MAV%C4%B0"
    },
    {
        "URUN_NO": 11,
        "SPOR_DALI": "yuruyus_ayakkabisi",
        "MARKA": "Decathlon",
        "FIYAT": 1450,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-spor-ayakkabi-siyah-klnj-be-d/_/R-p-347083?mc=8803408&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 12,
        "SPOR_DALI": "yuruyus_ayakkabisi",
        "MARKA": "Decathlon",
        "FIYAT": 3290,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/erkek-spor-ayakkabi-beyaz-gri-mavi-rr2k/_/R-p-354077?mc=8913819&c=BEJ_GR%C4%B0_MAV%C4%B0"
    }
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
