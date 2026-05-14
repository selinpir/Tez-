import pandas as pd
import glob
import os

os.chdir("/Users/selinpir/Desktop/tezYeni1103/2-yorumCekme/2.1-yorumCekme/16-voleybol(8)")

dosyalar = sorted(glob.glob("*.csv"))
print(f"Bulunan dosyalar: {dosyalar}")

if not dosyalar:
    raise FileNotFoundError(f"Klasörde hiç CSV yok!")

df_list = []
for dosya in dosyalar:
    try:
        df = pd.read_csv(dosya, encoding="utf-8-sig")
        if len(df.columns) <= 2:
            df = pd.read_csv(dosya, encoding="utf-8-sig", sep=";")

        # Her URUN_NO için yorum sayısını hesapla ve TUM_YORUM olarak ekle
        df["TUM_YORUM"] = df.groupby("URUN_NO")["URUN_NO"].transform("count")

        df_list.append(df)
        print(f"{dosya}: {len(df)} satır, {len(df.columns)} sütun")
    except Exception as e:
        print(f"{dosya} okunamadı: {e}")

df_final = pd.concat(df_list, ignore_index=True)

# Sütun adı temizleme
df_final.columns = [col.strip().rstrip(";") for col in df_final.columns]

df_final = df_final.rename(columns={
    "genel_puan":      "YORUM_YILDIZ",
    "kullanilan_sure": "YORUM_KULLANIM_SURESI",
    "yorum":           "YORUM",
})

df_final = df_final[pd.to_numeric(df_final["URUN_NO"], errors="coerce").notna()].copy()
df_final["URUN_NO"] = df_final["URUN_NO"].astype(int)

if "YORUMUN_POLARITESI" not in df_final.columns:
    df_final["YORUMUN_POLARITESI"] = ""

# URUN_NO'ya göre sırala, sonra SIRA_NO ata
df_final = df_final.sort_values("URUN_NO").reset_index(drop=True)
df_final.insert(0, "SIRA_NO", range(1, len(df_final) + 1))

# Birleştirme sonrası TUM_YORUM'u URUN_NO bazında yeniden hesapla (tüm CSV'ler dahil)
df_final["TUM_YORUM"] = df_final.groupby("URUN_NO")["URUN_NO"].transform("count")

sutunlar = ["SIRA_NO", "URUN_NO", "LINK_AD", "SPOR_DALI", "MARKA",
            "FIYAT", "TUM_YILDIZ", "TUM_YORUM",
            "YORUM_YILDIZ", "YORUM_KULLANIM_SURESI", "YORUM", "YORUMUN_POLARITESI"]

df_final = df_final[sutunlar].reset_index(drop=True)

df_final.to_excel("voleybol_birlestirme.xlsx", index=False, engine="openpyxl")
print(f"\nToplam satır: {len(df_final)}")
print("Kaydedildi: voleybol_birlestirme.xlsx")
