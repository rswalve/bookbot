from stats import get_num_words, get_chars_dict

def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	letter_count = get_chars_dict(text)
	print("============ BOOKBOT ============")
	print("Analyzing book found at {book_path}")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
      
	list_of_dicts = []
	for key, value in letter_count.items():
		new_dict = {"char": key, "num": value}
		list_of_dicts.append(new_dict)
            
	list_of_dicts.sort(reverse=True, key=sort_on)
	
	for item in list_of_dicts:
		#print(f"The '{item['char']}' character was found {item['num']} times")
		print(f"{item['char']}: {item['num']}")
            
	print("--- End report ---")

def get_book_text(path):
	with open(path) as f:
		return f.read()

def sort_on(dict):
      return dict["num"]

if __name__ == "__main__":
    main()
