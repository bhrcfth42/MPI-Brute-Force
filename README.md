# MPI Brute Force - MPI Kaba Kuvvet

Bu soruda basit olarak bir şifre kırma algoritması yazmanız gerekmektedir. Verilen bir sözlük içerisindeki tüm elemanlar tek tek denenerek kullanıcının şifresi bulunmaya çalışılacaktır. Ancak elimizde sadece kullanıcı şifresinin md5 ile şifrelenmiş halini bulunmaktadır. Burada istenen verilen sözlükteki elemanların tek tek md5 algoritmasından geçirilerek elde edilen çıktının şifreli metin ile karşılaştırılması ve doğru şifre kombinasyonu bulunduğunda bu şifrenin ekrana yazdırılmasıdır. Python programlama dilinde bu şifrenin ne olduğunu Brute Force(Kaba Kuvvet) ile bulan standart(seri) kodunu yazınız.
Daha sonra bu kodun paralel programlama ile mpi kütüphanesini kullanarak yazınız. Yazdığınız paralel kod için proses sayılarını 4, 8, 12 ve 24 olacak şekilde çalıştırınız ve programın çalışma sürelerini karşılaştırınız. Burada her bir proses, verilen sözlükteki verileri eşit olarak paylaşacak ve belirli aralıkta arama yapacaktır.
Sözlük listesi wordlist.txt olarak verilmiştir. Bu worldlist’i dosyadan okuyup dizi şeklinde kullanabilirsiniz.

Aranacak kelimenin md5 algoritması ile şifrelenmiş hali = “db77174aa34ded1b6139455a58d0a38b”
