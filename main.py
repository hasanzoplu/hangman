import random

kelimeler = ["kedi", "köpek", "kablumbağa", "yunus", "balina", "fok", "arı", "atmaca", "güvercin", "aslan"]
secilen_kelime = random.choice(kelimeler)
gecerliHarfler = "abcçdefgğhıijklmnoöpqrsştuüvwxyz"
toplamHak = 6
yapilanTahmin = ""

# Oyun görselleri
ADAM_ASMACA_GORSLLERI = [
    """
      --------
      |    |
      |
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |    |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|/
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|/
      |   /
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|/
      |   / / 
      |
    """
]


def rastgele_harf_tahmini(yapilan_tahmin):
    return random.choice([harf for harf in gecerliHarfler if harf not in yapilan_tahmin])


def sik_kullanilan_harf_tahmini(yapilan_tahmin):
    sik_kullanilan_harfler = "aeıioöuü"
    for harf in sik_kullanilan_harfler:
        if harf not in yapilan_tahmin:
            return harf
    return rastgele_harf_tahmini(yapilan_tahmin)


def uc_harfleri_tahmin_et(yapilan_tahmin):
    uclardaki_harfler = "mnsrldğçtkbcghfprsşvyz"
    for harf in uclardaki_harfler:
        if harf not in yapilan_tahmin:
            return harf
    return rastgele_harf_tahmini(yapilan_tahmin)


print("Adam Asmaca Oyununa Hoş Geldiniz!")

while toplamHak > 0:
    gercekKelime = ""
    for harf in secilen_kelime:
        if harf in yapilanTahmin:
            gercekKelime += harf
        else:
            gercekKelime += "_ "

    if gercekKelime == secilen_kelime:
        print(gercekKelime)
        print("Tebrikler kazandınız!")
        break

    print(ADAM_ASMACA_GORSLLERI[6 - toplamHak])
    print(""adı tahmin edin:", gercekKelime)
    print(f"Kalan hakkınız: {toplamHak}")

    # Kullanıcının kazanma stratejisini seç
    print("Kazanma Stratejileri:")
    print("1. Rastgele harf seç")
    print("2. Sık kullanılan harflerden seç")
    print("3. Üç harf içerenlerden seç")

    # Strateji seçimi
    stratejiler = [rastgele_harf_tahmini, sik_kullanilan_harf_tahmini, uc_harfleri_tahmin_et,
                   ]
    secim = int(input("Bir strateji seçin (1-4): "))
    secim -= 1  # Liste indeksleri 0'dan başladığı için

    if 0 <= secim < len(stratejiler):
        tahmin = stratejiler[secim](yapilanTahmin)
    else:
        print("Geçersiz strateji seçimi. Lütfen 1-4 arasında bir sayı seçin.")
        continue

    # Kullanıcının harf tahminini al
    print(f"Stratejiye göre tahmin: {tahmin}")
    tahmin_harf = input("Harfi girin: ").lower()

    if tahmin_harf in gecerliHarfler:
        print(f"Kullanıcının tahmini: {tahmin_harf}")
        yapilanTahmin += tahmin_harf

        if tahmin_harf not in secilen_kelime:
            toplamHak -= 1
    else:
        print("Geçersiz harf. Lütfen bir harf girin.")

else:
    print("Maalesef kaybettiniz. Doğru kelime:", secilen_kelime)
