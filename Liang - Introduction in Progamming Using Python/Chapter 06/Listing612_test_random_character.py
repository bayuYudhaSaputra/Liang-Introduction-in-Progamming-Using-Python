import Listing611_random_character

NUMBER_OF_CHARS = 175 # Number of characters to generate
CHARS_PER_LINE = 25 # Number of characters to display per line

# Print random characters between 'a' and 'z', 25 chars per line
for i in range(NUMBER_OF_CHARS):
    print( Listing611_random_character.getRandomLowerCaseLetter() , end = " " )
    if (i + 1) % CHARS_PER_LINE == 0:
        print() # Jump to the new line