import random

inventory = []
reputation_with_yoko = 0

def main_menu():
    print("Yoko house")
    print("18+")
    print("1. Начать игру")
    print("2. Читать лор")
    print("3. Выход")
    choice = input("Выбери действие: ")
    if choice == "1":
        intro()
    elif choice == "2":
        read_lore()
    elif choice == "3":
        exit_game()
    else:
        print("Неверный выбор. Попробуй снова.")
        main_menu()

def read_lore():
    print("\nИди смотреть плейлист Яндере на канале Лист Травки и после сыграй в Yoko no Hahashi.")
    main_menu()

def exit_game():
    print("\nДо свидания! Возвращайся, если захочешь снова сыграть.")
    exit()

def intro():
    print("Ты сбежал от Йоко в заброшенном колледже. После случившегося ты спишь в мягкой кровати, укутывшись клетчатым одеялом.")
    print("Ты чувствуешь какое-то прикосновение к своей голове и слышишь слова:")
    print("'Ха-ха-ха... Ты думал, что от меня будет так легко убежать? Дурачок.'")
    start_game()

def start_game():
    print("На утро ты увидел записку рядом с кроватью.")
    print("'Ты решил сбежать с того квеста. Я не потерплю это. Поэтому твой дом теперь квест. Удачи, милый.'")
    print("\n1. Начать исследовать дом")
    print("2. Игнорировать духа и выйти на улицу")
    choice = input("Выбери действие: ")
    if choice == "1":
        explore_room()
    elif choice == "2":
        leave_house()
    else:
        print("Неверный выбор. Попробуй снова.")
        start_game()

def leave_house():
    print("\nТы решаешь игнорировать Йоко и пытаешься выйти на улицу через окно.")
    print("Йоко не отпускает тебя и бьет по голове. Ты теряешь сознание и просыпаешься через 3 минуты.")
    change_reputation(-1)
    start_game()

def explore_room():
    print("\nТы начинаешь исследовать теперь Зоны Квеста (вашей хаты).")
    print("Дверь из комнаты закрыта, нужно искать ключ.")
    print("\n1. Вырвать заколку с волос Йоко")
    print("2. Искать ключ от комнаты по ящикам")
    choice = input("Выбери действие: ")
    if choice == "1":
        hack_and_slash()
    elif choice == "2":
        keysearch()
    else:
        print("Неверный выбор. Попробуй снова.")
        explore_room()

def hack_and_slash():
    print("\nТы осторожно вырываешь заколку с волос Йоко.")
    inventory.append("Заколка с волос Йоко")
    change_reputation(1)
    print("Инвентарь: ", inventory)
    yoko_hairpin()

def keysearch():
    print("\nТы начинаешь искать ключ в ящиках и находишь его.")
    inventory.append("Ключ")
    print("Инвентарь: ", inventory)
    roomkey()

def yoko_hairpin():
    print("Ты взламываешь дверь и после открываешь")
    print("\nЙоко забирает заколку обратно.")
    inventory.remove("Заколка с волос Йоко")
    print("Инвентарь: ", inventory)
    explore_hall()

def roomkey():
    print("Дверь открыта, но ключ оказался одноразовым")
    inventory.remove("Ключ")
    print("Инвентарь: ", inventory)
    explore_hall()

def explore_hall():
    print("Ты открываешь дверь и выходишь в коридор. Возле неё уже появляется Йоко, а рядом с ней баннер:")
    print("'А ты донатил в Yoko no Hahashi?'")
    print("На ней красовалась Йоко с белыми волосами и красными глазами.")
    print("\n1. Ответить да, смотря на баннер")
    print("2. Игнорировать")
    choice = input("Выбери действие: ")
    if choice == "1":
        donate_ending()
    elif choice == "2":
        explore_kitchen()
    else:
        print("Неверный выбор. Попробуй снова.")
        explore_hall()

def explore_kitchen():
    print("\nТы игнорируешь баннер и идешь дальше на кухню.")
    print("Чтобы успокоить Йоко, ты решаешь приготовить ей омлет.")
    print("\nНеобходимо собрать: сковородку, растительное масло, молоко, соль и яйца.")
    print("\n1. Искать на кухне сковородку")
    print("2. Искать растительное масло")
    print("3. Искать молоко")
    print("4. Искать соль")
    print("5. Искать яйца")
    print("6. Искать секрет")
    choice = input("Выбери действие: ")
    if choice == "1":
        find_item("Сковородка")
    elif choice == "2":
        find_item("Растительное масло")
    elif choice == "3":
        find_item("Молоко")
    elif choice == "4":
        find_item("Соль")
    elif choice == "5":
        find_item("Яйца")
    elif choice == "6":
        find_secret_key()
    else:
        print("Неверный выбор. Попробуй снова.")
        explore_kitchen()

def find_item(item):
    if item not in inventory:
        inventory.append(item)
        print("\nТы нашел", item)
    else:
        print(item, "уже есть в твоем инвентаре.")
    print("Инвентарь: ", inventory)
    check_ingredients()

def find_secret_key():
    print("\nТы решаешь поискать секретный ключ.")
    rid()

def rid():
    answer = input("\nЗагадка: \"Что имеет ключ, но не может открыть дверь?\" ")
    if answer.lower() == "пианино" or answer.lower() == "фильм":
        print("Правильно! Ты находишь секретный ключ.")
        inventory.append("Секретный ключ")
        print("Инвентарь: ", inventory)
        escape_from_house_or_not()
    else:
        print("Неправильно. Продолжай искать или попробуй снова.")
        rid()

