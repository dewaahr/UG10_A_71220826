nilai1 =float(input("Masukan nilai soal 1:"))
nilai2 = float(input("Masukan nilai soal 2:"))
nilai3 =float(input("Masukan nilai soal 3:"))
umur=int(input("Masukan umur anda:"))
#ratarata= (nilai1*0.5)+(nilai2*0.3)+(nilai3*0.2)/3
ratarata= int((nilai1+nilai2+nilai3)/3)
print("Rata-rata Nilai Anda:",ratarata)
if ratarata<=25:
    if umur<=80:
        print("Selamat anda Lulus")
    else:print("coba lagi tahun depan!")
else :
    if ratarata>=90:
        print("Selamat anda Lulus")
    else: print("coba lagi tahun depan!")
