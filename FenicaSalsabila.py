print ("-----------------------------------")
print ("PROGRAM PERHITUNGAN VOLUME DAN LUAS")
print ("-----------------------------------")
print ("[1] Balok")
print ("[2] Tabung")
print ("[3] Bola")
print ("-----------------------------------")
pilih = int(input("Pilih bangun datar: "))

if (pilih==1):
    pb = float(input("Panjang Balok = "))
    lb = float(input("Lebar Balok   = "))
    tb = float(input("Tinggi Balok  = "))
    print ("Volume Balok adalah = " ,pb*lb*tb)
    print ("Luas Balok adalah = " ,2*(pb*lb + pb*tb + lb*tb))
    
elif (pilih==2):
    rt = float(input("Jari-jari Tabung = "))
    tt = float(input("Tinggi Tabung    = "))
    print ("Volume Tabung adalah = " ,3.14*rt*rt*tt)
    print ("Luas Tabung adalah = " ,2*3.14*rt*(rt+tt))
    
elif (pilih==3):
    rb = float(input("Jari-jari Bola = "))
    print ("Volume Tabung adalah = " ,4/3*3.14*rb*rb*rb)
    print ("Luas Tabung adalah = " ,4*3.14*rb*rb)
    
else :
    print ("Tidak ada pilihan!")