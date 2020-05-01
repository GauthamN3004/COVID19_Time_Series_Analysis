import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import math

#fetching data

url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
df = pd.read_csv(url)
df.drop(columns=["Province/State","Lat","Long"],inplace=True)
df=df.groupby(["Country/Region"],as_index=False).sum()
df.loc[df["Country/Region"]=="US","Country/Region"]="United States"
countries=list(df["Country/Region"])


#function to return the set of countries
def c_list():
    return countries

def print_result(data,c_list,c_index,str):
    date = data.iloc[-1, 0]
    print("\n\tTotal",str,"as of",date)
    for i in range(5):
        print(c_list[i]," : ",data.iloc[-1,c_index[i]])
    print("\n")

#transforming data such that the headers are the country names and add date as another column
def transform(df):
    dates = list(df.columns)[1:]
    data = df.transpose()
    headers = list(data.iloc[0, :])
    data = data.iloc[1:, :]
    data.columns = headers
    data.insert(0, "dates", dates, True)
    data.reset_index(inplace=True, drop=True)
    return data

data=transform(df)

xval = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
x_data = []
country_index = []
country_list =[]
index=count()
row = data.shape[0]

def animate_total(i):
    z=next(index)
    if z>=row:
        return
    j=int(z)
    xval.append(z)
    x_data.append(data.iloc[z,0])
    y1.append(data.iloc[z,country_index[0]])
    y2.append(data.iloc[z, country_index[1]])
    y3.append(data.iloc[z, country_index[2]])
    y4.append(data.iloc[z, country_index[3]])
    y5.append(data.iloc[z, country_index[4]])
    plt.cla()
    plt.plot(x_data,y1,label=country_list[0])
    plt.xticks(list(x_data)[::math.ceil((z+1)/7)])
    plt.plot(x_data, y2, label=country_list[1])
    plt.plot(x_data, y3, label=country_list[2])
    plt.plot(x_data, y4, label=country_list[3])
    plt.plot(x_data, y5, label=country_list[4])
    plt.legend()
    plt.xlabel("Date")
    plt.title("Total Number of Cases Vs Time")
    plt.ylabel("Total Number of Cases")


def plot_graph_cases(ci,cl):
    global country_index,country_list,xval,y1,y2,y3,y4,y5,x_data,index
    xval = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    x_data = []
    index = count()
    country_index = ci[:]
    country_list = cl[:]
    # animating the graph plotting
    print("\n\nPlotting Total Cases vs Time graph...")
    plt.xlim(0, )
    plt.ylim(0, )
    ani = FuncAnimation(plt.gcf(), animate_total, interval=150)
    plt.show()
    # print results
    print_result(data, country_list, country_index, "Cases")
    return