# Ceasared: toy encryption 

**Toy** encyption alogrithm: described below. Uses a short public key and a (very) long private key. Sample keys included in source.
Please do **not** use to secure anything of value.

## Variables

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
s|salt

## Alogrithm

1. Plaintext >> Cipher One -- to each letter in plaintext adds k * i

        C1[i] = (P1[i]+bS[i*k]) % bS)


1. Cipher One >> Cipher Two -- for each letter of cipher1 in baseString sub letter in alphaPrivateKey


        C2[i] =  pKa[bS[C1[i]]]

1. Cipher Two >> Cipher 3 -- generate salt, add k to each num in numPubKey, use numPrivateKey to select salt from (numPubKey+k)

        NaCl[i] = PKa[(pK1[i+k]) mod len (PKa) ]

        C3[i] = bS[(C2[i] + s[i]) mod len(bS)]

