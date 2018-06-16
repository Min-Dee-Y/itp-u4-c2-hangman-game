from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []

""" Mask word"""

def _mask_word(word):
  if word =='':
    raise InvalidWordException
    
  else: 
    mask_word = '*' * len(word) 
    return mask_word

""" Uncover word """

def _uncover_word(answer_word, masked_word, character):
  answer_word = answer_word.lower()
  character = character.lower()
  list_ans = list(answer_word)
  list_mask = list(masked_word)  
  
  if ((answer_word or masked_word) == '') or (len(masked_word)!= len(answer_word)):
    raise InvalidWordException
  
  elif len(character) > 1:
    raise InvalidGuessedLetterException
    
  elif character in answer_word:
      i = 0
      for i in range(len(list_ans)):
        if list_ans[i] == character:
          list_mask[i] = character
      unmask = ''.join(list_mask)
        
  elif not character in answer_word:
    print('no')
    unmask = masked_word
  return unmask

    #char_index = answer_word.index(character)
    #list_mask = list(masked_word)
    #list_mask[char_index] = character
   # unmask = ''.join(list_mask)   
  
"""Get random word """
def _get_random_word(list_of_words):
  if not list_of_words:
    raise InvalidListOfWordsException
  
  else: word_to_guess = random.choice(list_of_words)
  return word_to_guess
 
"""Guess Letter """
def guess_letter(game, letter):
  game['answer_word'] = game['answer_word'].lower()
  letter = letter.lower()
  
  if game['masked_word'] == game['answer_word'] or game['remaining_misses'] == 0:
    raise GameFinishedException
    
  elif letter in game['answer_word']:
    game['masked_word'] = _uncover_word(game['answer_word'],game['masked_word'],letter)
    game['remaining_misses'] = game['remaining_misses']
    game['previous_guesses'] = game['previous_guesses'] + list(letter)
    
    if game['masked_word'] == game['answer_word']:
      raise GameWonException

    
  elif not letter in game['answer_word']:
    game['remaining_misses'] = game['remaining_misses'] - 1
    if game['remaining_misses'] == 0:
      raise GameLostException   
    game['masked_word'] = game['masked_word']
    game['previous_guesses'] = game['previous_guesses'] + list(letter)
    
    
  return game['masked_word'], game['remaining_misses'], game['previous_guesses']


"""Start New Game"""
def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
