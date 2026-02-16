import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rfm = pd.read_csv(r"Python\rfmdata.csv")

avg_value_per_segment = rfm.groupby('segment', as_index=False)['monetary'].mean()
avg_value_per_segment.rename(columns={'monetary': 'Average_Monetary'}, inplace=True)

plt.figure(figsize=(8,4))
plt.scatter(avg_value_per_segment['segment'], avg_value_per_segment['Average_Monetary'], color='lightblue')
plt.title('Average Monetary Value by Customer Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Average Monetary Value')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()