# Welcome message 
print '***Welcome to the Pig Latin translator***'

# Instructions
instructions = ('\nInstructions: \n'
'Pig Latin translator traslates the original word typed into Pig Latin by removing the first letter of the word and adding \'ay\' at the end.' )

# Print instructions
print instructions

# Suffix for the translation
pyg = 'ay'

# Storing original user input
original = raw_input('\nEnter a word to translate: ')

# Validating input
if len(original) > 0 and original.isalpha():
  word = original.lower() # Converting input into lowercase
  first = word[0] # Getting first letter of input
  # Creating a translation
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print '\nTranslation: %s'%new_word # Print translation

# Checking for invalid input
else: 
    print 'Invalid input'
    