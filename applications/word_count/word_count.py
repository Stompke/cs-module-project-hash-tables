def word_count(s):
    # Your code here
    cache = {}

    new_string = s.split()
    print(new_string)
    for word in new_string:
        if word != "":
            clean_word = ""
            for letter in word:
                if letter == "'":
                    clean_word += letter.lower()
                elif letter.isalpha():
                    clean_word += letter.lower()
            if clean_word in cache:
                cache[clean_word] += 1
            elif clean_word != "":
                cache[clean_word] = 1
    return cache


if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    # print(word_count('Hello, my cat.  And my cat doesn\'t say "hello" back.'))
    # print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count('a a\ra\na\ta \t\r\n'))
    print('a a\ra\na\ta \t\r\n')