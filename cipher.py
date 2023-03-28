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
        pc = "encrypt(plaintext, password)" \
             "   SET rail AS map object using length of plaintext and key\n" \
             "   SET down_direction to False to start at top-left grid\n" \
             "   SET row and col to 0 for top-left position\n" \
             "   LOOP through length of plaintext\n" \
             "   IF the row IS the top OR the bottom\n" \
             "      SET down_direction to NOT down_direction\n" \
             "      PUT next letter into the current grid square\n" \
             "      ADD 1 to the current column value\n" \
             "      IF down_direction IS True\n" \
             "         ADD 1 to the current row value\n" \
             "      IF down_direction IS False\n" \
             "         SUBTRACT 1 from the current row value\n" \
             "   SET result to empty array\n" \
             "   LOOP through length of key\n" \
             "      LOOP through length of plaintext\n" \
             "         IF current grid square IS NOT '\\n'" \
             "            PUT grid square into result array\n" \
             "   RETURN result"

        # The decrypt pseudocode
        pc += "insert the decryption pseudocode\n"

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