from scipy.stats import binom

def binom_dist_range(Trials, Probability_s, Number_s, Number_s2=None):
    if Number_s2 is None:
        return binom.pmf(Number_s, Trials, Probability_s)
    else:
        return sum(binom.pmf(x, Trials, Probability_s) for x in range(Number_s, Number_s2 + 1))

# 例として Trials=10, Probability_s=0.5, Number_s=3 を使います
# Using the example with Trials=10, Probability_s=0.5, and Number_s=3.
Trials = 10
Probability_s = 0.5
Number_s = 3
Number_s2 = 7

probability = binom_dist_range(Trials, Probability_s, Number_s, Number_s2)
print(f"The probability is approximately {probability:.6f}")