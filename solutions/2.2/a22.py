name = input("Как Вас зовут?\n")
print(f"Здравствуйте, {name}!")
print("Как дела?")
whatsapp = input()
match whatsapp:
    case "плохо":
        print("Всё наладится!")
    case "хорошо":
        print("Я за вас рада!")
