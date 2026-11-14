jami_soat, eng_kop, eng_xodim = 0, -1, ""

with open("11_Dars/IshVaqti.txt", "r") as f:
  for i, qator in enumerate(f, 1):
    qismlar = qator.split()
    if len(qismlar) < 2:
      continue

    ism, soat_str = " ".join(qismlar[:-1]), qismlar[-1]

    try:
      soat = int(soat_str)
      jami_soat += soat
      if soat > eng_kop:
        eng_kop, eng_xodim = soat, ism
    except ValueError:
      print(f"{i}-qator xato: '{soat_str}' son emas.")

print(f"Jami soat: {jami_soat}")
print(f"Eng ko'p ishlagan: {eng_xodim} ({eng_kop} soat)")