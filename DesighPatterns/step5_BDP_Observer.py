# The observer pattern involves as object, known as the subject,
# maintaining a list of its dependent objects, called observers,
# and notifying them automatically of any state changes.

# ex. in sheets , use barchart and totalSum

class Sheet2:
    def __init__(self):
        self.total = 0

    def calculate_total(self, values: list[float]):
        sum = 0
        for value in values:
            sum += value
        self.total = sum
        print(f"New total is: {self.total}")
        return self.total


class BarChart:
    def render(self, values: list[float]):
        print("Rendering bar chart with new values")


class DataSource:
    def __int__(self):
        self._values = list[float] = []
        self.dependents = list[object] = []

    def add_dependent(self, dependent: object):
        self.dependents.append(dependent)

    def remove_dependent(self, dependent: object):
        self.dependents.remove(dependent)

    @property
    def values(self) -> list[float]:
        return self._values

    @values.setter
    def values(self, new_values: list[float]) -> None:
        self._values = new_values
        # update dependencies
        for dependent in self.dependents:
            if isinstance(dependent, Sheet2):
                dependent.calculate_total(new_values)
            elif isinstance(dependent, BarChart):
                dependent.render(new_values)


data_source = DataSource()
sheet2 = Sheet2()
barChart = BarChart()

data_source.add_dependent(sheet2)
data_source.add_dependent(barChart)
data_source.values = [12.6, 4, 1, 51, 5, 1]

print ("removing barchart")
data_source.remove_dependent(barChart)
data_source.values = [12.6, 4]
