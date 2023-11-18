from random import randint

hitung_kepala = 0
hitung_buntut = 0
hitung_total = 0

jumlah_hitung = 10000000

while True:
  
  # angka integer acak: 0 atau 1
  putar  = randint(0,1)
  
  if putar:
    hitung_kepala  = hitung_kepala + 1
    #print (str(hitung_total) + " kepala ")
  else:
    hitung_buntut = hitung_buntut + 1
    #print (str(hitung_total) + " buntut")
    
  hitung_total = hitung_total + 1

  if (hitung_total >= jumlah_hitung):
    break

print ("Muncul kepala " + str(hitung_kepala) + " kali berturut-turut.")
print ("Muncul buntut " + str(hitung_buntut) + " kali berturut-turut.")
persentase_kepala = (hitung_kepala / jumlah_hitung) * 100
persentase_ekor = (hitung_buntut / jumlah_hitung) * 100
print ("Muncul buntut " + str(persentase_ekor) + " kali berturut-turut.")
print ("Muncul kepala " + str(persentase_kepala) + " kali berturut-turut.")


