import random

def Euclides(n,m):
    if m==0:
        return n
    else:
        return Euclides(m,(n%m)) 

def EuclidesEXT(n,m):
    if m==0:
        return (n,1,0)
    else:
        (d,x2,y2)=EuclidesEXT(m, n%m)
        (x,y)=(y2,x2-(((n/m)-((n/m)%1))*y2))
        return(d,x,y)

def Inverso(a,n):
    if Euclides(a,n)==1:
        (d,x,y)=EuclidesEXT(a,n)
        return (int(x%n))

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
        a1 = random.randrange(2, n3)
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
    while True:
        p=PrimoRandBITS(int(k/2),4)
        q=PrimoRandBITS(int(k/2),4)
        if p==q:
            continue
        else:
            break

    n5=p*q
    φ=phi(p)*phi(q)
    
    while True:
        e=random.randrange(2,φ)
        if Euclides(e,φ)==1:
            break
        else:
            continue

    d2=Inverso(e,φ)
    return(n5,e,d2)

    
        
k1=16
esp='  '
print('E        / D      / N    / M     / C     / M2')
for i2 in range(10):
    (n_,e_,d_)=RSA_KEY_GENERATOR(k1)
    m_=random.randrange(0,n_)
    c_=(m_**e_)%n_
    m2_=c_**d_%n_
    print('{e_:<{E_width}}{esp}{d_:>{D_width}}{esp}{n_:>{N_width}}{esp}{m_:>{M_width}}{esp}{c_:>{C_width}}{esp}{m2_:>{M2_width}}'.format(
        e_=e_, E_width=len('aaaaaa'),
        esp=esp,
        d_=d_, D_width=len('aaaaaa'),
        n_=n_, N_width=len('aaaaaa'),
        m_=m_, M_width=len('aaaaaa'),
        c_=c_, C_width=len('aaaaaa'),
        m2_=m2_, M2_width=len('aaaaaa'),))
