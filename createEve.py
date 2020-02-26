# Name: Austin Dominguez
# Name: Jeff Kunz

import photon

import random
import numpy

n = 100 # number of photons
avgPhotonNum = 'random.uniform(.75, 3)' # <1% qber and ~425-500 kbps at ~6
probDarkCount = 'random.uniform(.15, .5)' # <1% qber and ~425-500 kbsp at ~.04
sampleDenom = 4 # samples 1 out of x bits
# Alice --------------------------------------------

# Alice generates the raw key.
keyAlice = ""
for i in range(n): # Iterate over the number of photons.
    keyAlice += random.randint(0,1).__str__()

# Alice chooses the encoding basis for each key bit.
# This should be a string of '+'s and 'x's with '+'=H/V, 'x'=D/A.
basisAlice = ""
for i in range(n):
    basisAlice += '+' if random.randint(0,1) == 0 else 'x'

# Alice selects a photon state according to the key and basis.
# This should be a string of the characters 'H', 'V', 'D', 'A'.
photonAlice = ""
for i in range(n):
    case = (keyAlice[i], basisAlice[i])
    switcher = {
        ('0', '+'): 'H',
        ('1', '+'): 'V',
        ('0', 'x'): 'D',
        ('1', 'x'): 'A'
    }
    photonAlice += switcher.get(case)

# Alice prepares and sends each photon.
# Use the methods of the Photon class to prepare each photon.
photonArray = [photon.Photon() for i in range(n)]
for i in range(n):
    case = (keyAlice[i], basisAlice[i])
    switcher = {
        ('0', '+'): photonArray[i].prepareH,
        ('1', '+'): photonArray[i].prepareV,
        ('0', 'x'): photonArray[i].prepareD,
        ('1', 'x'): photonArray[i].prepareA
    }
    avgPhotonNumTemp = eval(avgPhotonNum)
    switcher.get(case)(avgPhotonNumTemp)


# Eve   --------------------------------------------

# You should implement this section after completing Alice and Bob.
# Eve is allowed to do whatever she wants to the photonAlice array.
# She cannot, however, have knowledge of Alice's or Bob's choice of bases, 
# nor Bob's measurement outcomes, until they are publicly announced.

# Eve selects a subsample of photons from Alice to measure.
# interceptIndex should be a string of n characters.
# Use the convention '0'=ignored, '1'=intercepted
interceptIndex = ""
# TODO: Put your code here.
for i in range(n):
    interceptIndex += '1'


# Eve chooses a basis to measure each intercepted photon.
# basisEve should be a string of n characters.
# Use the convention '+'=H/V, 'x'=D/A, ' '=not measured
basisEve = ""
# TODO: Put your code here.
for i in range(n):
    if interceptIndex[i] == '1':
        basisEve += '+' if random.randint(0, 1) == 0 else 'x'
    else:
        basisEve += ' '


# Eve performs a measurement on each photon.
# outcomeEve should be a string of n characters.
# Use the convention 'H','V','D','A', ' '=not measured
outcomeEve = ""
# TODO: Put your code here.
for i in range(n):
    probDarkCountTemp_EVE = eval(probDarkCount)
    if basisEve[i] == '+':
        outcomeEve += photonArray[i].measureHV(probDarkCountTemp_EVE)
    elif basisEve[i] == 'x':
        outcomeEve += photonArray[i].measureDA(probDarkCountTemp_EVE)
    else:
        outcomeEve += ' '


# Eve resends photons to Bob.
# Be sure to handle the cases in which Eve gets an invalid measurement.
# TODO: Put your code here.
for i in range(n):
    if outcomeEve[i] == 'H':
        photonArray[i].prepareH(random.uniform(.75, 3))
    elif outcomeEve[i] == 'V':
        photonArray[i].prepareV(random.uniform(.75, 3))
    elif outcomeEve[i] == 'D':
        photonArray[i].prepareD(random.uniform(.75, 3))
    elif outcomeEve[i] == 'A':
        photonArray[i].prepareA(random.uniform(.75, 3))



# OPTIONAL: Put any other nasty tricks here.


# Bob   --------------------------------------------

# Bob chooses a basis to measure each photon.
# This should be a string of '+'s and 'x's with '+'=H/V, 'x'=D/A.
basisBob = ""
for i in range(n):
    basisBob += '+' if random.randint(0,1) == 0 else 'x'

# Bob performs a measurement on each photon.
# Use the methods of the Photon class to measure each photon.
# outcomeBob should be a string of n characters.
# Use the convention 'H','V','D','A', 'N', 'M'////// ' '=not measured
outcomeBob = ""
for i in range(n):
    probDarkCountTemp = eval(probDarkCount)
    outcomeBob += photonArray[i].measureHV(probDarkCountTemp) if basisBob[i] == '+' else photonArray[i].measureDA(probDarkCountTemp)

# Bob infers the raw key.
# keyBob should be a string of n characters.
# Use the convention '0', '1', '-'=invalid measurement
keyBob = ""
for i in range(n):
    switcher = {
        'M' : '-',
        'N' : '-',
        'H' : '0',
        'V' : '1',
        'D' : '0',
        'A' : '1'
    }
    keyBob += switcher.get(outcomeBob[i])


# -----------------------------------------------------------
# Alice and Bob now publicly announce which bases they chose.
# Bob also announces which of his measurements were invalid.
# -----------------------------------------------------------


# Alice & Bob ----------------------------------------------------------

# Alice and Bob extract their sifted keys.
# siftedAlice and siftedBob should be strings of length n.
# Use the convention '0', '1', ' '=removed
siftedAlice = ""
siftedBob   = ""
for i in range(n):
    if basisAlice[i] == basisBob[i] and keyBob[i] != '-':
        siftedAlice += keyAlice[i]
        siftedBob += keyBob[i]
    else:
        siftedAlice += ' '
        siftedBob += ' '

