import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Compute the Kullback-Leibler divergence
def KL_divergence(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))

# Create two normal distributions
x = np.linspace(-10, 10, 1000)
p = norm.pdf(x, 0, 2)
q = norm.pdf(x, 2, 2)

# Calculate the Kullback-Leibler divergence
kl_div = KL_divergence(p, q)

# Plot the distributions and the KL divergence
plt.figure(figsize=(10, 6))
plt.plot(x, p, label='p: N(0, 2)')
plt.plot(x, q, label='q: N(2, 2)')
plt.fill_between(x, p, alpha=0.5)
plt.fill_between(x, q, alpha=0.5)
plt.title(f'Kullback-Leibler Divergence: {kl_div:.4f}')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.show()