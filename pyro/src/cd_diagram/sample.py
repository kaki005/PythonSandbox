import pandas as pd

from .cd_diagram import draw_cd_diagram

df_perf = pd.read_csv('example.csv', index_col=False)
draw_cd_diagram(df_perf=df_perf, title='Accuracy', labels=True)
