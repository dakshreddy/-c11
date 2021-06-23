import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")

data = df["Math_score"].tolist()

#fig = ff.create_distplot([data],["marks"],show_hist=False)

#fig.show()

mean = statistics.mean(data)
stev = statistics.stdev(data)
print("population mean:",mean)
print("population stdev:",stev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return(mean)

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

std_dev = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("sample mean:",mean)
print("sample stdev:",std_dev)
"""
fig = ff.create_distplot([mean_list],["marks"],show_hist=False)

fig.show()
"""
first_std_start,first_std_end = mean-std_dev,mean+std_dev
second_std_start,second_std_end = mean-(2*std_dev),mean+(2*std_dev)
third_std_start,third_std_end = mean-(3*std_dev),mean+(3*std_dev)
"""
fig = ff.create_distplot([mean_list],["marks"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [first_std_start,first_std_start],y = [0,0.17],mode = "lines",name = "1 stdev start"))
fig.add_trace(go.Scatter(x = [first_std_end,first_std_end],y = [0,0.17],mode = "lines",name = "1 stdev end"))

fig.add_trace(go.Scatter(x = [second_std_start,second_std_start],y = [0,0.17],mode = "lines",name = "2 stdev start"))
fig.add_trace(go.Scatter(x = [second_std_end,second_std_end],y = [0,0.17],mode = "lines",name = "2 stdev end"))

fig.add_trace(go.Scatter(x = [third_std_start,third_std_start],y = [0,0.17],mode = "lines",name = "3 stdev start"))
fig.add_trace(go.Scatter(x = [third_std_end,third_std_end],y = [0,0.17],mode = "lines",name = "3 stdev end"))

fig.show()
"""

df = pd.read_csv("data1.csv")

data1 = df["Math_score"].tolist()
mean_sample1 = statistics.mean(data1)

print("mean of sample 1 :",mean_sample1)
"""
fig = ff.create_distplot([mean_list],["marks"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [mean_sample1,mean_sample1],y = [0,0.17],mode = "lines",name = "sample1"))
fig.add_trace(go.Scatter(x = [first_std_start,first_std_start],y = [0,0.17],mode = "lines",name = "1 stdev start"))
fig.add_trace(go.Scatter(x = [first_std_end,first_std_end],y = [0,0.17],mode = "lines",name = "1 stdev end"))

fig.add_trace(go.Scatter(x = [second_std_start,second_std_start],y = [0,0.17],mode = "lines",name = "2 stdev start"))
fig.add_trace(go.Scatter(x = [second_std_end,second_std_end],y = [0,0.17],mode = "lines",name = "2 stdev end"))

fig.add_trace(go.Scatter(x = [third_std_start,third_std_start],y = [0,0.17],mode = "lines",name = "3 stdev start"))
fig.add_trace(go.Scatter(x = [third_std_end,third_std_end],y = [0,0.17],mode = "lines",name = "3 stdev end"))

fig.show()
"""

df = pd.read_csv("data2.csv")

data2 = df["Math_score"].tolist()
mean_sample2 = statistics.mean(data2)

print("mean of sample 2 :",mean_sample2)
"""
fig = ff.create_distplot([mean_list],["marks"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [mean_sample2,mean_sample2],y = [0,0.17],mode = "lines",name = "sample2"))
fig.add_trace(go.Scatter(x = [first_std_start,first_std_start],y = [0,0.17],mode = "lines",name = "1 stdev start"))
fig.add_trace(go.Scatter(x = [first_std_end,first_std_end],y = [0,0.17],mode = "lines",name = "1 stdev end"))

fig.add_trace(go.Scatter(x = [second_std_start,second_std_start],y = [0,0.17],mode = "lines",name = "2 stdev start"))
fig.add_trace(go.Scatter(x = [second_std_end,second_std_end],y = [0,0.17],mode = "lines",name = "2 stdev end"))

fig.add_trace(go.Scatter(x = [third_std_start,third_std_start],y = [0,0.17],mode = "lines",name = "3 stdev start"))
fig.add_trace(go.Scatter(x = [third_std_end,third_std_end],y = [0,0.17],mode = "lines",name = "3 stdev end"))

fig.show()
"""
df = pd.read_csv("data3.csv")

data3 = df["Math_score"].tolist()
mean_sample3 = statistics.mean(data3)

print("mean of sample 3 :",mean_sample3)
"""
fig = ff.create_distplot([mean_list],["marks"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [mean_sample3,mean_sample3],y = [0,0.17],mode = "lines",name = "sample3"))
fig.add_trace(go.Scatter(x = [first_std_start,first_std_start],y = [0,0.17],mode = "lines",name = "1 stdev start"))
fig.add_trace(go.Scatter(x = [first_std_end,first_std_end],y = [0,0.17],mode = "lines",name = "1 stdev end"))

fig.add_trace(go.Scatter(x = [second_std_start,second_std_start],y = [0,0.17],mode = "lines",name = "2 stdev start"))
fig.add_trace(go.Scatter(x = [second_std_end,second_std_end],y = [0,0.17],mode = "lines",name = "2 stdev end"))

fig.add_trace(go.Scatter(x = [third_std_start,third_std_start],y = [0,0.17],mode = "lines",name = "3 stdev start"))
fig.add_trace(go.Scatter(x = [third_std_end,third_std_end],y = [0,0.17],mode = "lines",name = "3 stdev end"))

fig.show()

"""
z_score1 = (mean_sample1-mean)/std_dev
print("the z score of sample 1 is:",z_score1)

z_score2 = (mean_sample2-mean)/std_dev
print("the z score of sample 2 is:",z_score2)

z_score3 = (mean_sample3-mean)/std_dev
print("the z score of sample 3 is:",z_score3)































































