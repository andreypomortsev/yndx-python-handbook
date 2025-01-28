class Programmer:
    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position
        self.position_salary = {"Junior": 10, "Middle": 15, "Senior": 20}
        self.bucks_per_hour = self.position_salary[self.position]
        self.hours = self.salary = 0

    def work(self, hours: int) -> None:
        self.hours += hours
        self.salary += self.bucks_per_hour * hours

    def rise(self) -> None:
        match self.bucks_per_hour:
            case 10:
                self.position = "Middle"
                self.bucks_per_hour = self.position_salary[self.position]
            case 15:
                self.position = "Senior"
                self.bucks_per_hour = self.position_salary[self.position]
            case _:
                self.bucks_per_hour += 1

    def info(self) -> str:
        info = f"{self.name} {self.hours}ч. {self.salary}тгр."
        return info
