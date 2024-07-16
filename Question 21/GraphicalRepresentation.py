import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Generate data for different types of skewness
np.random.seed(0)
data_symmetrical = np.random.normal(loc=0, scale=1, size=1000)
data_positive_skew = np.random.exponential(scale=1, size=1000)
data_negative_skew = -np.random.exponential(scale=1, size=1000)

# Create subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Symmetrical distribution
sns.histplot(data_symmetrical, kde=True, ax=axes[0], color='blue')
axes[0].set_title('Symmetrical Distribution')
axes[0].set_xlim(-4, 4)

# Positively skewed distribution
sns.histplot(data_positive_skew, kde=True, ax=axes[1], color='green')
axes[1].set_title('Positively Skewed Distribution')
axes[1].set_xlim(0, 8)

# Negatively skewed distribution
sns.histplot(data_negative_skew, kde=True, ax=axes[2], color='red')
axes[2].set_title('Negatively Skewed Distribution')
axes[2].set_xlim(-8, 0)

# Show plots
plt.tight_layout()
plt.show()
