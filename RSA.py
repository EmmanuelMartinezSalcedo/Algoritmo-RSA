import random

def Euclides(n,m):
    if m==0:
        return n
    else:
        return Euclides(m,(n%m)) 

def EsCompuesto(a,n2,t,u):
    x= pow(a,u,n2)
    if x == 1 or x == n2 - 1:
        return False
    for i in range(t-1):
        x=pow(x, 2,n2)
        if x == n2 - 1:
            return False
    return True

def MillerRabin(n3,s):
    t2=0
    u2=n3-1
    while u2 % 2 == 0:
        u2 = u2 // 2
        t2 = t2 + 1
    for i in range(s):
        a1 = random.randrange(2, n3 - 1)
        if EsCompuesto(a1,n3,t2,u2) == True:
            return False
    return True
def PrimoRandBITS(k,s2):
    while True:
        r=random.randrange(2,pow(2,k),2)
        r=r+1
        aux=MillerRabin(r,s2)
        if aux==True:
            break
        else:
            continue
    return r

def phi(n4):
    r=0
    for i in range(1,n4):
        d=Euclides(i,n4)
        if d==1:
            r=r+1
    return r

def RSA_KEY_GENERATOR(k):
    d2=0
    while True:
        p=PrimoRandBITS(int(k/2),4)
        q=PrimoRandBITS(int(k/2),4)
        if p==q:
            continue
        else:
            break
    n5=p*q
    n5=phi(n5)
    while True:
        e=random.randrange(2,n5-1)
        if Euclides(e,n5)==1:
            break
        else:
            continue

    for i in range(1,e):
        aux2=round(((i*e)-1)/n5,3)
        if aux2-int(aux2)==0.000:
            aux2=int(aux2)
        if isinstance(aux2,int)==True:
            d2=i
            break
        else:
            continue

    return(n5,e,d2)

    
        
k1=16
esp='  '
print('Lista E / D / N / M / C / M2')
for i2 in range(10):
    (N,E,D)=RSA_KEY_GENERATOR(k1)
    M=random.randrange(2,pow(2,k1))
    C=(pow(M,E))%N
    M2=(pow(C,D))%N
    print('{E:<{E_width}}{esp}{D:>{D_width}}{esp}{N:>{N_width}}{esp}{M:>{M_width}}{esp}{C:>{C_width}}{esp}{M2:>{M2_width}}'.format(
        E=E, E_width=len('aaaaaa'),
        esp=esp,
        D=D, D_width=len('aaaaaa'),
        N=N, N_width=len('aaaaaa'),
        M=M, M_width=len('aaaaaa'),
        C=D, C_width=len('aaaaaa'),
        M2=D, M2_width=len('aaaaaa'),))
