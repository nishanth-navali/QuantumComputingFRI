import photon

import random
import numpy as np

print("")
print("Photon class test")

N = 10000
photon = photon.Photon()

print("\nVacuum")
numN = 0; numH = 0; numV = 0; numM = 0
for n in range(N):
    photon.prepareVacuum()
    outcome = photon.measureHV(0.3)
    if outcome == "N": numN += 1
    if outcome == "H": numH += 1
    if outcome == "V": numV += 1
    if outcome == "M": numM += 1
print("N: " + str(numN/N))
print("H: " + str(numH/N))
print("V: " + str(numV/N))
print("M: " + str(numM/N))

print("\nPhoton")
numN = 0; numH = 0; numV = 0; numM = 0
for n in range(N):
    photon.prepareH(1)
    outcome = photon.measureHV(0.3)
    if outcome == "N": numN += 1
    if outcome == "H": numH += 1
    if outcome == "V": numV += 1
    if outcome == "M": numM += 1
print("N: " + str(numN/N))
print("H: " + str(numH/N))
print("V: " + str(numV/N))
print("M: " + str(numM/N))

print("\nVacuum w/ Polarizer")
numN = 0; numH = 0; numV = 0; numM = 0
for n in range(N):
    photon.prepareVacuum()
    photon.applyPolarizer(0,0)
    outcome = photon.measureHV(0.3)
    if outcome == "N": numN += 1
    if outcome == "H": numH += 1
    if outcome == "V": numV += 1
    if outcome == "M": numM += 1
print("N: " + str(numN/N))
print("H: " + str(numH/N))
print("V: " + str(numV/N))
print("M: " + str(numM/N))

print("\nPhoton w/ Polarizer")
numN = 0; numR = 0; numL = 0; numM = 0
for n in range(N):
    photon.prepareL(2)
    photon.applyPolarizer(np.pi/4,-np.pi/2)
    outcome = photon.measureRL(0.3)
    if outcome == "N": numN += 1
    if outcome == "R": numR += 1
    if outcome == "L": numL += 1
    if outcome == "M": numM += 1
print("N: " + str(numN/N))
print("R: " + str(numR/N))
print("L: " + str(numL/N))
print("M: " + str(numM/N))

print("\nPhoton w/ NoisyGate")
numN = 0; numH = 0; numV = 0; numM = 0
for n in range(N):
    photon.prepareH(1)
    photon.applyNoisyGate(1)
    outcome = photon.measureHV(0.3)
    if outcome == "N": numN += 1
    if outcome == "H": numH += 1
    if outcome == "V": numV += 1
    if outcome == "M": numM += 1
print("N: " + str(numN/N))
print("H: " + str(numH/N))
print("V: " + str(numV/N))
print("M: " + str(numM/N))

print("\nPhoton w/ Attenuation")
numN = 0; numH = 0; numV = 0; numM = 0
for n in range(N):
    photon.prepareH(1)
    photon.applyAttenuation(1)
    outcome = photon.measureHV(0.3)
    if outcome == "N": numN += 1
    if outcome == "H": numH += 1
    if outcome == "V": numV += 1
    if outcome == "M": numM += 1
print("N: " + str(numN/N))
print("H: " + str(numH/N))
print("V: " + str(numV/N))
print("M: " + str(numM/N))

print("\nBorn Rule")
numH = 0; numV = 0
theta = np.arccos(1 - 2*random.uniform(0,1))
phi   = random.uniform(0,1)*2*np.pi
for n in range(N):
    photon.prepareH(1)
    photon.applyUnitaryGate(theta, phi, 0)
    outcome = photon.measureHV(0.1)
    if outcome == "H": numH += 1
    if outcome == "V": numV += 1
print(str(numH/(numH+numV)) + " (modeled) vs " + str(np.cos(theta/2)**2) + " (predicted)")
