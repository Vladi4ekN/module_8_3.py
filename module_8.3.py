class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.__numbers = self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер.")

        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера.")

        return vin_number  

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров.")

        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера, должна состоять ровно из 6 символов.")

        return numbers

    def get_info(self):
        return f"Модель: {self.model}, VIN: {self.__vin}, Номер: {self.__numbers}"

try:
    car = Car("Toyota Camry", 1234567, "A123BC")
    print(car.get_info())
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
    print(e.message)

try:
    car = Car("Honda Accord", "1234567", "B456C")
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
    print(e.message)

try:
    car = Car("Ford Focus", 12345678, "C789DE")
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
    print(e.message)

try:
    car = Car("Mazda 3", 1234567, 123456)
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
    print(e.message)

try:
    car = Car("Nissan Altima", 1234567, "A1B2C")
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
    print(e.message)
