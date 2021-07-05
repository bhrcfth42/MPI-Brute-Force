import hashlib #MD5 şifreleme için gerekli kütüphane eklemsi yapılıyor

#Eşitlik kontrolü yapan bir fonksiyon oluşturuyoruz eğer eşit durum olursa aranan değerle bulundu şeklinde çıktı verecektir.
def Esit_mi(md5): #fonksiyon oluşturuluyor
    if aranan_sifre==md5: #eşitlik kontrölüne bakılıyor
        print("bulundu") #eşit olduğu durumda ekrana çıktı vermesini sağlar

aranan_sifre="db77174aa34ded1b6139455a58d0a38b" #aranan md5 şifremizi bir değere atamasını yapıyoruz
dosya = open("Wordlist.txt") #Dosyamızı okuyoruz.
dizi=[hashlib.md5(kelime[:len(kelime)-1:].encode()).hexdigest() for kelime in dosya] #Dosyayı okuyup satır satır kelimeleri alıyoruz ve kelimelerin sonundaki '\n' ifadesini kelime[:len(kelime)-1:] diyerek silip hashlib kütüphanesi ile md5 formata çevirerek dizimize yazıyoruz. 'hashlib.md5(kelime[:len(kelime)-1:].encode()).hexdigest()' bu kısım kelimenin md5 kısmına dönüşmesini sağlamaktadır.
for md5 in dizi: #Dizideki md5 şeklinde olan kelimeler tek tek okunmaya başlanıyor for döngüsü ile
    Esit_mi(md5) #Eşitlik kontrolünü yapan fonksiyon çağrılıyor.