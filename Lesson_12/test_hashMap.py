from hashMap import HashMap
import pytest

def test_HashMap():
	myMap = HashMap(20)
	myMap.set('1','3')
	myMap.set('a','4')
	myMap.set('u','8')
	assert myMap.get('1') == '3'
	assert myMap.get('u') == '8'
	assert myMap.exists('u') == True
	assert myMap.exists('2') == False
