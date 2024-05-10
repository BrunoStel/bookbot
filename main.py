def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    get_num_words(text)
    dict = get_letters_count(text)
    dict_list = transform_dict(dict)
    print_letters(dict_list) 

def sort_on(dict):
    return dict['occurrence']

def get_num_words(text):
    words = text.split()
    print(f"{len(words)} words found in the document")

def get_letters_count(text):
  dict = {}
  text_lower_case = text.lower()
  for letter in text_lower_case:
    if letter in dict:
      dict[letter] += 1
    else:
      dict[letter] =1
  return dict

def transform_dict(dict):
  dict_list=[]
  for val in dict:
    obj ={
      "character": val,
      "occurrence" : dict[val]
    }
    dict_list.append(obj)
  dict_list.sort(key=sort_on, reverse=True)
  return dict_list

def print_letters(dict_list):
  for dict in dict_list:
    if dict['character'].isalpha():
      print(f"Letter {dict['character']} appeared {dict['occurrence']} time(s)")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()