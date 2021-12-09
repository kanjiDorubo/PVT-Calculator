'''

'''
import math

'''
Apparent molecular weight (Ma)
''' 
def Mg(gas_SG):
    return 28.967*gas_SG # dimensionless
'''
gas density
using real gas equation
'''
def gas_density(Pres,Mg,Z,Tres): # pure component
    return (Pres*Mg)/(10.731*Z*Tres) # lb/ft3

'''
Gas Viscosity
Using Lee-Gonzalez-Eakin
Input: Gas density, res.temp., Molecular weight
'''

def gas_viscosity(gas_density,Tres,Mg):
    K=((9.4+0.02*Mg)*(Tres**1.5))/(209+Tres+19*Mg)
    X=3.5+986/T+0.01*Mg
    Y=2.4-0.2*X
    
    mu = 0.0001*K*math.exp(X*((gas_density/62.4)**Y))
    return mu # cP

'''
Gas Formation Volume Factor
Input: res.temp., res.pressure, Z
'''
def Bg(Z,Tres,Pres):
    return 0.0052*(Z*Tres)/Pres

'''
Gas Isothermal compressibility
Input: res.temp., res.pressure, Z
'''

def Cg(Tpr,Ppr,Z):  
    rho=(0.27*Ppr)/(Z*Tpr)
    
    A1=0.31506237
    A2=-1.0467099
    A3=-0.57832720
    A4=0.53530771
    A5=-0.61232032
    A6=-0.10488813
    A7=0.68157001
    A8=0.68446549
    
    T1=A1+A2/Tpr+A3/(Tpr)**3
    T2=A4+A5/Tpr
    T3=A5*A6/Tpr
    T4=A7/(Tpr)**3
    
    partZ_to_pseudo_density = T1 + 2*T2*rho + 5*T3*(rho**4) + 2*T4*rho*(1 + A8*(rho**2)-(A8**2)*(rho**4))*math.exp(-A8*rho**2)
    return 1/Ppr-(0.27/((Z**2)*Tpr))*(partZ_to_pseudo_density/(1+(rho/Z)*partZ_to_pseudo_density))

'''
Oil density
using standing
Input
'''

def oil_density(oil_SG,gas_SG,Rs,Tres):
    pembilang=62.4279*oil_SG+0.0136*Rs*gas_SG
    penyebut=0.972+0.000147*(Rs*(gas_SG/oil_SG)**0.5+1.25*(Tres-460))**1.75
    return pembilang/penyebut # lb/bbl