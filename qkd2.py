# Name: Nishanth Navali
# Name: Jordan Conklin

import photon

import random
import numpy

n = 1000 # number of photons

# Alice --------------------------------------------

# Alice generates the raw key.
keyAlice = ""
for i in range(n): # Iterate over the number of photons.
    # Append a random character ('0' or '1') to the end.
    if random.randint(0,1)==0: # Flip a coin (0 or 1).
        keyAlice += '0'
    else:
        keyAlice += '1'

# Alice chooses the encoding basis for each key bit.
# This should be a string of '+'s and 'x's with '+'=H/V, 'x'=D/A.
basisAlice = ""

for i in range(n):
    if random.randint(0, 1) == 0:  # Flip a coin (0 or 1).
        basisAlice += '+'
    else:
        basisAlice += 'x'

# Alice selects a photon state according to the key and basis.
# This should be a string of the characters 'H', 'V', 'D', 'A'.
photonAlice = ""
for i in range(n):
    if keyAlice[i] == '0':
        if basisAlice[i] == '+':
            photonAlice += 'H'
        elif basisAlice[i] == 'x':
            photonAlice += 'D'
    elif keyAlice[i] == '1':
        if  basisAlice[i] == '+':
            photonAlice += 'V'
        elif basisAlice[i] == 'x':
            photonAlice += 'A'

# Alice prepares and sends each photon.
# Use the methods of the Photon class to prepare each photon.
photonArray = [photon.Photon() for i in range(n)]
# TODO: Put your code here.
for i in range(n):
    if photonAlice[i] == 'H':
        photonArray[i].prepareH(1)
    elif photonAlice[i] == 'V':
        photonArray[i].prepareV(1)
    elif photonAlice[i] == 'D':
        photonArray[i].prepareD(1)
    elif photonAlice[i] == 'A':
        photonArray[i].prepareA(1)

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

# Eve chooses a basis to measure each intercepted photon.
# basisEve should be a string of n characters.
# Use the convention '+'=H/V, 'x'=D/A, ' '=not measured
basisEve = ""
# TODO: Put your code here.

# Eve performs a measurement on each photon.
# outcomeEve should be a string of n characters.
# Use the convention 'H','V','D','A', ' '=not measured
outcomeEve = ""
# TODO: Put your code here.

# Eve resends photons to Bob.
# Be sure to handle the cases in which Eve gets an invalid measurement.
# TODO: Put your code here.

# OPTIONAL: Put any other nasty tricks here.


# Bob   --------------------------------------------

# Bob chooses a basis to measure each photon.
# This should be a string of '+'s and 'x's with '+'=H/V, 'x'=D/A.
basisBob = ""
# TODO: Put your code here.
for i in range(n):
    if random.randint(0, 1) == 0:  # Flip a coin (0 or 1).
        basisBob += '+'
    else:
        basisBob += 'x'

# Bob performs a measurement on each photon.
# Use the methods of the Photon class to measure each photon.
# outcomeBob should be a string of n characters.
# Use the convention 'H','V','D','A', ' '=not measured
outcomeBob = ""
# TODO: Put your code here.
for i in range(n):
    if basisBob[i] == '+':
        outcomeBob += qubitArray[i].measureHV()
    else:
        outcomeBob += qubitArray[i].measureDA()

# Bob infers the raw key.
# keyBob should be a string of n characters.
# Use the convention '0', '1', '-'=invalid measurement
keyBob = ""
# TODO: Put your code here.
for i in range(n):
    if outcomeBob[i] == 'H' or outcomeBob[i] == 'D':
        keyBob += '0'
    elif outcomeBob[i] == 'V' or outcomeBob[i] == 'A':
        keyBob += '1'
    else:
        keyBob += '-'


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
# TODO: Put your code here.
for i in range (n):
    if basisAlice[i] == basisBob[i]:
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
# TODO: Put your code here.
equalCount = 0;
revealCount = 0;
for i in range (n):
    if (random.randint(0,7) == 5) and (siftedAlice[i] != ' '):
        sampleIndex += '1'
        revealCount += 1
    else :
        sampleIndex += '0'
for i in range (n):
    if sampleIndex[i] == '1':
        if siftedAlice[i] == siftedBob[i]:
            equalCount += 1

sampledBobQBER = 100.0 * (equalCount / revealCount)

# Alice and Bob remove the portion of their sifted keys that was sampled.
# Since a portion of the sifted key was publicly revealed, it cannot be used.
# secureAlice and secureBob should be strings of length n.
# Use the convention '0', '1', ' '=removed
secureAlice = ""
secureBob = ""
# TODO: Put your code here.
for i in range(n):
    if sampleIndex[i] == '1':
        secureAlice += " "
        secureBob += " "
    else:
        secureAlice += siftedAlice[i]
        secureBob += siftedBob[i]

# Alice and Bob make a hard determination whether the channel is secure.
# If it looks like there's something fishy, better hit the kill switch!
channelSecure = True # default value, to be changed to False if Eve suspected
# TODO: Put your code here.
if sampledBobQBER > 85:
    channelSecure = False

# Eve ------------------------------------------------------------------

# Eve infers the raw key.
# keyEve should be a string of n characters.
# Use the convention '0', '1', '-'=invalid measurement, ' '=not measured
keyEve = ""
# TODO: Put your code here.

# Eve extracts her sifted key.
# Knowing what Alice and Bob have publically revealed, Eve
# now selects which portion of her sifted key to keep.
# stolenEve should be strings of length n.
# Use the '0', '1', ' '=removed
stolenEve = ""
# TODO: Put your code here.


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