tadbir_1 = {"Ali", "Vali", "Sami", "Lola"}
tadbir_2 = {"Ali", "Sami", "Nodir"}
tadbir_3 = {"Ali", "Lola", "Nodir"}

print("Barcha tadbirlarda:",*tadbir_1 & tadbir_2 & tadbir_3)

print("Kamida ikkitasida:",*(tadbir_1 & tadbir_2) | (tadbir_1 & tadbir_3) | (tadbir_2 & tadbir_3))
print("Faqat bittasida:",*(tadbir_1 | tadbir_2 | tadbir_3) - ((tadbir_1 & tadbir_2) | (tadbir_1 & tadbir_3) | (tadbir_2 & tadbir_3)))
