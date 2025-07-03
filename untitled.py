import numpy as np
import pandas as pd
import matplotib.pyplot as pl
import seaborn as sb
df = pd.read_csv("all_recs.csv", encoding = "unicode_escape")
df.head()