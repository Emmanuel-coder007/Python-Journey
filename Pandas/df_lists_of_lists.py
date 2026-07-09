import pandas as pd

data = [
  ['Brooklyn', 'US', 2646000],
  ['Seoul', 'South Korea', 9411000],
  ['Barcelona', 'Spain', 1636000],
  ['Mexico City', 'Mexico', 9209944]
]

df = pd.DataFrame(data, columns=['city', 'country', 'population'])
print(df)