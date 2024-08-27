#cli.py
import pandas as pd
import numpy as np

def main():
    theData = pd.read_csv("tips.csv")
    print(theData)
    print(theData.describe())

if __name__ == "__main__":
    main()


