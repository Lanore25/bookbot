import sys 
def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

from stats import get_num_words, get_char_counts, sort_char_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = get_char_counts(book_text)
    sorted_char_counts = sort_char_counts(char_counts)
    for item in sorted_char_counts:
        char = item["char"]
        # Only print single alphabetic characters
        if char.isalpha():
            print(f"{char}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()