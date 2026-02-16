import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rfm = pd.read_csv(r"Python\rfmdata.csv")

recency_vs_spend = rfm.groupby('segment', as_index=False).agg(Avg_recency=('recency_date', 'mean'), Avg_monetary=('monetary', 'mean'))

fig, ax1 = plt.subplots(figsize=(8,4))

# Spend line
ax1.plot(recency_vs_spend['segment'],
         recency_vs_spend['Avg_monetary'],
         marker='o', color='tab:blue', label='Avg Monetary')
ax1.set_ylabel('Average Spend', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Recency line on second axis
ax2 = ax1.twinx()
ax2.plot(recency_vs_spend['segment'],
         recency_vs_spend['Avg_recency'],
         marker='s', color='tab:red', label='Avg Recency')
ax2.set_ylabel('Average Recency (days)', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

plt.title('Recency vs Spend by Customer Segment')
plt.xticks(rotation=45, ha='right')
fig.tight_layout()
plt.show()