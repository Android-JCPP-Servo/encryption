##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, Andersen Stewart
# Summary:
#    Rail Fence Cipher - a method which encrypts/decrypts messages synchronously
#    and ensures use of a password
##############################################################################


##############################################################################
# CIPHER
##############################################################################
class Cipher:
    def __init__(self):
        self._key = 0 # Define number of rails for encryption/decryption

    def get_author(self):
        return "Andersen Stewart"

    def get_cipher_name(self):
        return "Rail Fence Cipher"

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        tutorialsPoint = "Cryptography with Python - Quick Guide. Tutorials Point. (2023). Retrieved March 29, 2023, from https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm#:~:text=any%20practical%20use.-,Transposition%20Cipher,-Transposition%20Cipher%20is"
        geeksForGeeks = "GeeksforGeeks. (2023, March 27). RAIL FENCE CIPHER - encryption and decryption. GeeksforGeeks. Retrieved March 28, 2023, from https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/"
        return "Source 1:\n" + tutorialsPoint + '\n\n' + "Source 2:\n" + geeksForGeeks

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
        # The encrypt pseudocode
        pc = "encrypt(plaintext, password)\n" \
             "   key <- get_key_length(password)\n" \
             "   rail <- [['\\n' FOR i IN range(len(plaintext))] FOR j IN range(key)]\n" \
             "   down_dir <- False\n" \
             "   row <- 0\n" \
             "   col <- 0\n" \
             "   FOR i IN range(len(plaintext))\n" \
             "      IF row IS 0 OR row IS key - 1\n" \
             "         down_dir <- not down_dir\n" \
             "      rail[row][col] <- plaintext[i]\n" \
             "      col + 1\n" \
             "      IF down_dir IS True\n" \
             "         row + 1\n" \
             "      ELSE\n" \
             "         row - 1\n" \
             "   ciphertext <- []\n" \
             "   FOR i IN range(key)\n" \
             "      FOR j IN range(len(plaintext))\n" \
             "         IF rail[i][j] IS NOT '\\n'\n" \
             "            ciphertext.append(rail[i][j])\n" \
             "   RETURN \"\".join(ciphertext)\n\n"

        # The decrypt pseudocode
        pc += "decrypt(ciphertext, password)\n" \
              "   key <- get_key_length(password)\n" \
              "   rail <- [['\\n' FOR i IN range(len(ciphertext))] FOR j IN range(key)]\n" \
              "   down_dir <- None\n" \
              "   row <- 0\n" \
              "   col <- 0\n" \
              "   FOR i IN range(len(ciphertext))\n" \
              "      IF row IS 0\n" \
              "         down_dir <- True\n" \
              "      IF row IS key - 1\n" \
              "         down_dir <- False\n" \
              "      rail[row][col] <- '*'\n" \
              "      col + 1\n" \
              "      IF down_dir\n" \
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
              "         down_dir <- True\n" \
              "      IF row IS key - 1\n" \
              "         down_dir <- False\n" \
              "      IF rail[row][col] IS NOT '*'\n" \
              "         plaintext.append(rail[row][col])\n" \
              "         col + 1\n" \
              "      IF down_dir\n" \
              "         row + 1\n" \
              "      ELSE\n" \
              "         row - 1\n" \
              "   RETURN \"\".join(plaintext)\n\n"
        
        # Method for determining self._key size
        pc += "get_key_length(password)\n" \
              "   RETURN len(password)"

        return pc

    ##########################################################################
    # ENCRYPT
    # Using the Rail Fence encryption method, the plaintext will be encrypted
    # by following this process:
    # 1. Place first letter of string in top-left grid cell
    # 2. Place consecutive letters in next bottom-right grid cell until bottom
    #    row is reached
    # 3. If bottom is reached, move upward to the right until the grid top is
    #    reached
    # 4. Follow this pattern until end of string is reached
    # 5. Combine result layout into new (encrypted) string
    ##########################################################################
    def encrypt(self, plaintext, password):
        # Get self._key length
        self._get_key_length(password)
        # Set rail grid system
        rail = [['\n' for i in range(len(plaintext))] for j in range(self._key)]
        # Initialize variables and directions for grid layout
        down_dir = False
        row, col = 0, 0
        # Loop through length of plaintext to determine grid layout width
        for i in range(len(plaintext)):
            # Check if we're at the top or bottom of the grid layout
            if row == 0 or row == self._key - 1:
                # Start moving down or up, depending on position
                down_dir = not down_dir
            # Set the row and column to current string character position
            rail[row][col] = plaintext[i]
            # Move to the next column
            col += 1
            # If we're moving down...
            if down_dir:
                # Go downward one row
                row += 1
            # If we' moving up...'
            else:
                # Go up one row
                row -= 1
        # Begin defining the ciphertext
        ciphertext = []
        # Loop through length of self._key and plaintext to construct ciphertext
        for i in range(self._key):
            for j in range(len(plaintext)):
                # Check if the current character is not a newline character
                if rail[i][j] != '\n':
                    # Append current character if it is not a newline character
                    ciphertext.append(rail[i][j])
        # Return ciphertext
        return "".join(ciphertext)

    ##########################################################################
    # DECRYPT
    # Using the Rail Fence decryption method, the ciphertext will be decrypted
    # by following this process:
    # 1. Loop through all columns, placing markers ('*') to indicate where
    #    ciphertext characters will be placed along rail system
    # 2. Replace markers with ciphertext characters, looping through entire
    #    string
    # 3. Append the characters together to form plaintext
    # 4. Return the plaintext
    ##########################################################################
    def decrypt(self, ciphertext, password):
        # Get self._key from password length
        self._get_key_length(password)
        # Establish grid rail system
        rail = [['\n' for i in range(len(ciphertext))] for j in range(self._key)]
        # Initialize variables and directions for grid layout
        down_dir = None
        row, col = 0, 0
        # Loop through length of ciphertext to determine grid layout
        for i in range(len(ciphertext)):
            # If we're on the bottom row...
            if row == 0:
                # ...set down_dir to True
                down_dir = True
            # IF we're on the top row...
            if row == self._key - 1:
                # ...set down_dir to False
                down_dir = False
            # Set current grid cell to *
            rail[row][col] = '*'
            # Move to the next column
            col += 1
            # If we're moving down...
            if down_dir:
                # ...move down one row
                row += 1
            # If we're moving up...
            else:
                # ...move up one row
                row -= 1
        # Start checking to see which grid cells are marked with text
        index = 0
        # Loop through size of self._key to determine grid size
        for i in range(self._key):
            for j in range(len(ciphertext)):
                # Check if cell has * marker
                if rail[i][j] == '*' and index < len(ciphertext):
                    # Replace the marker with the corresponding ciphertext char
                    rail[i][j] = ciphertext[index]
                    # Move to the next index
                    index += 1
        # Begin decrypting to plaintext
        plaintext = []
        # Initialize row and column indices
        row, col = 0, 0
        # Loop through length of ciphertext
        for i in range(len(ciphertext)):
            # If we're on the bottom row...
            if row == 0:
                # ...set down direction to True
                down_dir = True
            # If we're on the top row...
            if row == self._key - 1:
                # ...set down direction to False
                down_dir = False
            # If the current char is not the marker...
            if rail[row][col] != '*':
                # ...append the character
                plaintext.append(rail[row][col])
                # Move to the next column
                col += 1
            # If we're moving down...
            if down_dir:
                # ...move down one row
                row += 1
            # If we' moving up...
            else:
                # ...move up one row
                row -= 1
        # Return plaintext
        return "".join(plaintext)
    
    ##########################################################################
    # GETKEYLENGTH
    # Assign the password length as the key (encryption/decryption) value
    ##########################################################################
    def _get_key_length(self, password):
        self._key = len(password)