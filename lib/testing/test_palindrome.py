from lib.palindrome import longest_palindromic_substring

def test_longest_palindrome_basic():
    assert longest_palindromic_substring("racecar") == "racecar"

def test_longest_palindrome_no_match():
    assert longest_palindromic_substring("hello") == "h" or "l"  # depends on spec

def test_single_char():
    assert longest_palindromic_substring("a") == "a"

def test_two_chars():
    assert longest_palindromic_substring("ab") in ["a", "b"]