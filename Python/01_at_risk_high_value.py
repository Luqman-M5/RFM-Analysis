import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rfm = pd.read_csv(r"Python\rfmdata.csv")
at_risk_high = rfm[(rfm['segment'] == 'At Risk') & (rfm['monetary'] > 3000)]


counts,bin_edges = np.histogram(at_risk_high['monetary'],bins=20)
percentage = counts / counts.sum() * 100


print("Bin Edges:", bin_edges)
print("Counts:", counts)
print("Percentage:", percentage)

plt.figure(figsize=(6,4))
plt.hist(at_risk_high['monetary'],bins=20,color='cyan', edgecolor='black',linewidth=0.7)
plt.title('High-value At Risk customers: spend distribution')
plt.xlabel('Total Revenue(Monetary)')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()