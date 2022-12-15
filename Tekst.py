# Zad 1
def main():
    words_list = [' się ', ' i ', ' oraz ', ' nigdy ', ' dlaczego ']

    with open("tekst.txt", 'r') as text_file:
        temp_text = text_file.read()

    for word in words_list:
        temp_text = temp_text.replace(word, " ")

    with open("replaced_file.txt", 'w') as edited_file_temp:
        edited_file_temp.write(temp_text)

    text_file.close()
    edited_file_temp.close()


if __name__== '_main_':
    main()

# Zad 2
def main():
    dictionaryOfWords = {" i ": " oraz ", " oraz ": " i ", " nigdy ": " prawie nigdy ", " dlaczego ": " czemu "}

    with open("tekst.txt", 'r') as text_file:
        temp_text = text_file.read()


    for word in dictionaryOfWords:
        temp_text = temp_text.replace(word, dictionaryOfWords[word])

    with open("replaced_file.txt", 'w') as edited_file_temp:
        edited_file_temp.write(temp_text)


    text_file.close()
    edited_file_temp.close()

if __name__ == '_main_':
    main()