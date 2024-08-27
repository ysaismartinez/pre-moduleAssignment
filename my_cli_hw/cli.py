# cli.py
#Import required libraries
import pandas as pd
import numpy as np

#Define a main method
def main():
    theData = pd.read_csv("tips.csv") #This loads a CSV file tips.csv which I added to the project folder.
    print(theData) #Then I print the contents of my CSV
    print(theData.describe()) #And I print the output of the describe() function. 

if __name__ == "__main__":
    main()


