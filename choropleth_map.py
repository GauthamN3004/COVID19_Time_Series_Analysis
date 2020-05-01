import matplotlib.pyplot as plt
import pandas as pd
import folium
import json
import warnings
import numpy as np
from urllib.request import urlopen
import json
from IPython.display import display
with urlopen('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/world_countries.json') as response:
    data = json.load(response)

YlOrRd = {
    3: ["rgb(255,237,160)", "rgb(254,178,76)", "rgb(240,59,32)"],
    4: ["rgb(255,255,178)", "rgb(254,204,92)", "rgb(253,141,60)", "rgb(227,26,28)"],
    5: ["rgb(255,255,178)", "rgb(254,204,92)", "rgb(253,141,60)", "rgb(240,59,32)", "rgb(189,0,38)"],
    6: ["rgb(255,255,178)", "rgb(254,217,118)", "rgb(254,178,76)", "rgb(253,141,60)", "rgb(240,59,32)", "rgb(189,0,38)"],
    7: ["rgb(255,255,178)", "rgb(254,217,118)", "rgb(254,178,76)", "rgb(253,141,60)", "rgb(252,78,42)", "rgb(227,26,28)", "rgb(177,0,38)"],
    8: ["rgb(255,255,204)", "rgb(255,237,160)", "rgb(254,217,118)", "rgb(254,178,76)", "rgb(253,141,60)", "rgb(252,78,42)", "rgb(227,26,28)", "rgb(177,0,38)"],
    9: ["rgb(255,255,204)", "rgb(255,237,160)", "rgb(254,217,118)", "rgb(254,178,76)", "rgb(253,141,60)", "rgb(252,78,42)", "rgb(227,26,28)", "rgb(189,0,38)", "rgb(128,0,38)"]
}

print('GeoJSON file downloaded!')
df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
df.drop(columns=["Province/State","Lat","Long"],inplace=True)
df=df.groupby(["Country/Region"],as_index=False).sum()
df.loc[df["Country/Region"]=="US","Country/Region"]="United States of America"
countries=list(df["Country/Region"])
df.head()
df.iloc[:,-1] = np.log(df.iloc[:,-1].values)/np.log(9)

def choropleth_map():
    column1 = df.columns[0]
    column2 = df.columns[-1]
    world_map = folium.Map(location=[0, 0], zoom_start=2, tiles='Stamen Terrain', max_bounds=True)
    world_map.choropleth(
        geo_data=data,
        name='choropleth',
        data=df,
        columns=['Country/Region', column2],
        key_on='feature.properties.name',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=1,
        min_zoom=10,
        max_zoom=10,
        bins=[0, 0.8, 1.6, 2.4, 3.2, 4.0, 4.8, 5.6, 6.4],
        legend_name='log(number of cases) base 9'
    )
    display(world_map)
    warnings.simplefilter("ignore")
    return
