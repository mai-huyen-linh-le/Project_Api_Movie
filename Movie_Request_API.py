import requests 
import csv
from key import Key_Api
import pandas as pd

# Read file 'oscar_winners.csv' file
oscar_winners = pd.read_csv(r"oscar_winners.csv")
Column_Name = ['Movie Title', 'Runtime', 'Genre', 'Award Wins', 'Award Nominations', 'Box Office', 'Director', 'Plot', 'DVD']

All_Data_Rows_List = []

for id in oscar_winners['IMDB']:
    rows_list = []
    data = requests.get(f"http://www.omdbapi.com/?apikey={Key_Api}&i={id}").json()
    Title = rows_list.append(data["Title"])
    Runtime = rows_list.append(data['Runtime'].split()[0])
    Genre = rows_list.append(data['Genre'])
    Award_Wins = rows_list.append(data['Awards'].split()[3])
    Award_Nominations = rows_list.append((data['Awards'].split()[6]))
    Box_Office = rows_list.append(data['BoxOffice'])
    # Additional columns
    Director = rows_list.append(data['Director'])
    Plot = rows_list.append(data['Plot'])
    Dvd = rows_list.append(data['DVD'])

    All_Data_Rows_List.append(rows_list)

# Maybe you need to turn off Window Defender or change local file path to run this code below
file_path = r'data_movie.csv'

with open("New_Movies.csv",'w') as f:
    writer = csv.writer(f)
    writer.writerow(Column_Name)
    for movie in All_Data_Rows_List:
        writer.writerow(movie)
