
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
    print ' \t \t ====================================='
    print ' \t \t || Program Kalkulator Raffy Gans    || '
    print ' \t \t || Author:Raffy Gans                || '
    print ' \t \t || Follow Instagram: @rava_art_story|| '
    print ' \t \t ===================================== '
    a= input(' Masukan Bilangan 1: ')
    b= input (' Masukan Biilangan 2 : ')
    b= input (' Masukan Biilangan 2 : ')
    print ' 1. Penjumlahan \n 2. pengurangan \n 3. perkalian \n>
    c= input ('Pilih 1-5 : ')
    if c== 1:
        print ' Hasilnya adalah = ', penjumlahan (a,b)
    elif c== 2:
        print ' Hasilnya adalah = ', pengurangan (a,b)
    elif c==3 :
        print 'Hasilnya adalah = ', perkalian (a,b)
    else :
        print 'Hasilnya adalah = ', pembagian (a,b)

    lagi=raw_input(" Mau Lagi ?[y/t] : ")
