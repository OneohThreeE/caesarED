CeasarED: encryption, decryption and public & private keygen


# Encryption:
--------------

## Variables
--------------

Variable|Desciption
--------|------------
P|plaintext
bS|baseString
pK1|Private Key a set of random numbers each an index of a unique letter of baseString in PK1
pKa|Private Key substituted 
PKa|Public Key obtained by using numbers of PK1 as indexes for basestring
PK1|Grid of random numbers used to generate Public Key 
k|shift factor
C1|cipher1
C2|cipher2
C3|cipher3
NaCl|salt

## Alogrithm
----------------

    1. Plaintext >> Cipher One -- to each letter in plaintext adds k*i


        C1[i] = (P1[i]+bS[i*k]) % bS)


    2.Cipher One >> Cipher Two -- for each letter of cipher1 in baseString sub letter in alphaPrivateKey


        C2[i] =  pKa[bS[C1[i]]]


    3.Cipher Two >> Cipher 3 -- generate salt, add k to each num in numPubKey, use numPrivateKey to select salt from (numPubKey+k)

        NaCl[i] = PKa[(pK1[i+k]) mod len (PKa) ]

        C3[i] = bS[(C2[i] + NaCl[i]) mod len(bS)]



# Decryption:
----------------

    Reverse of encryption.

# KeyGens:
----------------

    
## PUBLIC
----------------

    keyLen =  length of public key

    1. Generate OneKey

        OneKey = keyLen length array of random integers range 0 to (len(baseString) -1)
    
    2. Generate alphaKeySpace

        alphaKeySpace[i] = baseString[OneKey[i]]


    
## PRIVATE
----------------

    1. Generate numPrivKey, for each char in baseString, find all pos of char in alphaKeySpace, record i[] ,
    choose one i for each char


    2. Generate alphaPrivKey

        pKa[i] = baseString[pK1[i]]


    3. Generate shuffAlphaPrivKey and shuffNumPrivKey, arrange elem in list alphaPriv Key in random order




