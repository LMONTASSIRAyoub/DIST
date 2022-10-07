
Z1=0.1
Z2=0.2
Z3=0.3
Z4=0.4
Tf=200
Pf=100
F=100
Eps=0
K1=4.2
K2=1.75
K3=0.74
K4=0.34
KSI=0.12188336443887338
Result=((Z1*(1-K1))/(1+KSI*(K1-1)))+((Z2*(1-K2))/(1+KSI*(K2-1)))+((Z3*(1-K3))/(1+KSI*(K3-1)))+((Z4*(1-K4))/(1+KSI*(K4-1)))
print("la résultat est : ",Result)
def RR(Z1,Z2,Z3,Z4,K1,K2,K3,K4):
    Result=((Z1*(1-K1))/(1+KSI*(K1-1)))+((Z2*(1-K2))/(1+KSI*(K2-1)))+((Z3*(1-K3))/(1+KSI*(K3-1)))+((Z4*(1-K4))/(1+KSI*(K4-1)))
    return Result
print(RR(Z1,Z2,Z3,Z4,K1,K2,K3,K4))
def RRD(Z1,Z2,Z3,Z4,K1,K2,K3,K4):
    Result1=((Z1*((1-K1)**(2))/(1+KSI*(K1-1))**(2))+(((Z2*(1-K2)**(2)))/((1+KSI*(K2-1))**(2)))+((Z3*(1-K3)**(2)))/((1+KSI*(K3-1))**(2))+((Z4*(1-K4)**(2)))/((1+KSI*(K4-1))**(2)))
    return Result1
Fenctobj=RR(Z1,Z2,Z3,Z4,K1,K2,K3,K4)
N=float(input("Numbre iteration"))
while (Eps<=N):
    KSI1=KSI-(Fenctobj/(RRD(Z1,Z2,Z3,Z4,K1,K2,K3,K4)))
    print("root",KSI1,"at iteration",Eps)
    Eps=Eps+0.001
    KSI=KSI1
    #Fenctobj = RR(Z1, Z2, Z3, Z4, K1, K2, K3, K4)
    #print(Fenctobj,FKSI)





