from non_repeating_char import find_first_unique_ind
import pytest

def test_one_char():
	string = "l"
	first_unique_ind = find_first_unique_ind(string)
	assert first_unique_ind == 0

def test_all_repeating():
	string = "aabb"
	first_unique_ind = find_first_unique_ind(string)
	assert first_unique_ind == -1

def test_all_unique():
	string = "abcd"
	first_unique_ind = find_first_unique_ind(string)
	assert first_unique_ind == 0

def test_last_unique():
	string = "aabbbccdde"
	first_unique_ind = find_first_unique_ind(string)
	assert first_unique_ind == 9

def test_first_unique():
	string = "vaabbb"
	first_unique_ind = find_first_unique_ind(string)
	assert first_unique_ind == 0