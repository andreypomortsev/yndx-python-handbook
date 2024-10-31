name = input("Как Вас зовут?\n")
print(f"Здравствуйте, {name}!")
whatsapp = input("Как дела?\n")

match whatsapp:
    case "плохо":
        print("Всё наладится!")
    case "хорошо":
        print("Я за вас рада!")
