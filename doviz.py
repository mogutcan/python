import urllib2

page = urllib2.urlopen("http://www.tcmb.gov.tr/kurlar/today.html")
text = page.readlines()
for line in text:
        if line[0:7] == 'USD/TRY':
                kur_dolar = float(line[42:48])
        elif line[0:7] == 'EUR/TRY':
                kur_euro = float(line[42:48])
            

hesap=raw_input("Dolar donusumu icin 1 , Euro donusumu icin 2'ye basınız : ")
if hesap == "1" :
        carpan = input("Dolar adedi = ")
        sonuc = carpan*kur_dolar
        print str(carpan) +" $  = " ,str(sonuc) +" TL"
        

elif hesap == "2" :
        carpan = input("Euro adedi = ")
        sonuc = carpan*kur_euro
        print str(carpan) + " €  = " ,str(sonuc) +" TL"