def check_ingredients():
    required_items = ["Сковородка", "Растительное масло", "Молоко", "Соль", "Яйца"]
    if all(item in inventory for item in required_items):
        print("\nТы собрал(а) все необходимые ингредиенты для омлета.")
        print("Йоко довольна твоими усилиями.")
        change_reputation(1)
        dinners()
    else:
        explore_kitchen()

def dinners():
    print("*Хоть омлет и готовят на завтрак, но Йоко режила что пусть будет так*")
    print("*Ты и Йоко едят. Она умиляется, когда ты ешь*")
    change_reputation(1)
    bedroom()
def bedroom():
    print("*Она тебя отводит в комнату родителей на второй этаж и после села на кровать*")
    print("Ты меня как я вижу любишь. Но почему-то ты сбежал от меня тогда? Может потому что боишься меня7")
    print("Не бойся. Я больше не буду бить тебя ножом. Ложись ко мне на коленочки")
    print("1. Лечь на коленочки")
    print("2. Отказаться")
    choice = input("Выбери действие: ")
    if choice == "1":
        kneel()
    elif choice == "2":
        no()
    else:
        print("Неверный выбор. Попробуй снова.")
        bedroom()

def no():
    print("Почему? Страх?")
    print("Все будет хорошо. Я понимаю что ты боишься меня. Я сделала ошибку и хочу её исправить")
    print("Садись, ты мой маленький мальчик")
    print("*Ты медленно идешь назад*")
    print("Если ты не можешь, то...может когда-нибудь встретимся ещё7 Можешь идти...Я поняла тебя. Прости")
    good_enging()

def kneel():
    print("*Ты лег головой на её колени*")
    print("*Она гладит твою голову и тебя убаюкивает*")
    print("*Тепло...женское и любовное тепло*")
    change_reputation(4)
def escape_from_house_or_not():
    print("Ключ от выхода у меня есть...Надо сбежать или...Йоко...")
    print("Что же выбрать?")
    print("\n1. БЕЖАТЬ, БЕЖАТЬ, БЕЖАТЬ")
    print("2. Сохранить")

    choice = input("Выбери действие: ")
    if choice == "1":
        escape()
    elif choice == "2":
        save()
    else:
        print("Неверный выбор. Попробуй снова.")
        escape_from_house_or_not()

def escape():
    probability = random.randint(1, 100)
    if probability <= 30:
        good_enging()
    elif probability <= 95:
        wrong_key()

def  wrong_key():
    print("*Ключ оказался фальшивым и сломался*")
    inventory.remove("Секретный ключ")
    print("*Йоко это услышала и прибежала к тебе*")
    change_reputation(-8)

def save():
    print("*Ты решил сохранить ключ и Йоко проводит тебя в подвал*")
    print("*Она садит тебя на ковер и после...Говорит*")
    print("Ты сбежал от меня в колледже. Ты бросил меня там...Но...")
    print("Я знаю кто ты...Ты хочешь внимания...женского")
    print("Я тебе его дам. Хочешь?")
    print("1. Да")
    print("2. ПОШЛА *****")
    choice = input("Выбери действие")
    if choice == "1":
        mind_ending()
    elif choice == "2":
        yoko_sad()
    else:
        print("Неверный выбор. Попробуй снова.")
        save()

def yoko_sad():
    print("*Йоко плачет. Ей очень больно от твоего выбора*")
    print("Почему? ПОЧЕМУ НЕТ?! ПОЧЕМУ ТЫ ОТКАЗЫВАЕШЬСЯ ОТ МЕНЯ?")
    print("*Она кричит на тебя, однако дверь открыта*")
    print("1. БЕЖАТЬ")
    print("2. Принять судьбу")
    choice = input("Выбери действия: ")
    if choice == "1":
        good_enging()
    elif choice == "2":
        Yoko_Anger()
    else:
        print("Неверный выбор. Попробуй снова.")
        yoko_sad()

def Yoko_Anger():
    probability = random.randint(1, 100)
    if probability <= 50:
        print("*Йоко разозлилась!*")
        bad_ending()
    else:
        print("*Йоко приложила свою руку к твоей голове*")
        mind_ending()

def change_reputation(amount):
    global reputation_with_yoko
    reputation_with_yoko += amount
    print("Репутация с Йоко: ", reputation_with_yoko)
    if reputation_with_yoko >= 5:
        secret_ending()
    elif reputation_with_yoko <= -5:
        bad_ending()

def good_enging():
    print("Ты сбежал со своего дома. Ты двигаешься в сторону дома сестры, чтобы она смогла помочь тебе")
    print("Хорошая концовка: ПОБЕГ ИЗ ДОМА")
    exit()

def secret_ending():
    print("\nТы смог полюбить Йоко, а она поняла тебя")
    print("Теперь вы вместе навеки.")
    print("Секретная концовка: Вечная любовь.")
    exit()

def bad_ending():
    print("\nЙоко нападает на тебя и ты умираешь.")
    print("Плохая концовка: СМЭРТЬ.")
    exit()

def donate_ending():
    print("Ты закрываешь глаза и после открываешь.")
    print("Ты оказался в казино. Йоко что-то танцует, а все кто не был в очках вышли в транс")
    print("Какая-то пухлая девушка и парень, которые вне очков казались Вином из Tears of Themis и Арлекино из Geshin Impact")
    print("Почему-то за столом с картами сидел авокадо?")
    print("А рядом с ним Темный Лорд?")
    print("За спиной одного из игроков был флаг НСША, а на столе было до*** бабла")
    print("Донатная секртеная концовка: Прогрев гоев")
    exit()

def mind_ending():
    print("Йоко оказывается у тебя в голове и начинает изменять твою память, чтобы ты её полюбил")
    print("Нейтральная концовка: Смерть личности")
    exit()


main_menu()