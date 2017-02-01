#!/usr/bin/env python
#importowane biblioteki
import hashlib
import ssdeep
plik = open('C:/Users/Lukasz/Desktop/wdk/test.zip','rb')
#plik.mode 
#plik.name 
try:
    wczytaj = plik.read();
finally:
    plik.close()

sha = hashlib.sha256(wczytaj).hexdigest() #generujemy skr�t SHA-256
print("SHA-256:")
print(sha)	#skr�t SHA-256

md = hashlib.md5(wczytaj).hexdigest() #generujemy skr�t MD5
print("MD5:")
print(md)	#skr�t MD5

ssdp = ssdeep.hash(wczytaj)	#generujemy skr�t ssdeep
print("SSDEEP:")
print(ssdp)	#skr�t ssdeep

blocksize = 64935
mddeep = " "
with open('C:/Users/Lukasz/Desktop/wdk/test.zip',"rb") as file:
	for wynik in iter(lambda: file.read(1025),""): #u�ycie funkcji lambda ( funkcja bezimienna tworz�ca mini funkcj�)
		md5dp=hashlib.md5(wynik)
		mddeep=mddeep+md5dp.hexdigest() #skr�t md5deep
print("MD5DEEP:")
print(mddeep)	
