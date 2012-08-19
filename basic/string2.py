#!/usr/bin/python2
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  if len(s) < 3:
    result = s
  elif s[-3:] == 'ing':
    result = s + 'ly'
  else:
    result = s + 'ing'

  return result


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  whereIsNot = s.find('not')
  whereIsBad = s.find('bad')

  if whereIsNot == -1:
    return s
  elif whereIsBad > whereIsNot:
    # There is a 'not'...'bad' substring in s
    beginning = s[:whereIsNot]
    end = s[whereIsBad + 3:]
    result = beginning + 'good' + end
  else:
    result = s
    
  return result


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  halvesOfA = break_string(a)
  halvesOfB = break_string(b)

  result = halvesOfA[0] + halvesOfB[0] + \
           halvesOfA[1] + halvesOfB[1]

  return result

# Eu que fiz essa.
# Quebra a string s na metade, de acordo com as instrucoes de *F*
def break_string(s):
  length = len(s)
  half = length // 2

  # se o comprimento for impar, para que o caractere extra
  # caia na primeira metade, precisa acrescentar 1 ao valor
  # de half
  if length % 2 <> 0:
    half += 1

  beginning = s[:half]
  end = s[half:]

  result = [beginning, end]

  return result
  

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")
  test(not_bad("It's very bad"), "It's very bad")
  
  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
