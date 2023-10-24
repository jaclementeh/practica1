import pandas as pd
from utils import empty_file
from config import *


def extract_data():

    df1 = pd.read_parquet(path_parquet_file_1, engine='auto')
    empty_file(path_parquet_file_1)

    df2 = pd.read_parquet(path_parquet_file_2, engine='auto')
    empty_file(path_parquet_file_2)

    df3 = pd.read_parquet(path_parquet_file_3, engine='auto')
    empty_file(path_parquet_file_3)

    return df1, df2, df3


