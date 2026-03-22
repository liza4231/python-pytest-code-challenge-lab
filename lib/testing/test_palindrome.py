import pytest
from lib.palindrome import longest_palindromic_substring



def test_babad():
    assert longest_palindromic_substring("babad") == "bab"


def test_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"


def test_racecar():
    assert longest_palindromic_substring("racecar") == "racecar"


def test_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_two_characters_no_palindrome():
    assert longest_palindromic_substring("ac") == "a"


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"


def test_no_long_palindrome():
    result = longest_palindromic_substring("abcdef")
    assert len(result) == 1


def test_long_string():
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"


def test_numbers_and_letters():
    assert longest_palindromic_substring("12321abc") == "12321"


def test_case_sensitivity():
    assert longest_palindromic_substring("Aa") == "A"


def test_palindrome_in_middle():
    assert longest_palindromic_substring("abaxyzzyxf") == "xyzzyx"
