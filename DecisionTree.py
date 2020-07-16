import numpy as np
import pandas as pd
df = pd.read_excel("MS- train (MS).xlsx")
test = pd.read_excel("MS-test (MS).xlsx")
df.head()
test.head()
from chefboost import Chefboost as chef
config = {'algorithm': 'CHAID'}
model = chef.fit(df, config)

dogru=0
yanlis=0
for index,instance in test.iterrows():
    prediction = chef.predict(model,instance)
    actual = instance['Decision']
    if prediction==actual:
        dogru=dogru+1
    else:
        yanlis=yanlis+1

print("Dogru: ",dogru," Yanlış: ",yanlis)
