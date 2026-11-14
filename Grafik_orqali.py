import matplotlib.pyplot as plt

oylar = ["Yan", "Fev", "Mar", "Apr", "May", "Iyun"]
daromad = [12, 15, 11, 19, 22, 18]  # mln so‘m

kategoriyalar = ["Texnika", "Kiyim", "Oziq-ovqat"]
savdo = [35, 20, 45]  # dona

buyurtma_qiymatlari = [50, 75, 80, 120, 150, 150, 180, 220, 250, 300]

plt.plot(oylar,daromad,marker="p",color="b")
plt.title("Oylik daromadi")
plt.xlabel("Oylar")
plt.ylabel("Daromat (mln so'm)")
plt.grid(True)
plt.show()

a = plt.bar(kategoriyalar,savdo,color="r",width=0.5)
plt.bar_label(a)
plt.title("Do'kon Savdosi")
plt.xlabel("Yo'nalishlar")
plt.ylabel("Sotilganlar (dona)")
plt.show()

plt.hist(buyurtma_qiymatlari,bins=5,color="g",edgecolor="White")
plt.title("Buyurtmalar")
plt.xlabel("Buyurtma sonlari (dona)")
plt.ylabel("Kunlar")

plt.show()