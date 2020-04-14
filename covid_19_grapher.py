#importing libraries
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

#request input for countries
print("enter the countries to graph (any 5 valid country input): ")
c=""
country_list=[]
country_index=[]
cnt=0

#function to print results
def print_result(data,c_list,c_index,str):
    date = data.iloc[-1, 0]
    print("\n\tTotal",str,"as of",date)
    for i in range(5):
        print(c_list[i]," : ",data.iloc[-1,c_index[i]])
    print("\n\n")

#read 5 valid inputs from the user and store the index,name in separate lists
#you can also implement this as a list of tuples
while True:
    if cnt==5:
        break
    print("Country ",(cnt+1)," :",end=" ")
    c=input().lower()
    for index,i in enumerate(countries):
        copy_cnt=cnt
        if(i.lower()==c):
            country_list.append(i)
            country_index.append(index+1)
            cnt += 1
            break
    if(copy_cnt==cnt):
        print("No Such Country or Country Mis-spelt! Re-enter !")

#storing data points for each of the countries
xval=[]
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
x_data=[]
index=count()
row=data.shape[0]
flag=0
#animating the graph plotting
print("\n\nPlotting Total Cases vs Time graph...")
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
    if(flag==0):
        plt.title("Total Number of Cases Vs Time")
        plt.ylabel("Total Number of Cases")
    else:
        plt.title("Total Number of Deaths Vs Time")
        plt.ylabel("Total Number of Deaths")


plt.xlim(0,)
plt.ylim(0,)
ani=FuncAnimation(plt.gcf(),animate_total,interval=150)
plt.show()
#print results
print_result(data,country_list,country_index,"Cases")

flag=1
#animating COVID-19 death
#reading the data for deaths
df=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
df.drop(columns=["Province/State","Lat","Long"],inplace=True)
df=df.groupby(["Country/Region"],as_index=False).sum()
df.loc[df["Country/Region"]=="US","Country/Region"]="United States"
countries=list(df["Country/Region"])

data=transform(df)

xval=[]
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
x_data=[]
index=count()
row=data.shape[0]
print("Plotting Total Deaths vs Time graph...")
plt.xlim(0,)
plt.ylim(0,)
ani=FuncAnimation(plt.gcf(),animate_total,interval=150)
plt.show()
print_result(data,country_list,country_index,"Deaths")

print("Milestones (India)")
india = df.loc[df["Country/Region"] == "India"]
print(india)
max_case= int(india.iloc[0,-1])
case_list = [1,10]
n=1
while n<=max_case:
	if(len(case_list)-1)%3 ==2:
		n=int(case_list[len(case_list)-1]*2.5)
		case_list.append(n)
	else:
		n=case_list[len(case_list)-1]*2
		case_list.append(n)

total_columns = len(list(india.columns))
cols = list(india.columns)
i=1
j=0
months = ["Unknown","January","Febuary","March","April","May","June","July","August","September","October","November","December"]
n=case_list[j]
while(i<total_columns):
    if(india.iloc[0,i]>=n):
        date = cols[i].split("/")
        print("case %-7d"%case_list[j],":  ",date[1],months[int(date[0])],date[2])
        j+=1
        n=case_list[j]
    i+=1


input("press the enter key to exit!")
