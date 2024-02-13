

#! Genetik algoritmalar bir sezgisel algoritmalardır ve sezgisel algoritmalar Optimizasyon işlemlerinde kullanılırlar 
# Sezigisel Algoritmalarda en ideal değil ideal'e en yakın aranır. !!!!!!
#* Optimizasyon : Bir işi daha az maliyetle ve daha fazla verimlilikle yapmabilmeyi hedefler 

#? 1-) Popülasyon : Olası çözüm bilgilerini ifade eden bireylerin tamamımana verilen isimdir 
#? 2-) Kromozon   : Popülasyondaki her bireyin ismi  Kromozondur
#? 3-) Gen        : Bir popülasyon içinde farklı aday çözümlerini temsil eder 
#? 4-) Çaprazlama : Seçilmiş iki kromozounun belirlenmiş bir kuralla yeni bir gen oluşturmasıdır.
#? 5-) Mutasyon   : Yeni özelliklerin ortaya çıkmasını sağlamak amacıyla kullanılır.Belirli genlerin özellikleri rasgele olarak değiştirilir. Fazla mutasyon popülasyonumuza zarar verebilir


import numpy as np 
import random as rnd 

iterasyon = 100 
cross_over_rate = 0.75
pop_size = 6
gen_size =4


def kromozon_olustur():
    return [rnd.randint(0,30) for gen in range(0,gen_size)]

def baslangic_populasyonunu_olustur():
    return [kromozon_olustur() for i in range(0,pop_size)]

def fitness(kromozon):
    return 1/(1+abs((kromozon[0]+kromozon[1]*2+kromozon[2]*3+kromozon[3]*4)-30))

# Populasyondaki tüm kromozon fitness değerlerini gonderez
def olasilik_hesapla(fitness_degerleri): 
    P =[]
    
    total = sum(fitness_degerleri)
    for f in fitness_degerleri:
        P.append(f/total)
    return P

def gen_degisimi(kr1,kr2):
    yeni_kr1 = []
    yeni_kr2 = []
    c = rnd.randint(1,gen_size-1)
    
    yeni_kr1[:c] = kr2[:c]
    yeni_kr1[c:] = kr1[c:]
    
    yeni_kr2[:c] = kr1[:c]
    yeni_kr2[c:] = kr2[c:]
    return yeni_kr1,yeni_kr2

# Mutasyona ugrayacak kromozonu parametre olarak alıyoruz 
def mutasyon(mut):
    temp= []
    temp = mut[:] # mutasyona ugrayacak kromozonun tüm genlerini aktarıyoruz
    
    gen = rnd.randint(0,30)
    index = rnd.randint(0,gen_size-1)
    temp[index] = gen
    return temp


# F(x1,x2,x3,x4) = (x1 + x2 * 2 + x3 * 3 + x4 *4 ) -30 
#* denkleminin sonucunu sıfır yapan x1,x2,x3,x4 değerleri nedir ?

populasyon = baslangic_populasyonunu_olustur()
fitness_degeleri = []

for kromozon in populasyon:
    fitness_degeleri.append(fitness(kromozon))
    

epok = 0
while(epok<iterasyon):
    P = olasilik_hesapla(fitness_degeleri)
    C = np.cumsum(P) #* kümülatif toplam yapıyor Yani Tüm fitness değerlerini 0. indexten başlayarak toplaya toplaya son indexe kadar gidiyor
    
    rulet_parents = []
    for i in range(0,len(C)):
        r =rnd.random()
        for j in range(0,len(C)):
            if C[j] > r:
                rulet_parents.append(j) # bulduğu ilk değerin indexini ekliyor 
                break
    
    croosover_parents = []
    k = 0
    while(k<pop_size):
        r = rnd.random()
        if (r<cross_over_rate):
            if(rulet_parents[k] not in croosover_parents):
                croosover_parents.append(rulet_parents[k])
        k = k+1
    #print(len(rulet_parents)," ",len(croosover_parents))
    if(len(croosover_parents)>1):
        for i in range(0,len(croosover_parents)):
            for j in range(i+1,len(croosover_parents)):
                
                kr1 , kr2 = gen_degisimi(populasyon[croosover_parents[i]],populasyon[croosover_parents[j]])
                #print(kr1,' ',kr2)
    else :
        print("Caprazlamadan birsey gelmedi.")
        
    for i in range(100):
        mut = mutasyon(populasyon[rnd.randint(0,len(populasyon)-1)])
        populasyon.append(mut)
        fitness_degeleri.append(fitness(mut))
    
    zip_list = zip(fitness_degeleri,populasyon)
    sort_list = sorted(zip_list,reverse=True)
    
    p_sayisi = len(populasyon)
    while(p_sayisi>pop_size):
        sort_list.pop()
        p_sayisi = p_sayisi - 1
    
    populasyon = []
    fitness_degeleri = []
    
    for j , i in list(sort_list):
        populasyon.append(i)
        fitness_degeleri.append(j)
    epok =epok+1 
for i, j in zip(populasyon,fitness_degeleri):
    print(i, " " , j)
    