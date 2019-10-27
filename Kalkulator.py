def penjumlahan (a,b):
    penjumlahan = a+b
    return penjumlahan
def pengurangan (a,b):
    pengurangan = a-b
    return pengurangan
def perkalian(a,b):
    perkalian = a*b
    return perkalian
def pembagian (a,b):
    pembagian = a/b
    return pembagian

lagi= 'y'
while lagi=='y':
    print ' ====================================='
    print ' \t \t Author: Raffy '
    print ' \t \t Program Kalkulator Raffy Gans'
    print ' \t \t Selamat Mencoba Teman-teman'
    print ' °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°'
    print ' \t \t Follow Instagram :@rava_art_story '
    print ' ====================================='
    a= input(' Masukan Bilangan 1: ')
    b= input (' Masukan Biilangan 2 : ')
    print ' 1. Penjumlahan \n 2. pengurangan \n 3. perkalian \n 4. pembagian \n'
    c= input ('Pilih 1-5 : ')
    if c== 1:
        print ' Hasilnya adalah = ', penjumlahan (a,b)
    elif c== 2:
        print ' Hasilnya adalah = ', pengurangan (a,b)
    elif c==3 :
        print 'Hasilnya adalah = ', perkalian (a,b)
    else :
        print 'Hasilnya adalah = ', pembagian (a,b)

       print ' Terimakasih Sudah Menggunakan Tools Saya ^_^ '
       print ' Jangan Lupa Follow Instagram Saya @rava_art_story '
       print ' Heheheh THANKS FOR YOU^_^ '
      lagi=raw_input(" Mau Lagi ?[y/t] : ")
