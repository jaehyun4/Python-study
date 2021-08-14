def text_save(text):
    a = open("text.txt", "w")
    a.write(text)
    a.close()

def text_counter():
    count = 0
    for i in range(len(text)):
        if text[i] == word:
            count = count + 1
        else:
            continue
    print(count)

text = input("텍스트를 입력해주세요 :")
word = input("찾을 단어를 입력해주세요 :")

text_counter()
text_save(text)
