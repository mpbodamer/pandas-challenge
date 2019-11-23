# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "gameData.csv"

# Read Purchasing File and store into Pandas data frame
purchaseData = pd.read_csv(file_to_load)

purchaseData.head()
