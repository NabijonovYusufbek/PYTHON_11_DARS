ombor_1 = {"olma": 20, "anor": 12, "nok": 8}
ombor_2 = {"olma": 15, "banan": 10, "nok": 5}

birlashgan_ombor = {}

for mahsulot, miqdor in ombor_1.items():
    birlashgan_ombor[mahsulot] = miqdor

for mahsulot, miqdor in ombor_2.items():
    if mahsulot in birlashgan_ombor:
        birlashgan_ombor[mahsulot] += miqdor
    else:
        birlashgan_ombor[mahsulot] = miqdor

print(birlashgan_ombor)