# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


phrase = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

f=open("re-encoding.txt","wt+", encoding="utf-8")
f_another=open("re-encoding_another.txt","wt", encoding="utf-8")
f_another.write(phrase)
f_another.close()
f_another=open("re-encoding_another.txt","rt", encoding="utf-8")
text_r = f_another.readlines()
for i in range(26):
    for line in text_r:
        for letter in line:
            if letter == " " or letter == "'" or letter == '.':
                f.write(letter)
            else:
                index_letter = ord(letter) - i
                if (index_letter - i) < ord("a"):
                    new_index = (ord("z") + 1 - (i - (index_letter - ord("a"))))
                else:
                    new_index = index_letter - i
                encrypted_letter = chr(new_index)
                f.write(chr(new_index))
    f.write("\n")
f.close()
f_another.close()
f=open("re-encoding.txt","rt", encoding="utf-8")
text_n = f.readlines()
print(text_n[3])
f.close()