# Alice and Bob use a portion of their sifted keys to estimate the quantum bit error rate (QBER).
# sampleIndex should be a string of n characters.
# Use the convention '0'=ignored, '1'=sampled
# The QBER is the fraction of mismatches within the sampled portion.
# For large samples, it should be close to the actual QBER,
# which Alice and Bob, of course, do not know.
sampleIndex = ""
sampledBobQBER = 0
sampledBobDenom = 0
#sampleIndex = '0' * n
#"""
for i in range(n):
    value = random.randint(0,sampleDenom) 
    if(siftedAlice[i] != ' '):
        sampleIndex += '1' if value == 0 else '0'
        if(value == 0):
            sampledBobDenom += 1
            if(siftedBob[i] != siftedAlice[i]):
                sampledBobQBER += 1
    else:
        sampleIndex += '0'
if(sampledBobDenom > 0):
    sampledBobQBER = sampledBobQBER / sampledBobDenom
#"""
# Alice and Bob remove the portion of their sifted keys that was sampled.
# Since a portion of the sifted key was publicly revealed, it cannot be used.
# secureAlice and secureBob should be strings of length n.
# Use the convention '0', '1', ' '=removed
secureAlice = ""
secureBob = ""
for i in range(n):
    if(sampleIndex[i] == '1'):
        secureAlice += ' '
        secureBob += ' '
    else:
        secureAlice += siftedAlice[i]
        secureBob += siftedBob[i]

# Alice and Bob make a hard determination whether the channel is secure.
# If it looks like there's something fishy, better hit the kill switch!
channelSecure = True # default value, to be changed to False if Eve suspected



# Eve ------------------------------------------------------------------

# Eve infers the raw key.
# keyEve should be a string of n characters.
# Use the convention '0', '1', '-'=invalid measurement, ' '=not measured
keyEve = ""
# TODO: Put your code here.
for i in range(n):
    if outcomeEve[i] == 'H' or outcomeEve[i] == 'D':
        keyEve += '0'
    elif outcomeEve[i] == 'V' or outcomeEve[i] == 'A':
        keyEve += '1'
    else:
        keyEve += '-'
# Eve extracts her sifted key.
# Knowing what Alice and Bob have publically revealed, Eve
# now selects which portion of her sifted key to keep.
# stolenEve should be strings of length n.
# Use the '0', '1', ' '=removed
stolenEve = ""
# TODO: Put your code here.
for i in range(n):
    if sampleIndex[i] == '1':
        stolenEve +=  ' '
    else:
        stolenEve += keyEve[i]
# ANALYSIS -------------------------------------------------------------

# Below is a standard set of metrics to evaluate each protocol.
# You need not change any of what follows.

# Compare Alice and Bob's sifted keys.
numMatchBob = 0
actualBobQBER = 0
secureKeyRateBob = 0
secureKeyLengthBob = 0
for i in range(len(secureAlice)):
    if secureAlice[i] != ' ':
       secureKeyLengthBob += 1
       if secureAlice[i] == secureBob[i]:
           numMatchBob += 1

# Compute the actual quantum bit error rate for Bob.
if secureKeyLengthBob > 0:
    actualBobQBER = 1 - numMatchBob / secureKeyLengthBob
else:
    actualBobQBER = float('nan')
# Compute the secure key rate, assuming each trial takes 1 microsecond.
secureKeyRateBob = (1-actualBobQBER) * secureKeyLengthBob / n * 1e6;

# Compare Alice and Eve's sifted keys.
numMatchEve = 0
actualEveQBER = 0
stolenKeyRateEve = 0
stolenKeyLengthEve = 0
for i in range(len(stolenEve)):
    if stolenEve[i] != ' ':
       stolenKeyLengthEve += 1
       if secureAlice[i] == stolenEve[i]:
           numMatchEve += 1
# Compute the actual quantum bit error rate for Eve.
if stolenKeyLengthEve > 0:
    actualEveQBER = 1 - numMatchEve / stolenKeyLengthEve
else:
    actualEveQBER = float('nan')
# Compute the stolen key rate, assuming each trial takes 1 microsecond.
stolenKeyRateEve = (1-actualEveQBER) * stolenKeyLengthEve / n * 1e6;


# DISPLAY RESULTS ------------------------------------------------------

print("")
print("basisAlice  = " + basisAlice)
print("basisBob    = " + basisBob)
print("basisEve    = " + basisEve)
print("")
print("keyAlice    = " + keyAlice)
print("keyBob      = " + keyBob)
print("keyEve      = " + keyEve)
print("")
print("siftedAlice = " + siftedAlice)
print("siftedBob   = " + siftedBob)
print("")
print("secureAlice = " + secureAlice)
print("secureBob   = " + secureBob)
print("stolenEve   = " + stolenEve)
print("")
if not channelSecure:
    secureKeyRateBob = 0;
    stolenKeyRateEve = 0;
    print("*********************************************")
    print("* ALERT! The quantum channel is not secure. *")
    print("*********************************************")
    print("")
print("sampledBobQBER = " + str(sampledBobQBER))
print("actualBobQBER  = " + str(actualBobQBER))
print("actualEveQBER  = " + str(actualEveQBER))
print("")
print("secureKeyRateBob = " + str(secureKeyRateBob/1000) + " kbps")
print("stolenKeyRateEve = " + str(stolenKeyRateEve/1000) + " kbps")

# Your goal is to maximize secureKeyRateBob and minimize stolenKeyRateEve.