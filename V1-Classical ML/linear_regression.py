import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import os

# dataset = pd.read_csv('spam.csv')

#----------LOAD DATASET------------#

dataset_path = '../spam.csv'

if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"The dataset path '{dataset_path}' does not exist")


try:
    dataset = pd.read_csv(dataset_path)
except Exception as e:
    print(f"There's been an error {e} while reading the dataset at '{dataset_path}' ")




#----------VALIDATE DATASET------------#

required_columns = {'v1', 'v2'}
if not required_columns.issubset(dataset.columns):
    raise ValueError(f"The dataset must contain the following columns: {required_columns}") 