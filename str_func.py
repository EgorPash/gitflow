def capitalize_words(string):
"""
  Делает заглавными первые буквы каждого слова в строке.

  Args:
    string (str): Строка, в которой нужно сделать заглавными первые буквы слов.

  Returns:
    str: Строка с заглавными первыми буквами слов.
  """
  
  words = string.split()

  capitalized_words = [word.capitalize() for word in words]

  return " ".join(capitalized_words)
