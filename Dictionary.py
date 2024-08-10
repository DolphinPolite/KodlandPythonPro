from time import *
Number = 0
dictionary = {
    "HOMO SAPİENS": "Akıllı modern insan",
    "GEEZ": " 'Hadi ama' gibi anlamlara gelir",
    "NEANDERTALANSİS": "Başka bir insan türü",
    "MEME": "internet kültürü mizahı",
    "ANTİNENE": "internet kültürü mizahının tam tersini yapan ama yine de güldüren mizah türü",
    "MEGAZARAR ÖLÜM IŞINI": "Bilim kurgu kitabındaki bir ışın",
    "İHTİMALSİZLİK MOTORU": "İrrasyonel sayılar üreterek büyük enerji üreten bir bilim kurgu motoru"
}

print("MeyhaBBalar BNe sEvGiLi SöZlÜk prOGRamıı!!!! gELdİĞİN iÇin SağOL! ArTıK yaLnIz DeĞİLim Yuhiii!!!")
sleep(1)
print("SadEcE KeliMe GirCen Heee UNUTmA")
sleep(1)

while Number != 5:
    Number += 1

    word = input("AnLamaDıĞıN bİr Kelemi YaZ! (hEpSi Büyük HarfLe hEeEe!! (KüÇüK hARFlE yAZSAn BiLE büyük Saycamkine Heheheheh!)): ").upper()
    
    if word in dictionary.keys():
        print("TıMaM KeLİMe sÖZLüKtE vAR AnlaMı Şu:")
        print(dictionary[word])
    else:
        mean = input("kELİmeNin AnlaMInı Giysene: ")
        
        dictionary[word] = mean
    sleep(0.5)
        
print("GöRüŞÜrÜK sENİ öZLİcEM!! SöZlÜk PROgRaMı ÜzGün! üHÜHÜHÜH!")
