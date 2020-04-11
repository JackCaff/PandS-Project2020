# Jack Caffrey
# PandS Project 2020 Solution

# Initial program to verify various aspect of the program are working as required. 

import pandas as  pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris_csv.csv")
f = open("Summary.txt","a") #created Summary.txt file and appends to this file
print (df) # used to display Summary. 
f.close() #close Summary.txt

plt.scatter(df['sepallength'], df['sepalwidth']) #plots two variables to a scatter plot

df.hist(bins=150) #plots a histogram of the various variables for the CSV file

plt.show()# displays both plots.
