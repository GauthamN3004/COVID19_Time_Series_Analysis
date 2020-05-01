import covid_deaths as cd
import covid_cases as cc
import pandas as pd

url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
df = pd.read_csv(url)
df.drop(columns=["Province/State","Lat","Long"],inplace=True)
df=df.groupby(["Country/Region"],as_index=False).sum()

def print_milestone():
    print("Milestones (India)")
    india = df.loc[df["Country/Region"] == "India"]
    max_case = int(india.iloc[0, -1])
    case_list = [1, 10]
    n = 1

    while n <= max_case:
        if (len(case_list) - 1) % 3 == 2:
            n = int(case_list[len(case_list) - 1] * 2.5)
            case_list.append(n)
        else:
            n = case_list[len(case_list) - 1] * 2
            case_list.append(n)
    case_list.append(30000)
    case_list.sort()
    total_columns = len(list(india.columns))
    cols = list(india.columns)
    i = 1
    j = 0
    months = ["Unknown", "January", "Febuary", "March", "April", "May", "June", "July", "August", "September",
              "October", "November", "December"]
    n = case_list[j]
    while (i < total_columns):
        if (india.iloc[0, i] >= n):
            date = cols[i].split("/")
            print("case %-7d" % case_list[j], ":  ", date[1], months[int(date[0])], date[2])
            j += 1
            n = case_list[j]
        i += 1

    return
