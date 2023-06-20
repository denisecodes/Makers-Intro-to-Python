# Video alternative: https://youtu.be/qDWyR0XpJtQ&t=1295s

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def check_if_word_has_hyphen(words):
  no_hyphen_words = []
  for word in words:
    if "-" not in word:
      no_hyphen_words.append(word)
  return no_hyphen_words

def more_than_10_char(words):
  ten_char_words = []
  for word in words:
    if len(word) > 10:
      ten_char_words.append(word)
  return ten_char_words

def check_if_more_than_15_char(words):
  long_word_list = []
  for word in words:
    if len(word) > 15:
      word = word[:15] + "..."
      long_word_list.append(word)
    else:
      long_word_list.append(word)
  return "These words are quite long: " + ", ".join(long_word_list)

def report_long_words(words):
  no_hypen_words = check_if_word_has_hyphen(words)
  ten_char_words = more_than_10_char(no_hypen_words)
  long_words = check_if_more_than_15_char(ten_char_words)
  return long_words

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
