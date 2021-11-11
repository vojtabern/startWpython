import datetime


class Person:
    def __init__(self, nickname: str, sex: str):
        self.nickname = nickname
        self.sex = sex
        self.__birth = datetime.datetime.now()

    def __str__(self):
        return f"Nickname: {self.nickname}, sex: {self.sex}"

    def get_seconds_from_birth(self):
        actual_time = datetime.datetime.now()
        return int((actual_time - self.__birth).total_seconds())


class Player(Person):
    def __init__(self, nickname: str, sex: str, state: str):
        super().__init__(nickname, sex)
        self.state = state
        self.count_of_games = 0
        self.wins = 0
        self.score = {"plus": 0, "minus": 0}

    def __str__(self):
        return f"Metoda predka: {super().__str__()}, state: {self.state}"

    def win_rate(self):
        try:
            rate = (self.wins / self.count_of_games)* 100
        except Exception as error:
            return error
        else:
            return float("{:.2f}".format(rate))


# test

person = Person("Karel", "man")
player = Player("Jana", "woman", "CZE")
player.count_of_games = 555
player.wins = 308
input("Pockej chvili a zadej enter")
print(person, person.get_seconds_from_birth())
print(player, player.get_seconds_from_birth())
print(f"{player.win_rate()}%")
