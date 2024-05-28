# cron: 5 4 * * * # see https://crontab.guru, this always needs to be the first line
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(df)