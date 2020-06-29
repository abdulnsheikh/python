# import the library     
from matplotlib import pyplot as plt 
from collections import Counter
import csv


with open('languages.csv') as file:
	csv_reader = csv.DictReader(file)

	languages_counter = Counter()

	for row in csv_reader:
		languages_counter.update(row["Languages_Spoken"].split(";"))

languages = []
rank = []

for item in languages_counter.most_common(15):
	languages.append(item[0])
	rank.append(item[1])

languages.reverse()
rank.reverse()

# horizon bar chart
plt.barh(languages, rank, color='r')

# change the title  
plt.title("Most popular language according to the survey")

# change x axis name  
plt.xlabel("Number of people who speak the language") 

# make window fluid tight_layout  
plt.tight_layout() 

# show the graph object in the window  
plt.show()

