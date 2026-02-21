import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rfm = pd.read_csv(r"Python\rfmdata.csv")
at_risk_high = rfm[(rfm['segment'] == 'At Risk') & (rfm['monetary'] > 3000)]

bins = np.arange(3000,23000,1000)

counts,bin_edges = np.histogram(at_risk_high['monetary'],bins=20)
percentage = counts / counts.sum() * 100

print("Bin Edges:", bin_edges)
print("Counts:", counts)
print("Percentage:", percentage)

bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

plt.figure(figsize=(7,4))
bars = plt.bar(bin_centers, counts, width=800, color = 'cyan', edgecolor='black')

plt.title('High-value At Risk customers: spend distribution')
plt.xlabel('Total Revenue(Monetary)')
plt.ylabel('Number of Customers')
plt.xticks(bin_edges, rotation=45)

for bar, count, pct in zip(bars, counts, percentage):
    if count > 0:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f'({pct:.1f}%)',
            ha='center',
            va='bottom',
            fontsize=8
        )

plt.tight_layout()
plt.show()