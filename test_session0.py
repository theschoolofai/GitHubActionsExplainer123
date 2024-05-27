# DO NOT CHANGE THIS TEST FILE
import pytest
import session0

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 50, "Make your README.md file interesting! Add at least 500 words"

def test_function_failure():
  assert session0.myfunc(4, 4) == 8, 'Your function doesnt work at all!'
  
