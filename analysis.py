# Jack Caffrey
# PandS Project 2020 Solution
# [#] indicates References which can be viewed in the README

#[4]
import pandas as  pd
import matplotlib.pyplot as plt
import numpy as py

from matplotlib import pyplot as plt #Imports the library to save output as PNG file. 


df = pd.read_csv("iris_csv.csv")
print (df.head(151))


#[5]
x=df["sepallength"].max()
x1=df["sepallength"].min()
x2=df["sepallength"].count()

y=df["sepalwidth"].max()
y1=df["sepalwidth"].min()

z=df["petallength"].max()
z1=df["petallength"].min()

w=df["petalwidth"].max()
w1=df["petalwidth"].min()

Total = (x2 * 3)

#[6]
f = open("Summary.txt","w") #created Summary.txt file and appends to this file
f.write(f"The total number of samples recorded is {Total}. \nThese samples are a combination of 3 sets of {x2} Iris flower classes. These classes include: \nSetosa \nVersicolor \nVirginica. \n") # used to display Summary.
f.write(f"The largest value recorded for Sepal Length was {x} the smallest value recorded was {x1} from the {x2} samples.\n")
f.write(f"The largest value recorded for Sepal width was {y} the smallest value recorded was {y1} from the {x2} samples.\n")
f.write(f"The largest value recorded for Petal Length was {z} the smallest value recorded was {z1} from the {x2} samples.\n")
f.write(f"The largest value recorded for Petal Length was {w} the smallest value recorded was {w1} from the {x2} samples.\n")
f.write(f" By analysing the Histogram and Scatter plots prodcued by running the program it is possible ")
f.close() #close Summary.txt

#[7]
sepallenght = (df["sepallength"])
plt.hist(sepallenght, bins= 13, color = "red") #plts the Histogram 
plt.title("Recorded Sepal length")
plt.xlabel("Sepal Length")
plt.ylabel("No. of times value is recorded")
plt.savefig('Sepal Length.png')
plt.show()# displays Histograms .

sepalwidth = (df["sepalwidth"])
plt.hist(sepalwidth, bins= 13, color = "blue") #plts the Histogram 
plt.title("Recorded Sepal Width in CM")
plt.xlabel("Sepal Width")
plt.ylabel("No. of times value is recorded")
plt.savefig('Sepal Width.png')
plt.show()# displays Histograms

petallength = (df["petallength"])
plt.hist(petallength, bins= 13, color = "orange") #plts the Histogram 
plt.title("Recorded Petal length")
plt.xlabel("Petal Length")
plt.ylabel("No. of times value is recorded")
plt.savefig('Petal Length.png')
plt.show()# displays Histograms


petalwidth = (df["petalwidth"])
plt.hist(petalwidth, bins= 13, color = "green") #plts the Histogram 
plt.title("Recorded Petal Width")
plt.xlabel("Petal Width")
plt.ylabel("No. of times value is recorded")
plt.savefig('Petal Width.png')
plt.show()# displays Histograms

#[4]
plt.scatter(df["sepallength"], df["sepalwidth"]) #plots two variables to a scatter plot
plt.title("Sepal length vs Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show() #Displays Scatter Plot

plt.scatter(df["petallength"],df["petalwidth"])#plots two variables to a scatter plot
plt.title("Petal length vs Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show() #Displays Scatter Plot

