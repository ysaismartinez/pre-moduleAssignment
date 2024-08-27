#cli.py
import pandas as pd
import numpy as np


def main():
    print("my_cli_hw is running")
    theData = pd.read_csv("tips.csv")
    print(theData)
    print(theData.describe())

if __name__ == "__main__":
    main()


