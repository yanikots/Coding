import random
import sys
replay="e"
while replay == "e":
        MAXDIGIT=4  ###oyundaki basamak sayisi###

        target=[]

        y=random.randint(1,9)
        target.append(str(y))  #join için STR lazım

        i=1
        while i< MAXDIGIT:
                unique=False
                while not unique:
                    y=random.randint(0,9)
                    if str(y) not in target:
                        target.append(str(y))
                        unique=True                    ###loop variable###
                i=i+1

        target="".join(target)       # 1234 şeklinde bir çıktı veriyor (join yapmazsan ['1','2','3','4'] şeklinde)
        tahmin_sayısı=0
        
        print ("""Artılar ve Eksiler'e hoşgeldiniz!
Aklımdaki 4 haneli sayıyı bilebilecek misiniz? 
Söylediğiniz sayının rakamlarından birisi
eğer benim belirlediğim sayının rakamlarından birisiyle aynıysa
ve basamak olarak da aynı yerdeyse 1 artı,
farklı bir basamaktaysa 1 eksi söylenecektir.""") # /n komutuna gerek kalmadan alt alta uzun yazı
            

        found=False
        while not found:
            guess=str(input("Lütfen 4 haneli bir sayı giriniz:"))
            tahmin_sayısı=tahmin_sayısı+1
            guess=list(guess)                                             #user'ın girdiği 4567'yi ['4','5','6','7'] yapıyor böylece index kontrolü  yapıyoruz

            artı=0
            eksi=0
            a=0                                         #a'yı indeks sayısı olarak kullanacaz. 4 indeks olacak, 0,1,2,3,  olacak.
            while a<4:
                    if guess[a] in target:              # aslında bir string olduğu için aynı zamanda liste de oluyor, user'ın a indeksindeki say, tahmin listesinin içinde var mı diye bakıyoruz.
                            if guess[a]==target[a]:
                                artı=artı+1
                            else:                        
                                eksi=eksi+1
                    a=a+1

            if artı==4:
                    print("Doğru bildin!")
                    found = True
            else:        
                    print("artı:"+str(artı)+","+"eksi:"+str(eksi))           #str'ye çevir ki hata vermesin

            print("tahmin sayısı:"+str(tahmin_sayısı))
            
        replay = input("Tekrar oynamak ister misiniz?e/h")
sys.exit()
            
