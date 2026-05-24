# Module pwalgorithms
import time
import pwalgorithms as pwa

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

# analyze a two-word password
def two_words(target_password):
    dictionary = get_dictionary()
    attempts = 0
    start_time = time.time()

    for word1 in dictionary:
      for word2 in dictionary:
        # Concatenate two words
        guess = word1 + word2
        attempts += 1

        if guess == target_password:
          end_time = time.time()
          total_time = end_time - start_time
          return True, attempts, total_time
        
    end_time = time.time()
    total_time = end_time - start_time
    return True, attempts, total_time

# analyze a two-word and digit password
def two_words_and_digit(target_password):
    dictionary = get_dictionary()
    digits = "0123456789"
    attempts = 0
    start_time = time.time()

    for word1 in dictionary:
      for word2 in dictionary:
        base_phrase = word1 + word2
        for d in digits:
          # Check digit at the beginning
          guess_front = d + base_phrase
          attempts += 1
          if guess_front == target_password:
              end_time = time.time()
              total_time = end_time - start_time
              return True, attempts, total_time
          
          # Check digit at the end
          guess_back = base_phrase + d
          attempts += 1
          if guess_back == target_password:
              end_time = time.time()
              total_time = end_time - start_time
              return True, attempts, total_time
        
    end_time = time.time()
    total_time = end_time - start_time
    return False, attempts, total_time

# choose a passphrase to analyze
secret_passphrase = "kookykoala"

print("Analyzing passphrase: {}".format(secret_passphrase))
print("This may take a minute or two. Please wait...")

# Call the two_words function
found, num_guesses, time_elapsed = pwa.two_words(secret_passphrase)

if found:
  print("-" * 30)
  print("Success! Passphrase identified.")
  print("Attempts: {}".format(num_guesses))
  print("Time Taken: {:.2f} seconds".format(time_elapsed))
  print("-" * 30)
else:
  print("Passphrase not found in dictionary combinations.")


    
