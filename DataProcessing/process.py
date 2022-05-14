import pandas as pd
from neuralprophet import NeuralProphet
from matplotlib import pyplot as plt
import timeit

start = timeit.default_timer()

filename="predictionExTime.csv"
#csv = open(filename, 'w')	
#csv.write("execution time average\n")
#csv.close

df = pd.read_csv('sensorData.csv')
df.tail()

new_column = df[['TimeStamp', 'Temperature']]
new_column.dropna(inplace=True)
new_column.columns = ['ds', 'y']
new_column.tail()

n = NeuralProphet()
model = n.fit(new_column, freq='D')

future = n.make_future_dataframe(new_column, periods=1500)
forecast = n.predict(future)
forecast.tail()

plot = n.plot(forecast)
plt.show()

end = timeit.default_timer()
print("average",end-start)
csv = open(filename, 'a')
csv.write(str(end-start) + "\n")
csv.close 

