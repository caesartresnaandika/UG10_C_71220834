b = int(input("Masukan bulan (1-12:"))
if b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10  or b == 12:
    print ("Jumlah hari:", 31)
    
elif b == 4 or b == 6 or b == 9:
    print ("Jumlah hari:", 30)
    
elif b == 2:
    print ("Jumlah hari:", 28)

