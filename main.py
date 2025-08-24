from stats import get_book_text, count_words, count_characters, print_report
import sys



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    content = get_book_text(file_path)
    words_count =count_words(content)
    characters_dict = count_characters(content)
    print_report(characters_dict,words_count)

if __name__ == "__main__":
    main()


