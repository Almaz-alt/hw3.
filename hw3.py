# Класс Computer
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def get_cpu(self): return self.__cpu
    def set_cpu(self, cpu): self.__cpu = cpu
    def get_memory(self): return self.__memory
    def set_memory(self, memory): self.__memory = memory

    def make_computations(self):
        return f"Сумма: {self.__memory + 1}, Разница: {self.__memory - 1}, Умножение: {self.__memory * 2}"

    def __str__(self):
        return f"Computer: CPU={self.__cpu}, Memory={self.__memory}"

    def __eq__(self, other): return self.__memory == other.__memory
    def __ne__(self, other): return self.__memory != other.__memory
    def __lt__(self, other): return self.__memory < other.__memory
    def __le__(self, other): return self.__memory <= other.__memory
    def __gt__(self, other): return self.__memory > other.__memory
    def __ge__(self, other): return self.__memory >= other.__memory


# Класс Phone
class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards_list(self): return self.__sim_cards_list
    def set_sim_cards_list(self, sim_cards_list): self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            print(f"Звонок на {call_to_number} с SIM-{sim_card_number} - {self.__sim_cards_list[sim_card_number - 1]}")
        else:
            print("Неверный номер SIM-карты!")

    def __str__(self):
        return f"Phone: SIM-карты={', '.join(self.__sim_cards_list)}"


# Класс SmartPhone
class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Маршрут до {location} построен!")

    def __str__(self):
        return f"SmartPhone: {Computer.__str__(self)}, {Phone.__str__(self)}"


# Создание объектов
computer = Computer("Intel i5", 16)
phone = Phone(["Beeline", "MegaCom"])
smartphone1 = SmartPhone("Snapdragon 888", 8, ["O!", "Beeline"])
smartphone2 = SmartPhone("Apple A14", 12, ["MegaCom", "O!"])

# Вывод информации
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Тестирование методов
print(computer.make_computations())
phone.call(1, "+996777998811")
smartphone1.use_gps("Ош базар")
smartphone2.call(2, "+996555112233")

# Сравнение объектов
print(computer == smartphone1)
print(smartphone1 > smartphone2)
