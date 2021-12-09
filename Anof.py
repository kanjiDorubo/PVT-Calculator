from math import exp
from Functions import newton_raphson
import matplotlib.pyplot as plt
import numpy as np
# Ppc & Tpc in °R (rankine)
# Sutton
# Misc Standing
# Condensate Standing
# + corrected

cmd = ['Sutton', 'Misc Standing', 'Condensate Standing']
#===============
# Ppc
def Ppc(gas_SG, corr):
	if corr == "Sutton":
		return 756.8 - 131.07*gas_SG - 3.6*gas_SG**2

	elif corr == "Misc Standing":
		return 677 + 15*gas_SG - 37.5*(gas_SG**2)

	elif corr == "Condensate Standing":
		return 706 - 51.7*gas_SG - 11.1*gas_SG**2

#==================
# Tpc
def Tpc(gas_SG, corr):
	if corr == "Sutton":
		return 169.2 + 349.5*gas_SG - 74*gas_SG**2

	elif corr == "Misc Standing":
		return 168 + 325*gas_SG - 12.5*gas_SG**2

	elif corr == "Condensate Standing":
		return 187 + 330*gas_SG - 71.5*gas_SG**2

#===================
# Corrected values
def Tpc_corr(Tpc, gas_SG, yH2S, yCO2): # yH2S, yCO2: float; gas_SG: float
	A = yCO2 + yH2S
	epsilon = 120*(A**0.9 - A**1.6) + 15*(yH2S**0.5 - yH2S**4)

	return Tpc - epsilon

def Ppc_corr(Ppc, Tpc, gas_SG, yH2S, yCO2): # yH2S, yCO2: float; gas_SG: float
	Tpc_corr_ = Tpc_corr(Tpc, gas_SG, yH2S, yCO2)
	A = yCO2 + yH2S
	epsilon = 120*(A**0.9 - A**1.6) + 15*(yH2S**0.5 - yH2S**4)

	return (Ppc * Tpc_corr_)/(Tpc + yH2S*(1-yH2S)*epsilon) 

#==============
# Compressibility Factor (Z)
# Dranchuk-Abou-Kassem w/ iteration
def DranchukAbouKassem(Ppr, Tpr):
    A1 = 0.3265
    A2 = -1.07
    A3 = -0.5339
    A4 = 0.01569
    A5 = -0.05165
    A6 = 0.5475
    A7 = -0.7361
    A8 = 0.1844
    A9 = 0.1056
    A10 = 0.6134
    A11 = 0.7210

    R1 = A1 + A2/Tpr + A3/(Tpr**3) + A4/(Tpr**4) + A5/(Tpr**5)
    R2 = 0.27*Ppr/Tpr
    R3 = A6 + A7/Tpr + A8/(Tpr**2)
    R4 = A9*(A7/Tpr + A8/Tpr**2)
    R5 = A10/(Tpr**3)

    # estimate rho_r thru iteration, find root of f(rho_r), dapet rho_r, masuk ke rho_r = 0.27 Ppr/zTpr
    # define the Dranchuk Abuo Kassem function for root-finding
    # rho_r := x
    f = lambda y: 1 + R1*y - R2/y + R3*y**2 - R4*y**5 + (R5*y**2 * (1 + A11*y**2) * exp(-A11*y**2))
    y0 = R1 * R4
    # y0 = 5
    # find the root
    rho_r = newton_raphson(f, y0)

    Z = 0.27 * Ppr / (rho_r * Tpr)

    return Z
#===============
corr = cmd[2] # Cond Standing

gas_SG = 0.7
yH2S = 0.1
yCO2 = 0.05

_Ppc = Ppc(gas_SG, corr=corr) 
_Tpc = Tpc(gas_SG, corr=corr)

print(DranchukAbouKassem(1.3, 1.5))


# print(f"Ppc: {_Ppc}")
# print(f"Tpc: {_Tpc}")
# print("===")
# print(f"P`pc: {Ppc_corr(Ppc=_Ppc, Tpc=_Tpc, gas_SG=gas_SG, yCO2=yCO2, yH2S=yH2S)}")
# print(f"T`pc: {Tpc_corr(Tpc=_Tpc, gas_SG=gas_SG, yCO2=yCO2, yH2S=yH2S)}")
# print("===")
