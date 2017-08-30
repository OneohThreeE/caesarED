import cipher_machine
from status_messages import failure


def main():
    cipher = cipher_machine.CipherMachine()

    cipher.import_public_key('public_key1')  # default parameters
    cipher.import_private_key('private_key1')

    cm_com = {"e": cipher.encrypt,
              "d": cipher.decrypt,

              "k": cipher.set_key_shift,
              "gP": cipher.gen_pub_key,
              "gp": cipher.gen_private_key,

              "eP": cipher.export_public_key,
              "ep": cipher.export_private_key,

              "iP": cipher.import_public_key,
              "ip": cipher.import_private_key,

              "h": cipher.help,
              }

    cm_com_args = {"e": [1, "Enter plain text\n>"],
                   "d": [1, "Enter cipher text\n>"],

                   "k": [1, "Enter shift factor\n>"],
                   "gP": [1, "Enter key length\n>"],
                   "gp": [0],

                   "eP": [1, "Enter file name to export public key\n>"],
                   "ep": [1, "Enter file name to export private key\n>"],

                   "iP": [1, "Enter file name to import public key\n>"],
                   "ip": [1, "Enter file name to import private key\n>"],

                   "h": [0]
                   }

    while True:
        command = input("Enter instruction:\n>")

        if command in cm_com:
            args = []

            if cm_com_args[command][0]:
                args = [input(cm_com_args[command][x+1])
                        for x in range(cm_com_args[command][0])]

            print(cm_com[command](*args))

        else:
            print(failure("Invalid command. 'h' --> help"))


if __name__ == "__main__":
    main()
