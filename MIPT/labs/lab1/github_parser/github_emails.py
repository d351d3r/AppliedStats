# -*- coding: utf-8 -*-
"""GitHub_emails.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MPUjrdGJ1PJ1b6ir6RfLD8cTnXXWdTzA
"""

from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from zlib import crc32

with open("sem8.html") as f:
    soup = BeautifulSoup(f, "html.parser")
f.close()

email_list = []
for block in soup.body.main.find_all(
    "a", {"class": "js-navigation-open Link--primary"}
):
    email_list.append(block.get("title").rstrip(".csv"))

email_list = list(filter(lambda x: len(x) > 1, email_list))

dataframe = pd.DataFrame()

for mail in email_list:
    seed = crc32(mail.strip().encode("utf-8")) % (2 ** 32 - 1)
    rs = np.random.RandomState(seed)
    tasks = []
    for i in range(3):
        tasks.append(rs.randint(low=1, high=5))
    tasks.append(rs.randint(low=1, high=4))
    tasks.append(rs.randint(low=1, high=3))
    tasks.append(rs.randint(low=1, high=3))
    dataframe[mail] = tasks

dataframe = dataframe.T
dataframe.columns = np.arange(1, 7)

dataframe = pd.get_dummies(dataframe, columns=dataframe.columns)

dataframe.to_csv("res.csv")
