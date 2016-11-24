#########################
#                       #                              
# caesarED By: 1 0 3 E  #                      
#              0 3 E 1  #                      
#              3 E 1 0  #                     
#              E 1 0 3  #                     
#                       #          
#########################
#########################

import random

######    
#@@@@@# StringDoc+InitCond
######

""" CeasarED: encryption, decryption and public & private keygen

----------------
Encryption:
----------------

P1 = plaintext,
bS = baseString
pKa = shuffAlphaPrivateKey
pK1=shuffNumPrivateKey
PKa = alphaPublic key
PK1 = numPubKey
k = shift factor
C1 = cipher1
C2 = cipher2
C3 = cipher3
NaCl= salt


1. P1 >>C1 -- to each letter in plaintext adds k*i


    C1[i] = (P1[i]+bS[i*k]) % bS) 


2.C1 >> C2 -- for each letter of cipher1 in baseString sub letter in alphaPrivateKey


    C2[i] =  pKa[bS[C1[i]]]  


3.C2 >> C3 -- generate salt, add k to each num in numPubKey, use numPrivateKey to select salt from (numPubKey+k)

    NaCl[i] = PKa[(pK1[i+k]) mod len (PKa) ]

    C3[i] = bS[(C2[i] + NaCl[i]) mod len(bS)]



----------------
Decryption:
----------------

    Reverse of encryption.

----------------
KeyGens:
----------------


PUBLIC
----------------

keyLen =  length of public key

1. Generate OneKey

    OneKey = keyLen length array of random integers range 0 to (len(baseString) -1)

2. Generate alphaKeySpace

    alphaKeySpace[i] = baseString[OneKey[i]]



PRIVATE
----------------

1. Generate numPrivKey, for each char in baseString, find all pos of char in alphaKeySpace, record i[] , choose one i for each char


2. Generate alphaPrivKey

    pKa[i] = baseString[pK1[i]]


3. Generate shuffAlphaPrivKey and shuffNumPrivKey, arrange elem in list alphaPriv Key in random order




"""

main = '' #begin main loop


######    
#@@@@@# variStore
######

"""
    Global key Variables

"""


baseString = list('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.!?;:%#+@')
alphaKeySpace=''
oneKey=[]
shuffOnePrivKey = [] # numVer Privkey
shuffAlphaPrivKey = '' #charVer PrivKey
listShuffAlphaPrivKey = list(shuffAlphaPrivKey)
kShuffOnePrivKey = [] # salt = alphaKeySpace[shuffOnePrivKey[i+k]]
k=int() #shiftVari



######
#@@@@@# functions
######



###
#@#ENCRYPTION
###

def encrypt():

    """
    Ask to input plaintext then encrypts, also gen specific key varis from priv key pub key.

    -- gen specific key varis

    -- plaintext >> cipher1

    -- cipher1 >> cipher 2

    -- cipher2 >> cipher3

    """


    plaintext = input('Enter message:\n>>')

    kShuffAlphaPrivKey=''
    listKShuffAlphaPrivKey=[]

    cipher1=''
    cipher2=''
    cipher3=''

    """
    GenKeyVaris from shuffOnePrivKey

    """

    kShuffOnePrivKey = [((x + k)%len(baseString)) for x in shuffOnePrivKey] # gen kshuffoneprivkey
    for i in kShuffOnePrivKey: #gen kShuffAlphaPrivKey using kShuffOnePrivKey to lookup alphaKeySpace
        kShuffAlphaPrivKey += (alphaKeySpace[i])
    listKShuffAlphaPrivKey = list(kShuffAlphaPrivKey)

    """
    plaintext >> cipher1


    -- To each letter in plaintext adds shiftfactor * i

    """

    i = 0
    for c in plaintext: # add k*i to each elem plaintext form cipher1 
        if c in baseString:
            i += 1
            cipher1 += baseString[(baseString.index((c))+(k*i))%(len(baseString))]
    listCipher1 = list(cipher1)


    """
    cipher1 >> cipher2

    -- To each letter in listcipher1, subs with letter in same position in private key

    """

    listCipher2=''
    for i in listCipher1:
            c = baseString.index(i)
            cipher2 += shuffAlphaPrivKey[(baseString.index(i)%(len(baseString)))]

    listCipher2 = list(cipher2)


    """
    cipher2 >> cipher3

    -- To each letter in listCipher2 adds letter value in k-shifted private key

    """

    c=0
    for i in listCipher2:
        if c > (len(baseString)-1): # (c)mod(baseString)
            c = 0
        cipher3 += baseString[(baseString.index(i) + baseString.index(listKShuffAlphaPrivKey[c]))%(len(baseString))] 
        c +=1


    """
    OUT

    """

    print('Encrypted message is:\n' + cipher3)



###
#@#DECRYPTION
###


