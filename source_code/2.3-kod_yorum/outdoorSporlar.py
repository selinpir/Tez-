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
urun_listesi=[
    {
        "URUN_NO": 1,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2150,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-ayakkabi-gri-mh100/_/R-p-307854?mc=8555093&c=GR%C4%B0_MAV%C4%B0"
    },
    {
        "URUN_NO": 2,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2190,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-su-gecirmez-bot-gri-nh100/_/R-p-352773?mc=8871780&c=BEJ_GR%C4%B0"
    },
    {
        "URUN_NO": 3,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2050,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-kar-botu-su-gecirmez-siyah-nh100-mid/_/R-p-338961?mc=8737445&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 4,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1090,
        "TUM_YILDIZ": 4.5,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-ayakkabi-haki-nh50/_/R-p-350783?mc=8844095&c=S%C4%B0YAH_GR%C4%B0"
    },
    {
        "URUN_NO": 5,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2750,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-kar-botu-su-gecirmez-siyah-nh500-mid/_/R-p-307238?mc=8738739&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 6,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2990,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-su-gecirmez-bot-yesil-mh100/_/R-p-336189?mc=8789351&c=RENKS%C4%B0Z_GR%C4%B0_YE%C5%9E%C4%B0L"
    },
    {
        "URUN_NO": 7,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 980,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/cocuk-cirt-cirtli-outdoor-ayakkabi-mavi-24-34-nh100/_/R-p-313049?mc=8853302&c=S%C4%B0YAH_MAV%C4%B0"
    },
    {
        "URUN_NO": 8,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2050,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-kar-botu-su-gecirmez-siyah-nh100-mid/_/R-p-346370?mc=8800108&c=S%C4%B0YAH_GR%C4%B0"
    },
    {
        "URUN_NO": 9,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1090,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-ayakkabi-siyah-nh50/_/R-p-308248?mc=8553549&c=GR%C4%B0_YE%C5%9E%C4%B0L"
    },
    {
        "URUN_NO": 10,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2490,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/cocuk-outdoor-ayakkabi-turuncu-crossrock/_/R-p-357593?mc=8913048&c=S%C4%B0YAH_TURUNCU"
    }
]
"""
"""
urun_listesi = [
    {
        "URUN_NO": 11,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1850,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-ayakkabi-mavi-nh500-fresh/_/R-p-308263?mc=8786763&c=GR%C4%B0_MAV%C4%B0"
    },
    {
        "URUN_NO": 12,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2150,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-ayakkabi-gri-pembe-mh100/_/R-p-156123?mc=8612193&c=GR%C4%B0_YE%C5%9E%C4%B0L"
    },
    {
        "URUN_NO": 13,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 4350,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/erkek-su-gecirmez-outdoor-bot-gri-mh500-mid/_/R-p-330874?mc=8618767&c=KAHVERENG%C4%B0_MAV%C4%B0"
    },
    {
        "URUN_NO": 14,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1590,
        "TUM_YILDIZ": 4.5,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-bot-gri-nh100/_/R-p-171860?mc=8649282&c=KAHVERENG%C4%B0_GR%C4%B0"
    },
    {
        "URUN_NO": 15,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2750,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/cocuk-outdoor-bot-turuncu-crossrock/_/R-p-357625?mc=8913058&c=S%C4%B0YAH_TURUNCU"
    },
    {
        "URUN_NO": 16,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2250,
        "TUM_YILDIZ": 4.5,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-su-gecirmez-bot-mavi-nh100-mid/_/R-p-308079?mc=8554571&c=KAHVERENG%C4%B0_GR%C4%B0_MAV%C4%B0"
    },
    {
        "URUN_NO": 17,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1650,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/cocuk-outdoor-ayakkabi-gri-nh500/_/R-p-338586?mc=8736029&c=KAHVERENG%C4%B0_GR%C4%B0_TURUNCU"
    },
    {
        "URUN_NO": 18,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 3850,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-kar-botu-su-gecirmez-siyah-mh500-mid/_/R-p-340149?mc=8756995&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 19,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 3350,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-kar-botu-su-gecirmez-deri-hibrid-kahverengi-nh500-mid/_/R-p-350703?mc=8928705&c=S%C4%B0YAH_KAHVERENG%C4%B0"
    },
    {
        "URUN_NO": 20,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 4350,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-su-gecirmez-outdoor-ayakkabi-gri-mh500/_/R-p-330907?mc=8809163&c=S%C4%B0YAH_GR%C4%B0"
    }
]
"""

"""
urun_listesi=[
    {
        "URUN_NO": 21,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1650,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/cocuk-cirt-cirtli-outdoor-ayakkabi-gri-nh500/_/R-p-338630?mc=8736032&c=KAHVERENG%C4%B0_GR%C4%B0_TURUNCU"
    },
    {
        "URUN_NO": 22,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1650,
        "TUM_YILDIZ": 4.5,
        "URL": "https://www.decathlon.com.tr/r/cocuk-cirt-cirtli-outdoor-ayakkabi-bej-nh500/_/R-p-338587?mc=8786686&c=PEMBE_BEJ"
    },
    {
        "URUN_NO": 23,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1650,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/cocuk-bagcikli-outdoor-ayakkabi-bej-nh500/_/R-p-338631?mc=8786670&c=PEMBE_BEJ"
    },
    {
        "URUN_NO": 24,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2650,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/cocuk-su-gecirmez-outdoor-deri-kar-botu-kahverengi-35-38-sh500/_/R-p-307314?mc=8739087&c=MAV%C4%B0"
    },
    {
        "URUN_NO": 25,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2650,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/cocuk-outdoor-bot-turuncu-crosscrock/_/R-p-357721?mc=8928753&c=S%C4%B0YAH_MAV%C4%B0"
    },
    {
        "URUN_NO": 26,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2190,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-su-gecirmez-ayakkabi-gri-nh100/_/R-p-352810?mc=8871776&c=GR%C4%B0_YE%C5%9E%C4%B0L"
    },
    {
        "URUN_NO": 27,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2050,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/cocuk-outdoor-bot-kahverengi-nh500/_/R-p-348269?mc=8852751&c=KAHVERENG%C4%B0_GR%C4%B0"
    },
    {
        "URUN_NO": 28,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2050,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/cocuk-outdoor-bot-mavi-nh500/_/R-p-348179?mc=8811490&c=PEMBE_MAV%C4%B0"
    },
    {
        "URUN_NO": 29,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2650,
        "TUM_YILDIZ": 4.9,
        "URL": "https://www.decathlon.com.tr/r/cocuk-su-gecirmez-outdoor-kar-botu-turuncu-tarcin-24-34-sh500/_/R-p-307322?mc=8544119&c=PEMBE_MAV%C4%B0"
    },
    {
        "URUN_NO": 30,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2050,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/cocuk-outdoor-bot-mavi-nh500/_/R-p-348281?mc=8852774&c=PEMBE_MAV%C4%B0"
    },
    {
        "URUN_NO": 31,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1750,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/cocuk-su-gecirmez-outdoor-kar-botu-gri-mor-sh100/_/R-p-332649?mc=8648748&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 32,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1990,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-kar-botu-su-gecirmez-siyah-nh100/_/R-p-312022?mc=8581754&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 33,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1250,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/erkek-su-gecirmez-outdoor-kar-botu-siyah-sh100/_/R-p-108105?mc=8344304&c=GR%C4%B0"
    },
    {
        "URUN_NO": 34,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2550,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/kadin-su-gecirmez-outdoor-kar-botu-lacivert-sh500-high/_/R-p-340155?mc=8802419&c=BEJ"
    },
    {
        "URUN_NO": 35,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1250,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/kadin-su-gecirmez-outdoor-kar-botu-gri-sh100-mid/_/R-p-108086?mc=8344698&c=PEMBE_GR%C4%B0"
    },
    {
        "URUN_NO": 36,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2850,
        "TUM_YILDIZ": 4.5,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-kar-botu-siyah-nh500-high/_/R-p-344259?mc=8785598&c=S%C4%B0YAH_RENKS%C4%B0Z"
    }
]
"""

urun_listesi=[
    {
        "URUN_NO": 37,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1990,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-kar-botu-su-gecirmez-siyah-nh100/_/R-p-301402?mc=8501300&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 38,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1990,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-kar-botu-su-gecirmez-siyah-nh100-high/_/R-p-351123?mc=8851794&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 39,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2750,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-kar-botu-kahverengi-nh500-mid/_/R-p-307054?mc=8928703&c=MAV%C4%B0"
    },
    {
        "URUN_NO": 40,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 3350,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-kar-botu-su-gecirmez-bej-nh500-mid/_/R-p-348272?mc=8811473&c=KAHVERENG%C4%B0_BEJ"
    },
    {
        "URUN_NO": 41,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 3450,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-kar-botu-su-gecirmez-siyah-nh500/_/R-p-332914?mc=8644860&c=BEJ"
    },
    {
        "URUN_NO": 42,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2950,
        "TUM_YILDIZ": 4.5,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-kar-botu-su-gecirmez-siyah-nh500/_/R-p-324197?mc=8927929&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 43,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 4750,
        "TUM_YILDIZ": 4.6,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-kar-botu-su-gecirmez-sari-nh900/_/R-p-305000?mc=8901614&c=SARI"
    },
    {
        "URUN_NO": 44,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1850,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/cocuk-su-gecirmez-outdoor-kar-botu-lacivert-35-38-sh100/_/R-p-331109?mc=8861908&c=GR%C4%B0_MOR"
    },
    {
        "URUN_NO": 45,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 2650,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/cocuk-outdoor-kar-botu-su-gecirmez-lacivert-sh500/_/R-p-333165?mc=8861918&c=MAV%C4%B0"
    },
    {
        "URUN_NO": 46,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 6090,
        "TUM_YILDIZ": 4.2,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-kar-botu-su-gecirmez-mavi-mh900-pro-mid/_/R-p-349835?mc=8826199&c=MAV%C4%B0"
    },
    {
        "URUN_NO": 47,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 4250,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-kar-botu-su-gecirmez-deri-kahverengi-nh500/_/R-p-332020?mc=8641979&c=KAHVERENG%C4%B0"
    },
    {
        "URUN_NO": 48,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1850,
        "TUM_YILDIZ": 4.8,
        "URL": "https://www.decathlon.com.tr/r/cocuk-su-gecirmez-outdoor-kar-botu-lacivert-24-34-sh100/_/R-p-331132?mc=8861912&c=GR%C4%B0_MOR"
    },
    {
        "URUN_NO": 49,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1790,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/erkek-kar-botu-siyah-sh100-ultra-warm/_/R-p-133825?mc=8640887&c=S%C4%B0YAH_GR%C4%B0"
    },
    {
        "URUN_NO": 50,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1250,
        "TUM_YILDIZ": 4.7,
        "URL": "https://www.decathlon.com.tr/r/kadin-outdoor-kar-botu-su-gecirmez-siyah-nh100-mid/_/R-p-346334?mc=8873835&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 51,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Quechua",
        "FIYAT": 1250,
        "TUM_YILDIZ": 4.4,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-kar-botu-siyah-nh100-mid/_/R-p-342110?mc=8752017&c=S%C4%B0YAH"
    },
    {
        "URUN_NO": 52,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Simond",
        "FIYAT": 4550,
        "TUM_YILDIZ": 4.4,
        "URL": "https://www.decathlon.com.tr/r/erkek-outdoor-trekking-deri-bot-su-gecirmez-mt100/_/R-p-346646?mc=8801288&c=S%C4%B0YAH_GR%C4%B0"
    },
    {
        "URUN_NO": 53,
        "SPOR_DALI": "outdoor_sporlar",
        "MARKA": "Simond",
        "FIYAT": 7090,
        "TUM_YILDIZ": 4.5,
        "URL": "https://www.decathlon.com.tr/r/erkek-su-gecirmez-outdoor-deri-bot-kahverengi-mt500/_/R-p-344596?mc=8786155&c=KAHVERENG%C4%B0_GR%C4%B0"
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
