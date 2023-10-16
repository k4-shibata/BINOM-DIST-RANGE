# BINOM.DIST.RANGE関数
この関数はMicrosoft ExcelのBINOM.DIST.RANGE関数をpythonで再現した物です。  
参照元：[https://support.microsoft.com/ja-jp/office/binom-dist-range-%E9%96%A2%E6%95%B0-17331329-74c7-4053-bb4c-6653a7421595](https://support.microsoft.com/ja-jp/office/binom-dist-range-%E9%96%A2%E6%95%B0-17331329-74c7-4053-bb4c-6653a7421595)
```python
from scipy.stats import binom

def binom_dist_range(Trials, Probability_s, Number_s, Number_s2=None):
    if Number_s2 is None:
        return binom.pmf(Number_s, Trials, Probability_s)
    else:
        return sum(binom.pmf(x, Trials, Probability_s) for x in range(Number_s, Number_s2 + 1))
```

## 説明
二項分布を使用した試行結果の確率を返します。

## 構文
binom_dist_range(試行回数, 確率_s, 数値_s, [数値_s2])  
binom_dist_range関数の構文には次の引数があります。

- **試行回数**<br>
  必須。独立した試行の回数。0以上である必要があります。

- **確率**<br>
  必須。各試行での成功確率。0以上1以下である必要があります。

- **数値**<br>
  必須。試行での成功回数。0以上Trials以下である必要があります。

- **数値**<br>
  オプション。指定した場合、成功した試行の回数がNumber_sとnumber_s2の間に収まる確率が返されます。Number_s以上Trials以下である必要があります。

## 解説
- 次の方程式が使用されます：
  $$\sum_{k=S}^{S2} \binom{N}{k} p^k (1-p)^{N-k}$$
  
- 上記の方程式では、N は試行回数、p は成功率、s は成功数、s2 は 成功数 2、および k は繰り返し変数を表します。

## 使用例
| 数式  | 説明 | 結果 |
| - | - | - |
| binom_dist_range(60, 0.75, 48) | 60 回の試行のうち 48 回成功する確率と 75% の成功確率をベースとする二項分布 (0.084 つまり 8.4%) を返します。 | 0.083975 |  
| binom_dist_range(60, 0.75, 45, 50) | 60 回の試行のうち 45 ～ 50 回成功する確率と 75% の成功確率をベースとする二項分布 (0.524 つまり 52.4%) を返します。 | 0.523630 |
