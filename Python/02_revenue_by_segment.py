import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rfm = pd.read_csv(r"Python\rfmdata.csv")

revenue_by_segment = rfm.groupby('segment', as_index=False)['monetary'].sum()
revenue_by_segment.rename(columns={'monetary': 'Total_Revenue'}, inplace=True)
revenue_by_segment_percentage = revenue_by_segment['Total_Revenue'] / revenue_by_segment['Total_Revenue'].sum() * 100

plt.figure(figsize=(8,4))
bars = plt.bar(revenue_by_segment['segment'], revenue_by_segment['Total_Revenue'], color='lightblue', edgecolor='black')
for bar,pct in zip(bars, revenue_by_segment_percentage):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{pct:.1f}%',
        ha='center',
        va='bottom',
        fontsize=8
    )

plt.title('Total Revenue by Customer Segment')
plt.xlabel('Customer Segment')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()