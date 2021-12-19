import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv('medium_data.csv')
data = df["reading_time"].tolist()

pop_mean = statistics.mean(data)
print( "Population mean is ", pop_mean)


mean_list = []
for i in range(0, 100):
    dataset = []
    for i in range(0, 30):
        value = data[random.randint(0,len(data)-1)]
        dataset.append(value)
        mean = statistics.mean(dataset)
        mean_list.append(mean)

sample_mean = statistics.mean(mean_list) 
print( "Sample data mean is", sample_mean) 

sample_stdev = statistics.stdev(mean_list) 
print( "Sample data standard deviation is", sample_stdev)  

df2 = mean_list
mean = statistics.mean(df2)
fig = ff.create_distplot([df2], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,1], mode="lines", name='Mean'))
fig.show()