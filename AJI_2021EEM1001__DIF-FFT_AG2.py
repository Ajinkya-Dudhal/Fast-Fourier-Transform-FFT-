#DIF FFT code
#Ajinkya Dudhal_2021EEM1001_Assigment-2
import math
import cmath

#Taking Input sequence from user
N=int(input("Enter number elements in sequence="))
y=[]
for i in range(0,N):
    x=int(input("Enter element{}=".format(i)))
    y.append(x)
print("Input sequence x[n]=",y)

#Calculating number of stages in Butterfly diagram
m=int(math.log(N,2))
if (m%round(m))!=0:
    if (m%round(m))<0.5:
        m=round(m+1)
    else:
        m=round(m)

#Butterfly diagram algorithm for DIF FFT in 'm' stages 
lo=[]
for i in range(m-1,-1,-1):
    for j in range(0,N-1,pow(2,i+1)):
        for k in range(pow(2,i)):
            r=y[j+k]+y[j+k+pow(2,i)]
            lo.append(r)
        for k in range(pow(2,i)):
            z=complex(0,(-2*3.14*k)/pow(2,i+1))     #Twiddle factor calculation
            r=y[j+k]-y[j+k+pow(2,i)]
            r=r*cmath.exp(z)
            lo.append(r)
    print("Output sequence of Stage{}={}\n".format(m-i,lo))     #Output sequence at each stage
    y=[]
    y=lo
    lo=[]

#Decimal to binary conversion of index and bit reversal logic
lo=[]
for k in range(0,N):
    i=k
    bin=[]
    while i!=0:
        p=i%2
        bin.append(p)
        i=i//2
    bin.reverse()
    l=len(bin)
    if l!=m:
        zeros=m-l
        while zeros!=0:
            bin.insert(0,0)
            zeros=zeros-1

#Binary to decimal conversion of index
    dec=0
    for j in range(int(m)):
        dec=dec+(bin[j]*pow(2,j))
    element=y[dec]
    lo.append(element)
print("Output DFT sequence X(k)=",lo)