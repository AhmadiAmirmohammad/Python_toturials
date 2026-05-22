from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self) -> None:
        pass


class Sheet2(Observer):
    def __init__(self, data_source):
        self.data_source = data_source

    def update(self) -> None:
        self.total = self.calculate_total(self.data_source.values)

    def calculate_total(self, values: list[float]):
        sum = 0
        for value in values:
            sum += value
        self.total = sum
        print(f"New total is: {self.total}")
        return self.total


class BarChart(Observer):
    def __init__(self, data_source):
        self.data_source = data_source

    def update(self):
        print("Rendering bar chart with new values")


class Subject:
    def __init__(self):
        self.observers: list[Observer] = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update() # pull method
            #pull method: observer used anything dataSource in own class

            #push method: any change send for all observer perhaps need or not need
            #observer.update(values)


class DataSource(Subject):
    def __int__(self):
        super().__init__()
        self._values = list[float] = []

    @property
    def values(self) -> list[float]:
        return self._values

    @values.setter
    def values(self, values: list[float]) -> None:
        self._values = values
        super().notify_observers(values)


data_source = DataSource()
sheet2 = Sheet2(data_source)
barChart = BarChart(data_source)

data_source.add_observer(sheet2)
data_source.add_observer(barChart)

data_source.values = [12.6, 4, 1, 51, 5, 1]
print(data_source.values)

