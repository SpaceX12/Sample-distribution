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

df2 = pd.read_csv("data.csv")
data2 = df["reading_time"].tolist()
sample1_mean = statistics.mean(data2)
print("Mean of sample 1 is", sample1_mean)

first_std_deviation_start, first_std_deviation_end = sample_mean-sample_stdev, sample_mean+sample_stdev
second_std_deviation_start, second_std_deviation_end = sample_mean-(2*sample_stdev), sample_mean+(2*sample_stdev)
third_std_deviation_start, third_std_deviation_end = sample_mean-(3*sample_stdev), sample_mean+(3*sample_stdev)

print("std1",first_std_deviation_start, first_std_deviation_end)
print("std2",second_std_deviation_start, second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)

fig = ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[sample1_mean, sample1_mean], y=[0, 1], mode="lines", name="Mean of sample 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 1], mode="lines", name="Standard deviation 1 start"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 1], mode="lines", name="Standard deviation 1 end"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 1], mode="lines", name="Standard deviation 2 start"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 1], mode="lines", name="Standard deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,1], mode="lines", name="Standard deviation 3 start"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,1], mode="lines", name="Standard deviation 3 end"))
fig.show()

z_score = (sample1_mean - pop_mean)/sample_stdev

print("z score of the data is", z_score)