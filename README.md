# BINOM.DIST.RANGE function
This function reproduces the BINOM.DIST.RANGE function in Microsoft Excel using Python.  
Source:[https://support.microsoft.com/en-us/office/binom-dist-range-function-17331329-74c7-4053-bb4c-6653a7421595](https://support.microsoft.com/en-us/office/binom-dist-range-function-17331329-74c7-4053-bb4c-6653a7421595)
```python
from scipy.stats import binom

def binom_dist_range(Trials, Probability_s, Number_s, Number_s2=None):
    if Number_s2 is None:
        return binom.pmf(Number_s, Trials, Probability_s)
    else:
        return sum(binom.pmf(x, Trials, Probability_s) for x in range(Number_s, Number_s2 + 1))
```

## Description
Returns the probability of a trial result using a binomial distribution.

## Syntax
binom_dist_range(trials, probability_s, number_s, [number_s2])  
The binom_dist_range function syntax has the following arguments.

- **Trials**<br>
  Required. The number of independent trials. Must be greater than or equal to 0.

- **Probability_s**<br>
  Required. The probability of success in each trial. Must be greater than or equal to 0 and less than or equal to 1.

- **Number_s**<br>
  Required. The number of successes in trials. Must be greater than or equal to 0 and less than or equal to Trials.

- **Number_s2**<br>
  Optional. If provided, returns the probability that the number of successful trials will fall between Number_s and number_s2. Must be greater than or equal to Number_s and less than or equal to Trials.

## Remarks
- The following equation is used:<br>
  $$\sum_{k=S}^{S2} \binom{N}{k} p^k (1-p)^{N-k}$$
  
- In the equation above, N is Trials, p is Probability_s, s is Number_s, s2 is Number_s2, and k is the iteration variable.

## Example
| Formula  | Description | Result |
| - | - | - |
| binom_dist_range(60, 0.75, 48) | Returns the binomial distribution based on the probability of 48 successes in 60 trials and a 75% probability of success (0.084, or 8.4%). | 0.083975 |  
| binom_dist_range(60, 0.75, 45, 50) | Returns the binomial distribution based on the probability of between 45 and 50 successes (inclusive) in 60 trials and a 75% probability of success (0.524, or 52.4%). | 0.523630 |
