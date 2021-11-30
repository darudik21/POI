
alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
itog = ''
smeshenie = int(input('Шаг шифровки: '))
message = input("Сообщение для шифровки: ").upper()
format_text="".join([c for c in message if c.isalpha() or c.isdigit() or c ==' ']).upper()
print(f" Текст без знаков припинания\n{format_text}")


for i in format_text:
        position = alfavit.find(i)
        new_position = position + smeshenie
        if i in alfavit:
            itog += alfavit[new_position]
        else:
            itog += i

print(f"Зашифрованное сообщение:\n {itog}.")




