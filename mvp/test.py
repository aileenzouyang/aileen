import pandas as pd
import json
df = pd.read_csv("cars.csv")
  
# parsing the DataFrame in json format.
json_records = df.reset_index().to_json(orient ='records')
data = []
data = json.loads(json_records)
context = {'d': data}
  