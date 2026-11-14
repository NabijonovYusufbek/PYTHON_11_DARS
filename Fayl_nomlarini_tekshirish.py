fayllar = [
    "Hisobot 2026.pdf",
    "profil rasmi.jpg",
    "video.mp4",
    "jadval.xlsx",
    "diagramma.png",
]

ruxsat_etilgan = (".pdf", ".jpg", ".png")

asosiy_fayllar = []
boshqa_fayllar = []

for fayl in fayllar:
  if fayl.lower().endswith(ruxsat_etilgan):
    
    yangi_nom = fayl.replace(" ", "_")
    asosiy_fayllar.append(yangi_nom)
  else:
    boshqa_fayllar.append(fayl)

print("Yaroqli:", asosiy_fayllar)
print("Yaroqsiz:", boshqa_fayllar)