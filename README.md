# Algoritmo-RSA
Nombre: Emmanuel del Piero Martinez Salcedo

El presente código permite generar claves públicas y secretas para la encriptación de información usando el algoritmo RSA, en esta ocación el algoritmo imprimira una tabla con 6 variables: E, D, N, M, C, M2 donde C es la clave pública y M2 la clave privada

###Algoritmo RSA
En criptografía, RSA (Rivest, Shamir y Adleman) es un sistema criptográfico de clave pública desarrollado en 1979, que utiliza factorización de números enteros. Es el primer y más utilizado algoritmo de este tipo y es válido tanto para cifrar como para firmar digitalmente.

La seguridad de este algoritmo radica en el problema de la factorización de números enteros. Los mensajes enviados se representan mediante números, y el funcionamiento se basa en el producto, conocido, de dos números primos grandes elegidos al azar y mantenidos en secreto. Actualmente estos primos son del orden de 10^300, y se prevé que su tamaño siempre crezca con el aumento de la capacidad de cálculo de los ordenadores.

##Funcionamiento
El codigo esta inicializado con variables de 16 bits esto pues al iniciarlo con 64 gasta demasiado tiempo computacional. Así que lo he reducido a 16 para esta prueba
Para el funcionamiento estoy usando mis funciones creadas en previos proyectos que son: Euclides, EsCompuesto y MillerRabin y añado las nuevas funciones: PrimoRandBITS, phi, RSA_KEY_GENERATOR que sirven para generar un numero aleatorio de k bits, función phi de Euler y el generador de la clave RSA respectivamente

Para el experimento estoy usando una presición S de 4 para no usar mucho tiempo computacional.

##Código
```python
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
    d2=1
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

```
