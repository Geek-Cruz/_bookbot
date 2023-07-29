with open("frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.lower().split()
    list_words = {}
    for word in words:
        for char in word:
            if not char.isalpha():
                pass
            elif char not in list_words:
                list_words[char.lower()] = 1
            else:
                list_words[char.lower()] += 1
    lst = [[v,k] for k, v in list_words.items()]
    lst.sort(reverse = True)

    print("\n--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document\n\n")
    for sublst in lst:
        print(f"The '{sublst[1]}' character was found {sublst[0]} times")
      
