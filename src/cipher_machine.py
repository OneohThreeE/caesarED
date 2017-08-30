import random
import string

from status_messages import success, failure
import import_export


class CipherMachine:
    """
    class containing encryption algorithm, key generation and import functions.
    """

    def __init__(self):
        self.base_string = string.ascii_letters + string.punctuation + string.digits + " "
        self.len_base_string = len(self.base_string)

        self.alpha_key_space = ''  # public key

        self.shuffled_num_private_key = []  # private key
        self.shuffled_alpha_private_key = []

        self.salt = [] 

        self.k = 0  # shift factor

        self.key_directory = import_export.get_path("")

    def import_public_key(self, a_file_name):
        key_space = import_export.import_public_key(a_file_name)

        if key_space:
            self.alpha_key_space = key_space
            return success("Public key imported")
        else:
            return failure("Public key import unsuccessful")

    def import_private_key(self, a_file_name):
        private_key = import_export.import_private_key(a_file_name)

        if private_key:
            self.set_key_shift(private_key[1])
            self.shuffled_num_private_key = private_key[0]
            self.shuffled_alpha_private_key = ''.join([self.alpha_key_space[x] for x in self.shuffled_num_private_key])
            self.gen_salt()
            return success("Private key imported")
        else:
            return failure("Private key import unsuccessful")

    def export_public_key(self, a_file_name):
        import_export.export_public_key(self.alpha_key_space, a_file_name)
        return success("Public key exported to: {}{}".format(self.key_directory, a_file_name))

    def export_private_key(self, a_file_name):
        import_export.export_private_key(self.shuffled_num_private_key, self.k, a_file_name)
        return success("Private key exported to: {}{}".format(self.key_directory, a_file_name))

    def set_key_shift(self, key_shift):
        self.k = key_shift
        return success("Key shift = {}".format(str(key_shift)))

    def gen_pub_key(self, len_key):
        """
        Generates a public key of length len_key; len(set(alpha_key)) is len_base_string 
        Calls gen_private_key()
        :param len_key: integer -- length of public key
        :return: None
        """
        len_key = int(len_key)
        if len_key < 3 * self.len_base_string:
            return failure("Insufficient key length")

        while True:
            num_key = [random.randint(0, self.len_base_string-1) for _ in range(len_key)]

            alpha_key = [self.base_string[x] for x in num_key]

            if len(set(alpha_key)) is not self.len_base_string:
                continue

            self.alpha_key_space = ''.join(alpha_key)
            break

        self.gen_private_key()
        return success("Public key generated")

    def gen_private_key(self):
        """
        gen_private_key: generates private key of len is len_base_string
        Calls gen_salt()
        :return: None
        """
        sel = []  # selection

        for i in self.base_string:  # get all positions of each character in alpha_key_space
            pos = [pos for pos, char in enumerate(self.alpha_key_space) if char is i]
            sel.append(random.choice(pos))  # select one position value for each character

        self.shuffled_num_private_key = random.sample(sel, self.len_base_string)  # list of pos chosen shuffled

        self.shuffled_alpha_private_key = ''.join([self.alpha_key_space[x] for x in self.shuffled_num_private_key])
        # Translate chosen numbers to characters

        self.gen_salt()
        return success("Private key generated")

    def gen_salt(self):
        """
        Generate key dependencies from public and private key variables.  
        :return: None
        """
        self.salt = [self.alpha_key_space[((x + self.k) % len(self.base_string))]
                     for x in self.shuffled_num_private_key]
        return success("Salt generated")

    def encrypt(self, plaintext):
        """
        Encrypts plaintext using algorithm below.

        -- plaintext >> cipher1
        To each letter in plaintext adds shift_factor (k) * index of letter in plaintext
        
        -- cipher1 >> cipher 2
        To each letter in cipher1, subs with letter in same position in private key
        
        -- cipher2 >> cipher3
        To each letter in cipher2 adds letter value in k-shifted private key
        
        :param plaintext: String -- plaintext
        :return: String -- encrypted plaintext
        """

        plaintext = plaintext.replace('\n', ' ')

        # add k*i to each elem plaintext form cipher1
        cipher = [(self.base_string.index(x) + (self.k * c)) % self.len_base_string
                  for c, x in enumerate(plaintext)]

        cipher = [self.shuffled_alpha_private_key[x] for x in cipher]

        cipher = [self.base_string[(self.base_string.index(x) +
                  self.base_string.index(self.salt[c % self.len_base_string])) %
                                   self.len_base_string]
                  for c, x in enumerate(cipher)]

        return success("Cipher text:\n" + ''.join(cipher))

    def decrypt(self, cipher_text):
        """
        Decrypts cipher_text using algorithm described below.
    
        -- cipher_text >> cipher2
    
        -- cipher2 >> cipher1
    
        -- cipher1 >> plain_text
        
        :param cipher_text: String -- encrypted text string
        :return: String -- unencrypted plaintext
    
        """

        cipher2 = [self.base_string[((self.base_string.index(x) -
                   self.base_string.index(self.salt[c % self.len_base_string])) %
                                     self.len_base_string)]
                   for c, x in enumerate(cipher_text)]

        cipher1 = [self.base_string[self.shuffled_alpha_private_key.index(x)] for x in cipher2]

        plain_text = [self.base_string[(self.base_string.index(x) - (self.k * c)) % self.len_base_string]
                      for c, x in enumerate(cipher1)]

        return success("Plain text:\n" + ''.join(plain_text))

    def help(self, query):
        pass
