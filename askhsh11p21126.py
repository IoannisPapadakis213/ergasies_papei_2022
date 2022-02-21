from scipy.stats import entropy as en
from urllib.request import Request, urlopen
import pandas as pd
sum=0
print("Τα αποτελεσματα των 20 τελευταίων γυρων είναι")
for bhma in range(20,0,-1):
    req = Request('https://drand.cloudflare.com/public/'+str(bhma), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    txt=str(data)
    t1=txt.split('"randomness":',1)
    t2=str(t1[1])
    t3=t2.split(",",1)
    t4=int((t3[0][-65:-1]),16)
    print("-----------------------")
    print("Για τον "+str(bhma)+"o γύρο")
    print("ΟΙ ΑΡΙΘΜΟΙ ΤΟΥ ΠΕΔΙΟΥ RANDOMNESS:",t3[0][-65:-1])
    print("TO ΑΚΕΡΑΙΟ ΜΕΡΟΣ ΤΟΥ:",t4)
    print("ΤΟ ΔΕΚΑΕΞΑΔΙΚΟ:",hex(t4))
    print("-------------------------")  
print("!!!ΕΝΤΡΟΠΙΑ!!!")
t4=pd.Series(t4)
data=t4.value_counts()
print(en(data))


    
