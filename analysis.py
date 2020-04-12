# Jack Caffrey
# PandS Project 2020 Solution
# [#] indicates References which can be viewed in the README

#[4]
import pandas as  pd
import matplotlib.pyplot as plt

from matplotlib import pyplot as plt #Imports the library to save output as PNG file. 

df = pd.read_csv("iris_csv.csv")

#[5]
x=df["sepallength"].max()
y=df["sepallength"].min()
z=df["sepallength"].count()

#[6]
f = open("Summary.txt","w") #created Summary.txt file and appends to this file
f.write(f"The total number of samples recorded is {z}. \nThese samples are a combination of 3 sets of 50 Iris flower classes. These classes include: \nSetosa \nVersicolor \nVirginica. \n") # used to display Summary.
f.write(f" The largest value recorded for Sepal Length was {x} the smallest value recorded was {y} from the {z} samples.\n")
f.close() #close Summary.txt

#[7]
sepallenght = (df["sepallength"])
plt.hist([sepallenght]) #plts the Histogram 
plt.savefig('Sepal_Length.png')
plt.show()# displays Histograms .

#[4]
plt.scatter(df['sepallength'], df['sepalwidth']) #plots two variables to a scatter plot

plt.show() #Displays Scatter Plot


