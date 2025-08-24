def get_book_text(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content

def count_words(content):
    words = content.split()
    return len(words)

def count_characters(content):
    characters = {}
    lower_content = content.lower()
    for char in lower_content:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    

    return characters

def print_report(char_dict, word_count):
    #print(char_dict["t"])
    characters_list = []
    for char in char_dict:
        char_dictionary = {"char": char, "num": char_dict[char]}
        characters_list.append(char_dictionary)
    def sort_on(items):
        return items["num"]

    characters_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in characters_list:
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")