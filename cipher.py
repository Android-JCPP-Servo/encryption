##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################


##############################################################################
# CIPHER
##############################################################################
class Cipher:
    def __init__(self):
        # TODO: Insert anything you need for your cipher here
        self._key = 3 # Define number of rows or rails for encryption/decryption

    def get_author(self):
        # TODO: Return your name
        return "Andersen Stewart"

    def get_cipher_name(self):
        # TODO: Return the cipher name
        return "Rail Fence Cipher"

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        # TODO: This function should return your citation(s)
        return "GeeksforGeeks. (2023, March 27). RAIL FENCE CIPHER - encryption and decryption. GeeksforGeeks. Retrieved March 28, 2023, from https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/"

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
        # TODO: This function should return your psuedocode, neatly formatted

        # The encrypt pseudocode
        pc = "encrypt(plaintext, password)\n" \
             "   rail <- [['\\n' FOR i IN range(len(plaintext))] FOR j IN range(key)]\n" \
             "   dir_down <- False\n" \
             "   row <- 0\n" \
             "   col <- 0\n" \
             "   FOR i IN range(len(plaintext))\n" \
             "      IF row IS 0 OR row IS key - 1\n" \
             "         dir_down <- not dir_down\n" \
             "      rail[row][col] <- plaintext[i]\n" \
             "      col + 1\n" \
             "      IF dir_down IS True\n" \
             "         row + 1\n" \
             "      ELSE\n" \
             "         row - 1\n" \
             "   ciphertext <- []\n" \
             "   FOR i IN range(key)\n" \
             "      FOR j IN range(len(plaintext))\n" \
             "         IF rail[i][j] IS NOT '\\n'\n" \
             "            ciphertext.append(rail[i][j])\n" \
             "   RETURN \"\".join(ciphertext)"

        # The decrypt pseudocode
        pc += "decrypt(ciphertext, password)\n" \
              "   rail <- [['\\n' FOR i IN range(len(plaintext))] FOR j IN range(key)]\n" \
              "   dir_down <- None\n" \
              "   row <- 0\n" \
              "   col <- 0\n" \
              "   FOR i IN range(len(ciphertext))\n" \
              "      IF row IS 0\n" \
              "         dir_down <- False\n" \
              "      IF row IS key - 1\n" \
              "         dir_down <- True\n" \
              "      rail[i][j] <- '*'\n" \
              "      col + 1\n" \
              "      IF dir_down\n" \
              "         row + 1\n" \
              "      ELSE\n" \
              "         row - 1\n" \
              "   index <- 0\n" \
              "   FOR i IN range(key)\n" \
              "      FOR j IN range(len(cipher))\n" \
              "         IF rail[i][j] IS '*' AND index < len(cipher)\n" \
              "            rail[i][j] <- cipher[index]\n" \
              "            index + 1\n" \
              "   plaintext <- []\n" \
              "   row <- 0\n" \
              "   col <- 0\n" \
              "   FOR i IN range(len(cipher))\n" \
              "      IF row IS 0\n" \
              "         dir_down <- True\n" \
              "      IF row IS key - 1\n" \
              "         dir_down <- False\n" \
              "      IF rail[i][j] IS NOT '*'\n" \
              "         plaintext.append(rail[row][col])\n" \
              "         col + 1\n" \
              "      IF dir_down\n" \
              "         row + 1\n" \
              "      ELSE\n" \
              "         row - 1\n" \
              "   RETURN \"\".join(plaintext)"

        return pc

    ##########################################################################
    # ENCRYPT
    # TODO: ADD description
    ##########################################################################
    def encrypt(self, plaintext, password):
        ciphertext = plaintext
        # TODO - Add your code here
        return ciphertext

    ##########################################################################
    # DECRYPT
    # TODO: ADD description
    ##########################################################################
    def decrypt(self, ciphertext, password):
        plaintext = ciphertext
        # TODO - Add your code here
        return plaintext