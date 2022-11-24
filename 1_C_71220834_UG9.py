("============== PILIH MENU ==============")
print ("1. Tambah")
print ("2. Kurang")
print ("3. Kali")
print ("4. Bagi")
bil1 = int(input ("Masukan angka pertama:"))
bil2 = int(input ("Masukan angka kedua:"))
pilih = input ("Pilihan anda:")
if pilih == '1':
    print ("hasil:",bil1+ bil2)
elif pilih == '2':
    print ("hasil:",bil1 - bil2)
elif pilih == '3':
    print ("hasil:",bil1*bil2)
elif pilih == '4':
    print ("hasil:",bil1/bil2)

