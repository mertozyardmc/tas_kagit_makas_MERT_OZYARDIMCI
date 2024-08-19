import random
import math
def tas_kagit_makas_MERT_OZYARDIMCI():
    def generator():
        return random.choice(moves)
    def generatoreh():
        return random.choice(moveseh)
    i = 1
    gamecounter = 1
    playergamescore = 0
    opponentgamescore = 0
    while i == 1:
        print("\nKadim zamanlarda, Yedi Zirveler Dağı'nın derinliklerinde, bin yıllardır süregelen bir turnuva düzenlenirdi."
        "\nKatılımcılar, Aether'in Işığı (ışık) Acaia'nın Tohumu (toprak) ve Nyx'in Gölgesi (gölge) arasında ustalıklarını sergileyerek, doğanın en güçlü varlığı olma yolunda mücadele ederdi."
        "\nBu yıl, turnuvaya katılma sırası sana geldi. Ancak karşında, eski zamanlardan beri mağlup edilemeyen ve ismi tarihin tozlu sayfalarında unutulmuş bir varlık duruyor:"
        "\n\n Antros."
        "\nAntros, elementlerin efendisi olarak bilinir ve sonsuz döngüler boyunca turnuvayı kazanan taraf olmuştur."
        "\nTurnuvanın galibi, evrenin güçlerini kontrol eden antik bir ruhla ödüllendirilecektir."
        "\nBu efsanevi mücadelede, Antros’a karşı Aether'in Işığı,Acaia'nın Tohumu ve Nyx'in Gölgesi’ni ustalıkla kullanmalısın."
        "\n\nAncak dikkat et! Aether'in Işığı Nyx'in Gölgesi'ni yok eder, Nyx'in Gölgesi Acaia'nın Tohumu’nu tüketir, ve Acaia'nın Tohumu ise Aether'in Işığı'nı emer."
        "\n\nHazır isen Mücadele başlasın!!")
        moves = ["I","G","T"]
        roundcounter = 1
        playerscore = 0
        opponentscore = 0
        while  not (playerscore == 2 or opponentscore == 2):
            playermove = input(str("\n Unutma!\nAether'in Işığı için (I), Nyx'in Gölgesi için (G), ve Acaia'nın Tohumu için (T) yazmalısınız!\n\n"))
            opponentmove = generator()
            if playermove in moves:
                if playermove == "I" and opponentmove == "I": #DRAW
                    print("Aether'in Işığı (I) kendi kendine zarar veremez! ")
                elif playermove == "I" and opponentmove == "G": #PLAYERWİN
                    playerscore += 1
                    print("Rakibin Nyx'in Gölgesi'ni seçti. Aether'in Işığı (I), Nyx'in Gölgesi'ni (G) yok eder!")
                elif playermove == "I" and opponentmove == "T": #OPPONENTWİN
                    opponentscore += 1
                    print("Rakibin Acaia'nın Tohumu'nu seçti. Acaia'nın Tohumu (T), Aether'in Işığı'nı (I) emer!")
                elif playermove == "G" and opponentmove == "I": #OPPONENTWİN
                    opponentscore += 1
                    print("Rakibin Aether'in Işığı'nı seçti. Aether'in Işığı (I), Nyx'in Gölgesi'ni (G) yok eder!")
                elif playermove == "G" and opponentmove == "G": #DRAW
                    print("Nyx'in Gölgesi (G) kendi kendine zarar veremez! ")
                elif playermove == "G" and opponentmove == "T": #PLAYERWİN
                    playerscore += 1
                    print("Rakibin Acaia'nın Tohumu'nu seçti. Nyx'in Gölgesi (G) Acaia'nın Tohumu’nu (T) tüketir!")
                elif playermove == "T" and opponentmove == "I": #PLAYERWİN
                    playerscore += 1
                    print("Rakibin Aether'in Işığı'nı seçti. Acaia'nın Tohumu (T), Aether'in Işığı'nı (I) emer!")
                elif playermove == "T" and opponentmove == "G": #OPPONENTWİN
                    opponentscore += 1
                    print("Rakibin Nyx'in Gölgesi'ni seçti. Nyx'in Gölgesi (G) Acaia'nın Tohumu’nu (T) tüketir!")
                elif playermove == "T" and opponentmove == "T":  #DRAW
                    print("Acaia'nın Tohumu (T) kendi kendine zarar veremez! ")
                print( roundcounter,".Round bitti.","\nPuanın:",playerscore,"\nRakibinin Puanı:",opponentscore)
                roundcounter += 1
            else:
                print("Gİrdiğiniz değer yanlış!\nLütfen ( I ) ( G ) ( T ) gibi harfleri kullanınız! Parantezsiz ve büyük!")
        if playerscore == 2:
            playergamescore += 1
            print("Bu oyunu sen kazandın!")
        else:
            opponentgamescore += 1
            print("Antros kazandı!")

        while True:
            devammi = input("Devam etmek istiyor musun. Evet için ( E ) , Hayır için ( H ) \n")
            moveseh = ["E", "H"]
            if devammi in moveseh:
                if devammi == "E":
                    if generatoreh() == "E":
                        gamecounter += 1
                        print(f"{gamecounter}. oyunumuza hoş geldin")
                        break
                    else:
                        print("Malesef rakibiniz korkup kaçtı!")
                        i += 1
                        break
                else:
                    print("Başka zaman görüşürüz!")
                    i += 1
                    break
            else:
                print("Yanlış girdiniz, Lütfen ( E ) veya ( H )'den birini seçiniz!")
    if playergamescore > opponentgamescore:
        print(f"{playergamescore} skor ile rakibin Antrosu Mağlup etmeyi başardın!")
    elif playergamescore == opponentgamescore:
        print("Oyunumuz beraberlik ile Sonuçlanıyor!")
    else:
        print(f"{opponentgamescore} skor ile rakibin seni yendi!")
tas_kagit_makas_MERT_OZYARDIMCI()

