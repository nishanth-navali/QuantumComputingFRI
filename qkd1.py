# TODO: Put your name here.
# Name: Nishanth Navali

import qubit

import random
import numpy

n = 10 # number of qubits

# Alice --------------------------------------------

# Alice generates the raw key.
keyAlice = ""
for i in range(n): # Iterate over the number of qubits.
    # Append a random character ('0' or '1') to the end.
    if random.randint(0,1)==0: # Flip a coin (0 or 1).
        keyAlice += '0'
    else:
        keyAlice += '1'
print("keyAlice    = " + keyAlice)

# Alice chooses the encoding basis for each key bit.
# This should be a string of '+'s and 'x's with '+'=H/V, 'x'=D/A.
basisAlice = ""
# My code
for i in range(n):
    if random.randint(0, 1) == 0:  # Flip a coin (0 or 1).
        basisAlice += '+'
    else:
        basisAlice += 'x'
print("basisAlice  = " + basisAlice)

# Alice selects a qubit state according to the key and basis.
# This should be a string of the characters 'H', 'V', 'D', 'A'.
qubitAlice = ""
# TODO: Put your code here.
for i in range(n):
    if(keyAlice[i] == '0'):
        if(basisAlice[i] == '+'):
            qubitAlice += 'H'
        elif(basisAlice[i] == 'x'):
            qubitAlice += 'D'
    elif(keyAlice[i] == '1'):
        if (basisAlice[i] == '+'):
            qubitAlice += 'V'
        elif (basisAlice[i] == 'x'):
            qubitAlice += 'A'

print("qubitAlice  = " + qubitAlice)

# Alice prepares and sends each qubit.
# Use the methods of the Qubit class to prepare each qubit.
qubitArray = [qubit.Qubit() for i in range(n)]
# TODO: Put your code here.
for i in range(n):
    if qubitAlice[i] == 'H':
        qubitArray[i].prepareH()
    elif qubitAlice[i] == 'V':
        qubitArray[i].prepareV()
    elif qubitAlice[i] == 'D':
        qubitArray[i].prepareD()
    else:
        qubitArray[i].prepareA()
# Eve   --------------------------------------------
# You should implement this section after completing Alice and Bob.

# Eve chooses a basis to measure each qubit.
basisEve = ""
# TODO: Put your code here.
for i in range(n):
    if random.randint(0, 1) == 0:  # Flip a coin (0 or 1).
        basisEve += '+'
    else:
        basisEve += 'x'
print("basisEve    = " + basisEve)

# Eve performs a measurement on each qubit.
# (This is similar to what Bob does.)
outcomeEve = ""
# TODO: Put your code here.
for i in range(n):
    if basisEve[i] == '+':
        outcomeEve += qubitArray[i].measureHV()
    else:
        outcomeEve += qubitArray[i].measureDA()
print("outcomeEve  = " + outcomeEve)

# Eve resends qubits to Bob.
# (This is similar to what Alice does.)
# TODO: Put your code here.
for i in range(n):
    if outcomeEve[i] == 'H':
        qubitArray[i].prepareH()
    elif outcomeEve[i] == 'V':
        qubitArray[i].prepareV()
    elif outcomeEve[i] == 'D':
        qubitArray[i].prepareD()
    else:
        qubitArray[i].prepareA()

# Bob   --------------------------------------------

# Bob chooses a basis to measure each qubit.
# (This is similar to what Alice does.)
basisBob = ""
# TODO: Put your code here.
for i in range(n):
    if random.randint(0, 1) == 0:  # Flip a coin (0 or 1).
        basisBob += '+'
    else:
        basisBob += 'x'
print("basisBob    = " + basisBob)

# Bob performs a measurement on each qubit.
# Use the methods of the Qubit class to measure each qubit.
outcomeBob = ""
# TODO: Put your code here.
for i in range(n):
    if basisBob[i] == '+':
        outcomeBob += qubitArray[i].measureHV()
    else:
        outcomeBob += qubitArray[i].measureDA()
print("outcomeBob  = " + outcomeBob)
# This should be a string of the characters 'H', 'V', 'D', 'A'.

# Bob infers the raw key.
keyBob = ""
# TODO: Put your code here.
for i in range(n):
    if outcomeBob[i] == 'H' or outcomeBob[i] == 'D':
        keyBob += '0'
    else:
        keyBob += '1'
print("keyBob      = " + keyBob)
# Only about half of Bob's raw key with match Alice's raw key.


# -----------------------------------------------------------
# Alice and Bob now publicly announce which bases they chose.
# -----------------------------------------------------------


# Alice and Bob extract their sifted keys.
siftedAlice = ""
siftedBob   = ""
# TODO: Put your code here.
for i in range (n):
    if basisAlice[i] == basisBob[i]:
        siftedAlice += keyAlice[i]
        siftedBob += keyBob[i]
print("siftedAlice = " + siftedAlice)
print("siftedBob   = " + siftedBob)


# Compare Alice and Bob's sifted keys.
numMatch = 0
if len(siftedAlice) != len(siftedBob):
    print("Sifted keys are different lengths!")
else:
    for i in range(len(siftedAlice)):
        if siftedAlice[i] == siftedBob[i]:
           numMatch += 1
    matchPercent = numMatch / len(siftedAlice) * 100
print(str(matchPercent) + "% match")

# Without Eve, you should expect a 100% match.
# With Eve present, this will drop to about 75%.
# (Using a larger value of n will give better statistics.)

# Sample Output ---------------------------------------------
# keyAlice    = 0101100000
# basisAlice  = +x+x++++x+
# qubitAlice  = HAHAVHHHDH
# basisEve    = x++xx+x+++
# outcomeEve  = DVHADHAHHH
# basisBob    = x+xx+x++xx
# outcomeBob  = DVDAHDVHDA
# keyBob      = 0101001001
# siftedAlice = 11000
# siftedBob   = 10100
# 60.0% match
# -----------------------------------------------------------
