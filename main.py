def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  chars_dict = count_characters(text)
  alpha_dict = get_alpha_dict(chars_dict)
  letters_list_report = cvrt_to_list_and_sort(alpha_dict)
  
  print(f"--- Begin report of {book_path} ---")
  print(f"{num_words} words found in the document \n")
  for letter in letters_list_report:
    print(f"The \'{letter['letter']}\' character was found {letter['num']} times")
  print("--- End report ---")
  
def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_words(text = ''):
  words = text.split()
  return len(words)
  
def count_characters(text = ''):
  # lower case the text
  lowered_text = text.lower()
  chars_dict = {} 
     
  for c in lowered_text:
    if c in chars_dict:
      chars_dict[c] += 1
    else:
      chars_dict[c] = 1
      
  return chars_dict

def sort_on(dict):
  return dict["num"]

def get_alpha_dict(dict):
  alpha_dict = {}
  
  for k in dict:
    if k.isalpha():
      alpha_dict[k] = dict[k]
   
  return alpha_dict
    
def cvrt_to_list_and_sort(dict):
  letters = []
  
  for key in dict:
    letter = {"letter": key, "num": dict[key]}
    letters.append(letter)
  
  letters.sort(reverse=True, key=sort_on)
  
  return letters

main()