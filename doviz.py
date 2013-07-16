#-*- coding : utf-8 -*-

import urllib2

page = urllib2.urlopen("http://www.tcmb.gov.tr/kurlar/today.html")
text = page.readlines()

for line in text:
        if line[0:7] == 'USD/TRY':
                kur_dolar = float(line[42:52])
        elif line[0:7] == 'EUR/TRY':
                kur_euro = float(line[42:52])
            
doviz = raw_input("Dolar donusumu icin 1 , Euro donusumu icin 2'ye basınız : ")

print("\n")
print("Türkiye Cumhuriyeti Merkez Bankası'ndan bugünkü kur verileri alınıyor...\n")
    
if doviz == "1" :
    carpan = input("Dolar adedi = ")
    sonuc = carpan*kur_dolar
    print str(carpan) +" $  = " ,str(sonuc) +" TL"
        

elif doviz == "2" :
    carpan = input("Euro adedi = ")
    sonuc = carpan*kur_euro
    print str(carpan) + " €  = " ,str(sonuc) +" TL"
