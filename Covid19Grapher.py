import covid_cases as cc
import milestone as ms
import covid_deaths as cd

countries = cc.c_list()

#request input for countries
print("enter the countries to graph (any 5 valid country input): ")
c=""
country_list=[]
country_index=[]
cnt=0

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

while(True):
    print("\nEnter the option: \n1 - Total Deaths\n2 - Total Cases\n3 - Milestones India\n4 - World Choropleth Map\n5 - Exit :")
    opt = int(input())
    if (opt == 1):
        cc.plot_graph_cases(country_index, country_list)
    elif(opt == 2):
        cd.plot_graph_deaths(country_index, country_list)
    elif (opt == 3):
        ms.print_milestone()
    elif (opt == 4):
        print("opt = 4")
    else:
        print("\nTHANK YOU FOR USING THE COVID-19 GRAPHER !")
        break


