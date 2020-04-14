***PandS-Project2020*** <br>
***Jack Caffrey***
=================

### Introduction 

Project was completed as part of the Programming and Scripting module. <br>
In order to complete the project the following was required:

1. **Researching** the Fisher's Iris Data Set (Summary will be included in this README).<br>
2. Downloading the Data Set and including it in the **Repository**.<br>
3. Writing a program call **analysis.py**. This program outputs:<br>
    * A summary of each of the variables to a text file.<br>
    * Saves a histogram of each variable to png files.<br>
    * Outputs a scatter plot of each pair of varaiables.<br>

***Fisher's Iris Data Set***
============================

The Fisher Iris Data set was first introduced by biologist *Ronald Fisher* in his 1936 paper " *The use of multiple measurments in taxonomic problems* ". The data set comprises of 150 records captured under 5 attributes for three related species of ***Iris Flower***. These attributes include: <br>
1. Petal Length. <br>
2. Petal Width. <br>
3. Sepal Length. <br>
4. Sepal Width. <br>
5. Class (Species) <br>
These records were then used to quantify the morphologic variation between 1. *Iris Setose*, 2. *Iris Virginica* and 3. *Iris Versicolour* Flowers.<br> 
The data set is also known as *Anderson's Iris* data set, because the data used in the data set was captured by Edgar Anderson. [2]

***Aim of the Fisher Iris Data Set***
=====================================

The aim of the Data set is to categorize and model the class memebership, of the 3 species of Iris flowers from length and width recorded measurments of Sepals and Petals of each of the flowers.<br>
It is also widely acknowledged as the best known example in the field of machine learning. [3]

***Program Operation***
=======================
* Open CMDER and navigate to the file location using the commands (e.g. cd \desktop\PandS-Project2020) .<br>
* Enter ***python analysis.py*** and click return (Enter) to run program. 

***Program Output***
====================
* Program imports the various libraries required using the import function. These libraries are already available from python.<br>
* The Fisher Iris Data Set (saved in CSV formatt) is then read into the program using the ***df = pd.read_csv("iris_csv.csv")*** this file is used in the creation of the Summary.txt, Histograms and Scatter Plots.<br>
* Max and minimum values are defined to assist in the analysis of the data set in the creation of the ***Summary.txt*** file.<br>
* Program opens the ***Summary.txt*** and writes (w), the summary of the analysis of each of the variables to this txt file.<br>
* f.close () closes the ***Summary.txt file***.
* Histogram of each of the variables is saved in PNG formatt in the file directory.<br>
* Scatter plots for the different variables are then created and displayed as the program is run. <br>

* The following outputs are automatically created when the program is run: <br>
1. A summary of the Fisher Iris Data Set, the operation of the program, the expected program outputs, approach taking to complete the project and the references used when creating the program in the ***README***.
2. Anaylsis of the Data Set in the form ***Summary.txt***.
3. ***Histogram*** of each of the variables saved in ***PNG formatt***.
4. ***Scatter*** plots of each pairs of variables variables. 

#### Project Approach 
* Reviewed project requirments as indentified by the problem statment.<br>
* Created github repository and cloned to PC. <br>
* Committed Initial commit to ensure repository was set up correctly. <br>
* Researched formatting of README files - *MARKDOWN* <br>
* Edited README files and comitted various test commits to verify formatting. <br>
* Researched *Fishers Iris Data Set*. <br>
* Committed introduction of Summary to README. <br>
* Committed Summary to README and various formatting updates. <br>
* Added *Project Summary* notes & Inital test of program. <br>
* Researched writing to txt files in python and included in analysis.py program. <br>
* Researched creating and saving Histograms as PNG files in python and included in analysis.py program.<br>
* Created scatter plot for inital pair of variables.<br>
* All References used in the creation of this program are idenified below or in the code as [#]. <br>
* Reviewed the project before the final commit for submission. 
* Github was used to save all commits while carrying out the project


### References 
---------------
1. Formatting [Basic Syntax] (https://www.markdownguide.org/basic-syntax/ "Guide for Markdown").
2. [Iris Flower Dataset] (https://www.kaggle.com/arshid/iris-flower-dataset).
3. Machine Learning Examples [Neural designer] (https://www.neuraldesigner.com/learning/examples/iris-flowers-classification).

### Program References
----------------------
4. Programming and Scripting Lecture notes.
5. Extract values from a CSV file [Stackover flow] (2020) (https://stackoverflow.com/questions/48920014/how-to-extract-the-min-value-and-max-value-from-csv-file-using-python)
6. Outputting functions to a text file python [ Quora ] (2020) (https://www.quora.com/How-do-I-write-the-output-of-a-function-to-a-text-file-in-python)
7. Saving images as PNG files [Stackover flow] (2020) (https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib).
 

