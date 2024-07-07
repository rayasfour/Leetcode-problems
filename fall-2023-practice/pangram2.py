class Solution:
  def checkIfPangram(self, sentence):
    unique_alphabets = set()

    for letter in sentence.lower():
      if letter.isalpha():
        unique_alphabets.add(letter)
    
    if len(unique_alphabets) == 26:
      return True
    return False
