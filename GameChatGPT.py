#1.різниця мого коду і коду який написав ChatGPT полягає в тому що мій код був написаний в ооп парадигмі а код ChatGPT в процедурній парадигмі
#2.різниця полягає в тому що в грі ChatGPT золото нараховується за правильні відповіді а в моїй грі золото можна взяти лише тоді коли всі nps переможенні і позиція player рівна позиції cold
#3.в моїй грі  питання йшли по порядку і вкожного nps були свої питання а в ChatGPT питання випадкові

import random

# Початкова позиція персонажа
character_position = (0, 0)

# Початкова позиція NPC
npc_position = (2, 2)

# Початкова кількість золота
gold = 0

# Змінні, що містять питання та відповіді NPC
npc_questions = {
    "Чому небо синє?": "Бо розсіюється синє світло.",
    "Яка столиця Франції?": "Париж.",
    "Скільки місяців у році?": "12 місяців.",
}

# Функція для виводу карти
def display_map():
    # в моїй грі я використовую двохмірний масив в циклі фор дістаю підмасив і зліплюю елементи підмасву докупи за допомогою методу рядка join і виводжу в консоль
    for i in range(4):
        for j in range(4):
            # а от ChatGPT
            #провіряє  чи (і,j)=позиції player
            if (i, j) == character_position:
                print("X", end=" ")#виводить гравця
            # провіряє  чи (і,j)=позиції nps
            elif (i, j) == npc_position:
                print("N", end=" ")#виводити nps
            else:
                print(".", end=" ")#інакше в рядок виводить крапки
        print()#переносить на новий рядок

# Головний цикл гри
while True:
    print("\nВаша поточна кількість золота:", gold)
    display_map()

    # Перевірка, чи персонаж і NPC знаходяться на однаковій позиції
    if character_position == npc_position:
        print("\nNPC стоїть перед вами. Відповідайте на його питання, щоб отримати золото.")
        question = random.choice(list(npc_questions.keys()))
        correct_answer = npc_questions[question]
        user_answer = input(f"Питання NPC: {question}\nВаша відповідь: ")

        if user_answer.lower() == correct_answer.lower():
            print("Правильна відповідь! Ви отримуєте 1 золоту.")
            gold += 1
        else:
            print("Неправильна відповідь. Ви втрачаєте 1 золоту.")
            gold -= 1

        # Випадково перемістити NPC на нову позицію
        npc_position = (random.randint(0, 3), random.randint(0, 3))

    # Введення команди від користувача
    command = input("Введіть команду (вгору, вниз, вліво, вправо, вихід): ").lower()

    if command == "вихід":
        print("Гра завершена.")
        break
    #я замість вгору вниз вліво вправо використовував букви w s a d і-для інформації про характеристики персонажа e-для виходу з гри
    elif command in ["вгору", "вниз", "вліво", "вправо"]:
        # Рух персонажа
        x, y = character_position
        if command == "вгору" and x > 0:
            character_position = (x - 1, y)
        elif command == "вниз" and x < 3:
            character_position = (x + 1, y)
        elif command == "вліво" and y > 0:
            character_position = (x, y - 1)
        elif command == "вправо" and y < 3:
            character_position = (x, y + 1)
    else:
        print("Неправильна команда. Введіть 'вгору', 'вниз', 'вліво', 'вправо' або 'вихід'.")