from testhelper import test

# Write a function that takes a sentence and returns a string with all the 'non vowels' 
# blanked out with an underscore, to be used in a guessing game.abs
# Example input / output:
# "The quick brown fox jumped over the lazy dog"
# "__e _ui__ __o__ _o_ _u__e_ o_e_ __e _a__ _o_"

def sentence_word_blanker(sentence):
    return "_" # Replace with your solution

### TESTS - Run the code that calls the function to check it works.
test("Sudoku box checker 1","aeiou", 
    sentence_word_blanker("aeiou"))

test("Sudoku box checker 2","______", 
    sentence_word_blanker("blrzzz"))

test("Sudoku box checker 3","__e _ui__ __o__ _o_ _u__e_ o_e_ __e _a__ _o_", 
    sentence_word_blanker("The quick brown fox jumped over the lazy dog"))


