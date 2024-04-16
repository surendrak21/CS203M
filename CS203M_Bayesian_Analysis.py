import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta as beta_dist

# Observations
data = ['H', 'H', 'H', 'T', 'T', 'T', 'H', 'H', 'H', 'T']
num_heads = sum(1 for outcome in data if outcome == 'H')
num_tails = len(data) - num_heads

# Priors
priors = [(2, 5), (5, 2), (1, 1), (2, 2)]

# Calculate MLE and MAP estimates
MLE = num_heads / (num_heads + num_tails)

# Plot posterior distributions for each case
x = np.linspace(0, 1, 1000)

for i, (alpha_prior, beta_prior) in enumerate(priors):
    alpha_posterior = alpha_prior + num_heads
    beta_posterior = beta_prior + num_tails
    
    MAP = (alpha_posterior - 1) / (alpha_posterior + beta_posterior - 2)
    
    posterior = beta_dist.pdf(x, alpha_posterior, beta_posterior)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, posterior, label=f'Beta({alpha_posterior}, {beta_posterior})')
    plt.axvline(x=MLE, color='k', linestyle='--', label='MLE')
    plt.axvline(x=MAP, color='r', linestyle='--', label='MAP')
    
    plt.title(f'Posterior Distribution for Beta({alpha_prior}, {beta_prior}) Prior')
    plt.xlabel('Probability of Heads')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)
    plt.ylim(0, 10)  
    plt.show()
