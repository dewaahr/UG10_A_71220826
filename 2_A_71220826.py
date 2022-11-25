print("===== Selamat datang di toko Andi Tersenyum, selamat belanja! =====")
total=int(input("Total belanja:Rp "))
diskon1=int(total-(total*0.02))
diskon2=int(total-(total*0.05))
diskon3=int(total-(total*10/100))
if total < 100000:
     print("Tidak ada diskon! Maka yang anda bayarkan adalah:",total)
elif total<= 100000:
     print("Biaya yang harus anda bayarkan setelah diskon adalah:Rp",diskon1)
elif total >=500000:
     print("Biaya yang harus anda bayarkan setelah diskon adalah:Rp",diskon2)
elif total >= 1000000:
     print("Biaya yang harus anda bayarkan setelah diskon adalah:Rp",diskon3)
