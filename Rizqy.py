'''
Pakettt

'''

import math
'''
Oil Viscosity
'''
#Beggs-Robinson
def oil_viscosity(T, oil_SG):
    x = T**(-1.163)*math.exp(13.108-(6.591/oil_SG))
    
    muoil = (10**x) - 1
    return muoil


'''
Oil Formation Volume Factor(Bo)
'''

#Vasquez-Beggs

#Solution Gas Oil Ratio
def oil_Rso(P, Yo, T, Tsep, Psep, g):
    if Yo <= 30:
        c1 = 0.0362
        c2 = 1.0937
        c3 = 25.7240
    else:
        c1 = 0.0178
        c2 = 1.1870
        c3 = 23.9310

    yg100 = g*(1.0 + 5.912*10**(-5)*Yo*Tsep*math.log(Psep/114.7))

    Rso = c1*yg100*(P**c2)*math.exp(c3*(Yo/(T+460)))

    return Rso


#bubble point pressure
def Pb(Yo, T, g, Rso):
    if Yo <= 30:
        c1 = 0.0362
        c3 = 25.7240
    else:
        c1 = 0.0178        
        c3 = 23.9310

    pbp = (Rso/(c1*g*math.exp(c3*(Yo/(T+460)))))

    return pbp


#Oil formation volume factor
def oil_fvf(Yo, T, g, Rso):
    if Yo <= 30:
        A1 = 4.677*10**(-4)
        A2 = 1.751*10**(-5)
        A3 = -1.811*10**(-8)


    else:
        A1 = 4.670*10**(-4)
        A2 = 1.100*10**(-5)
        A3 = 1.337*10**(-9)


    Bo = 1 + A1*Rso + A2*(T-60)*(Yo/g) + A3*Rso*(T-60)*(Yo/g)

    return Bo


#Compressibility Factor
def oil_co(P, Yo, T, g, Rso):
    co = ((-1433 + 5*Rso+ 17.2*T - 1180*g + 12.61*Yo)/10**5*P)
    return co

# Oil formation volume factor undersaturated
def oil_fvf_undersat(P, co, Pb, Bo):
    Boo = Bo*math.exp(co*(Pb - P))
    return Boo





