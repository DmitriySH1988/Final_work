class РеестрДомашнихЖивотных:
    def __init__(self):
        self.счетчик = Счетчик()
        self.домашние_животные = []
        self.вьючные_животные = []

    def завести_новое_животное(self):
        имя = input("Введите имя животного: ")
        команда = input("Введите команду для животного: ")
        дата_рождения = input("Введите дату рождения животного (гггг-мм-дд): ")

        if имя and команда and дата_рождения:
            возраст = self.считать_возраст(дата_рождения)
            if возраст < 0:
                print("Ошибка: неправильная дата рождения.")
            elif возраст >= 1 and возраст < 3:
                молодое_животное = МолодыеЖивотные(имя, команда, дата_рождения, возраст)
                if isinstance(молодое_животное, ДомашниеЖивотные):
                    self.домашние_животные.append(молодое_животное)
                elif isinstance(молодое_животное, ВьючныеЖивотные):
                    self.вьючные_животные.append(молодое_животное)
                self.счетчик.add()
                print("Животное успешно добавлено.")
            else:
                print("Животное слишком молодое или слишком старое для добавления.")
        else:
            print("Ошибка: не все поля заполнены.")

    def определить_животное(self, имя_животного):
        for животное in self.домашние_животные:
            if животное.имя == имя_животного:
                return "Домашнее животное: " + животное.имя
        for животное in self.вьючные_животные:
            if животное.имя == имя_животного:
                return "Вьючное животное: " + животное.имя
        return "Животное не найдено."

    def увидеть_список_команд(self, имя_животного):
        for животное in self.домашние_животные:
            if животное.имя == имя_животного:
                return "Команды для " + животное.имя + ": " + животное.команда
        for животное in self.вьючные_животные:
            if животное.имя == имя_животного:
                return "Команды для " + животное.имя + ": " + животное.команда
        return "Животное не найдено."

    def обучить_животное(self, имя_животного, новая_команда):
        for животное in self.домашние_животные:
            if животное.имя == имя_животного:
                животное.команда = новая_команда
                return "Команда для " + животное.имя + " обновлена: " + животное.команда
        for животное in self.вьючные_животные:
            if животное.имя == имя_животного:
                животное.команда = новая_команда
                return "Команда для " + животное.имя + " обновлена: " + животное.команда
            return "Животное не найдено."
        
    def навигация_по_меню(self):
        while True:
            print("Меню:")
            print("1. Завести новое животное")
            print("2. Определить животное")
            print("3. Увидеть список команд")
            print("4. Обучить животное")
            print("5. Выйти")
            выбор = input("Выберите действие: ")
            if выбор == "1":
                self.завести_новое_животное()
            elif выбор == "2":
                имя = input("Введите имя животного: ")
                print(self.определить_животное(имя))
            elif выбор == "3":
                имя = input("Введите имя животного: ")
                print(self.увидеть_список_команд(имя))
            elif выбор == "4":
                имя = input("Введите имя животного: ")
                новая_команда = input("Введите новую команду: ")
                print(self.обучить_животное(имя, новая_команда))
            elif выбор == "5":
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите снова.")

class Счетчик:
    def init(self):
        self.значение = 0

    def add(self):
        self.значение += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            if self.значение != 0:
                raise Exception("Ресурс не был закрыт.")
            

# Теперь, чтобы воспользоваться этими классами и программой, вы можете сделать следующее:

реестр = РеестрДомашнихЖивотных()

try:
    with реестр.счетчик:
        реестр.навигация_по_меню()
except Exception as e:
    print(e)



