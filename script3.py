#Код для задания 1
import matplotlib.pyplot as plt
from sklearn import datasets

# Загружаем данные iris
iris = datasets.load_iris()
X = iris.data[:, :2]  # sepal length и sepal width
y = iris.target
target_names = iris.target_names

# Цвета для классов
colors = ['purple', 'teal', 'yellow']

plt.figure(figsize=(8,6))
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X[y == i, 0], X[y == i, 1], color=color, label=target_name)

plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal width (cm)')
plt.title("Iris' sepal sizes")
plt.legend()
plt.show()


#Код для задания 2
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Загружаем данные co2
data = sm.datasets.co2.load_pandas().data

# Данные содержат пропуски, уберём их
data = data.resample('M').mean().fillna(method='ffill')

plt.figure(figsize=(10,6))
plt.plot(data.index, data.co2, label='CO2 concentration')
plt.title('CO2 concentration over time')
plt.xlabel('Year')
plt.ylabel('CO2 (ppm)')
plt.legend()
plt.show()

