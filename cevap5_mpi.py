from mpi4py import MPI #Mpi kütüphanesini ekliyoruz
import hashlib#MD5 şifrelemesi için gerekli olan kütüphaneyi ekliyoruz

#Eşitlik kontrolü yapan bir fonksiyon oluşturuyoruz eğer eşit durum olursa aranan değerle bulundu şeklinde çıktı verecektir.
def Esit_mi(md5,rank): #fonksiyon oluşturuluyor
    if aranan_sifre==md5: #eşitlik kontrölüne bakılıyor
        print(md5," bulundu. Islemci Ranki: ",rank, ) #eşit olduğu durumda ekrana çıktı vermesini sağlar

comm=MPI.COMM_WORLD
size=comm.Get_size() #Kaç process çağırdığımıza bakıyoruz size eşitliyoruz.
rank=comm.Get_rank() #Çalışan işlemcinin rankını yani hangisi olduğunu tutuyoruz

aranan_sifre="db77174aa34ded1b6139455a58d0a38b" #aranan md5 şifreleme kelimesi ataması yapıldı. İnternet üzerinden içeriğine bakıldığında 'turkey' yazmaktadır.

if rank==0: #Master Ranka özel işlemlerini yazıyoruz.
    dosya = open("Wordlist.txt") #Dosyamızı okuyoruz.
    dizi=[hashlib.md5(kelime[:len(kelime)-1:].encode()).hexdigest() for kelime in dosya] #Dosyayı okuyup satır satır kelimeleri alıyoruz ve kelimelerin sonundaki '\n' ifadesini kelime[:len(kelime)-1:] diyerek silip hashlib kütüphanesi ile md5 formata çevirerek dizimize yazıyoruz. 'hashlib.md5(kelime[:len(kelime)-1:].encode()).hexdigest()' bu kısım kelimenin md5 kısmına dönüşmesini sağlamaktadır.
    uzunluk=int(len(dizi)/size); #Diziyi işlemcilere parçalı şekilde göndermek için bir işlemciye gönderilmesi gereken uzunluk hesaplanıyor.
    if size>1: #eğer toplam işlemci sayımız 1 den büyükse send işlemi yapacaz.
        for process_rank in range(1,size): #Döngü ile tüm işlemci ranklarını dolaşmaya başlıyoruz 1 den başlayarak size'a kadar
            comm.send(dizi[int(process_rank*uzunluk):int((process_rank+1)*uzunluk)],dest=int(process_rank)) #Burada process_rank ile uzunluğu çarparak başlangıç noktasını ve process_rank+1*uzunluk yazarakta bitiş noktasını buluyoruz. bu şekilde dizide belirlenen kısmın dest=process_rank ile gereken işlemciye gönderilmesini sağlıyoruz. 
        for md5 in dizi[int(rank*uzunluk):int((rank+1)*uzunluk)]: #Master rank sadece gönderme işlemi yapmakla kalmayıp kendi payına düşmesi gereken kısmı araması için döngü çağırıyorum ve dizinin ilk uzunluk yani yukarda hesaplamada bulduğum uzunluk kadarını master Processe arattırıyorum.
            Esit_mi(md5,rank) #Fonksiyonumu çağırarak kontrol işlemine başlıyorum
    else: #Eğer size 1 den büyük değil yani tek işlemci durumlarında direk kontrole geçmesi sağlanıyor
        for md5 in dizi: #Diziyi tek tek okuma işlemi yapılıyor
            Esit_mi(md5,rank) #okunan elemanın kontrolü için fonksiyonu çağırıyor
else: #Master İşlemci olmayan diğer işlemciler bu kısımda çalışması sağlanıyor.
    dizi=comm.recv(source=0) #Master işlemcide gönderdiğimiz veriyi okumak için recv fonksiyonu kullanıyoruz source=0 diyerek hangi işlemci olduğunu belirterek o işlemciden gelen diziyi bu işlemci için yeni olacak olan data dizi değişkenine atıyor.
    for md5 in dizi: #mesajla gelen dizi tek tek okunması sağlanıyor
        Esit_mi(md5,rank) #Okunan elemanın doğruluğunun kontrolü için fonksiyonumuzu çağırıyoruz.