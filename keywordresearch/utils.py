import pandas as pd
import os
from typing import TextIO

def read_file(file_io):
    file_name = file_io.name
    _, ext = os.path.splitext(file_name)
    df = None
    if ext == '.xlsx':
        df = pd.read_excel(file_name)  
    elif ext == '.csv':
        df = pd.read_csv(file_name)  
    else:
        print("We don't accept that file type")
    return df



