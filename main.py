def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

from stats import get_num_words, get_char_counts

def main():
    book_text = get_book_text("/home/user/bookbot/books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")
    char_counts = get_char_counts(book_text)
    print(char_counts)

if __name__ == "__main__":
    main()