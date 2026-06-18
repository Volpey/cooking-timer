class Recipe:
    def __init__(self, name, cooking_time, temperature):
        self.name = name
        self.cooking_time = cooking_time
        self.temperature = temperature

    def show_info(self):
        print()
        print(self.name)
        print()
        print(f"Empfohlene Zeit: {self.cooking_time} Minuten")

        if self.temperature is not None:
            print(f"Empfohlene Temperatur: {self.temperature}°C")

        print()

    def confirm(self):
        answer = input("Einverstanden? (y/n): ")
        return answer.lower() == "y"