from stats import get_num_words, get_chars_dict
import sys

if len(sys.argv) != 2:
    # 1. Print the usage message
    print("Usage: python3 main.py <path_to_book>")
    
    # 2. Exit the program with status code 1 (indicating an error)
    sys.exit(1)


def main():
	book_path = sys.argv[1]
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	letter_count = get_chars_dict(text)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}")
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
