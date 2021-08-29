import numpy as np

n=int(input("kaç departman var?:"))
y=0
dt=0

malzemeakis=np.array([[0]*n]*n,dtype=float)
malzemeakis=malzemeakis.reshape(n,n)
print("MALZEME AKIŞI BOŞ TABLO:\n",malzemeakis)

for i in range(0,n):
    for j in range(0,n):
        if malzemeakis[i,j]==0:
            if i==j:
                malzemeakis[i,j]=0
            else:
                malzemeakis[i,j]=float(input("değer:"))
                       
print("MALZEME AKIŞ TABLOSU:\n",malzemeakis)


while (True):
    amer=np.array([[0]*2]*n,dtype=float)
    amer=amer.reshape(n,2)
    print("AĞIRLIK MERKEZİ BOŞ TABLO:\n",amer)

    for i in range(0,n):
        for j in range(0,2):
            if amer[i,j]==0:
                amer[i,j]=float(input("değer:"))

    print("MALZEME AKIŞ TABLOSU:\n",malzemeakis)
                       
    print("AĞIRLIK MERKEZİ TABLOSU:\n",amer)

    uzaklik=np.array([[0]*n]*n,dtype=float)
    uzaklik=uzaklik.reshape(n,n)

    for i in range(0,n):
        for j in range(0,n):
                if i==j:
                    uzaklik[i,j]=0
                else:
                    uzaklik[i,j]= abs((amer[i,0]-amer[j,0]))+abs((amer[i,1]-amer[j,1]))
                    uzaklik[j,i]=float(uzaklik[i,j])
                       
    print("UZAKLIK TABLOSU:\n",uzaklik)

    mutoplam=0

    for i in range(0,n):
        for j in range(0,n):
        
            mutoplam = mutoplam + malzemeakis[i,j]*uzaklik[i,j]
    print("MEVCUT TOPLAM MALİYET:",mutoplam)


    for w in range(0,n):
        for q in range(0,n):
            if w!=q: 
                amer[w,0] , amer[w,1] , amer[q,0] , amer[q,1] = amer[q,0] , amer[q,1] , amer[w,0] , amer[w,1]
                for p in range(0,n):
                    for t in range(0,n):
                        if p==t:
                            uzaklik[p,t]=0
                        else:
                            uzaklik[p,t]= abs((amer[p,0]-amer[t,0]))+abs((amer[p,1]-amer[t,1]))
                            uzaklik[t,p]=float(uzaklik[p,t])
                smutoplam=0           
                for i in range(0,n):    
                    for j in range(0,n):        
        
                        smutoplam = smutoplam + malzemeakis[i,j]*uzaklik[i,j]
                amer[w,0] , amer[w,1] , amer[q,0] , amer[q,1] = amer[q,0] , amer[q,1] , amer[w,0] , amer[w,1]
            
                print("{}. ve".format(w+1),"{}. değiştiğinde :".format(q+1),smutoplam) 





 





