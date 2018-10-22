#
#
#

#
#
#
#

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)