def decrypt():

    """
    Ask to input ciphertext then decrypts, also gen specific key varis from priv key pub key.

    -- gen specific key varis

    -- cipher3 >> cipher2

    -- cipher2 >> cipher1

    -- cipher1 >> plaintextOne

    """

    cipherThree = input('Enter ciphertext to decrypt:\n>>')
    listCipherThree= list(cipherThree)

    kShuffAlphaPrivKey=''
    listKShuffAlphaPrivKey=[]    

    cipherOne=''
    cipherTwo=''
    plaintextOne=''


    """
    GenKeyVaris from shuffOnePrivKey

    """

    kShuffOnePrivKey = [((x + k)%len(baseString)) for x in shuffOnePrivKey] # gen kshuffoneprivkey
    for i in kShuffOnePrivKey: #gen kShuffAlphaPrivKey using kShuffOnePrivKey to lookup alphaKeySpace
        kShuffAlphaPrivKey += (alphaKeySpace[i])
    listKShuffAlphaPrivKey = list(kShuffAlphaPrivKey)
    listShuffAlphaPrivKey = list(shuffAlphaPrivKey)

    """
    CipherThree >> cipherTwo

    """
    c = 0

    for i in cipherThree:
        if c > (len(baseString)-1): # (c)mod(baseString)
            c = 0
        cipherTwo += baseString[(baseString.index(i) - baseString.index(listKShuffAlphaPrivKey[c]))%(len(baseString))]
        c += 1

    listCipherTwo= list(cipherTwo)


    """
    cipherTwo >> cipherOne

    """
    for i in listCipherTwo:
        cipherOne += baseString[listShuffAlphaPrivKey.index(i)]

    listCipherOne= list(cipherOne)

    """
    cipherOne >> plaintextOne

    """
    i = 0

    for p in listCipherOne:
        i += 1
        plaintextOne += baseString[(baseString.index(p)-(k*i))%(len(baseString))]

    """
    OUT

    """

    print('Decrypted message is:\n' + plaintextOne)


###
#@#pubKeyGen
###



def pubKeyGen():

    """
    pubKeyGen: generates n-length public key

    """
    global alphaKeySpace
    alphaKeySpace=''

    check = 0
    while check == 0:
        keySize = int(input('Enter keySpace length ( keySpace > 1000 )\n>>'))
        oneKey=[]



        """
        Generate random string, element range 0-72, length = keyLength

        """

        c=0
        while keySize > c:
            r1 = str(random.randint(0,72)) 
            oneKey += r1 + ' ' 
            c += 1


        """
        Read oneKey between spaces and add entries converted 
        using dictionary to alphaKeySpace

        """

        temp1 = ''
        for i in oneKey:     
            if i == ' ':
                alphaKeySpace += (baseString[int(temp1)]) # convert ints to letters, store in alphaKey
                temp1= ''
            if i != ' ':
                temp1 += i # -w i to temp1 ie -r number

            """
            Check keyspace contains all char

            """

        for i in baseString:
            if i not in alphaKeySpace:
                print('INVALID keySpace')
                check = 0
                break
            else:
                check = 1


                """
                OUT

                """


        print('Your alphaKeySpace is:\n' + alphaKeySpace)



###
#@#privKeyGen
###


def privKeyGen( ):

    """
    privKeyGen: generates 73 char private key

    """
    baseString = list('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.!?;:%#+@')
    pos = [] #position
    sel = [] #selection

    global shuffAlphaPrivKey
    shuffAlphaPrivKey=''

    global shuffOnePrivKey
    shuffOnePrivKey=[]



    """
    Fill pos with positions of each char in alphaKeySpace

    """
    for i in baseString: 
        pos = [pos for pos, char in enumerate(alphaKeySpace) if char == i] #positions of character i in alphaKeySpace
        sel.append(random.choice(pos)) #for each char add random pos to sel
    shuffOnePrivKey = random.sample(sel,73) # list of pos chosen shuffled

    """
    Trans chosen numbers to char

    """

    for i in shuffOnePrivKey:
        shuffAlphaPrivKey += (alphaKeySpace[i])
    print('Your private key is:\n' + shuffAlphaPrivKey) # private key



###### ##   
#@@@@@@@# mainLoop
########


while main == '':   

    print('\n','-'*39,'\n','  caesarED: encryption and decryption','\n','-'*39,'\n') 
    main = input('"e" to encrypt, "d" to decrypt, "c" for command list or "x" to exit\n>>')

######    
#@@@@@# ENCRYPTION
######


    while main == 'e': #encrypt

        """
        Check pub & priv keySpace not empty

        """

        if alphaKeySpace == '':
            print('Generating public key...')
            main ='g'
            break

        if shuffAlphaPrivKey == '':
            print('Generating private key...')
            main ='s'
            break

        if k == 0:
            k = int(input('Enter Shift Factor:\n>>'))



        """
        Encrypt

        """

        encrypt()

        main='' #reset loop



######    
#@@@@@# DECRYPTION
######

    if main == 'd': #decrypt

        """
        Decrypt

        """
        decrypt()

        main = ''

######   
#@@@@@# setShiftFactor
######

    if main == 'k':

        """
        Set shift factor 'k'

        """

        k = int(input('Enter shift factor:\n>>'))


######    
#@@@@@# keySpaceGen
######        

    if main == 'g':

        """
        Generate n-length public Key, chars from baseString

        """

        pubKeyGen()      

        main = ''



######
#@@@@@# shuffAlphaKeySel from alphaKeySpace
######

    if main == 's':


        """
        privKeyGen: generates 73 char private key, for i in baseString

        """

        privKeyGen()


        main=''

######    
#@@@@@# ExitCond+command list
######

    if main == 'x': #exit
        exit()

    if main == 'c':
        print('"e" to encrypt, "d" to decrypt", "g" to generate a new public keySpace,\n"s" to select a private key, "k" to set shiftFactor, "x" to exit')
        main = ''

    if main == 'test':
        print(alphaKeySpace)
        main= ''

        """
        Reset loop on nonValid entry

        """

    else: 
        main=''
