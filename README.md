包名：jxcrawl
本项目用 python （3.X）编写，专注于获取公开（股市行情）数据。
安装方法： 
pip install jxcrawl

申明：
1. 调用本包中的接口，将直接从公开网站拿公开数据.

2. 本包作者不对数据的真实性，准确性，时效性等负责，本包接口返回的数据都是来自公开网站的公开数据。
	调用者调用本包接口返回数据用于决策、计算等等，引发的自身经济损失或法律问题由使用者自己承担，和本包作者无关。

3. 本包仅用于学习研究，禁止用来向各接口所指向的网站发起攻击或频繁调用使其不堪重负或瘫痪。

# -------------------------------------------------------------
一些示例：

1. 获取指定股票的实时行情数据
code_arr=['300101','600570']      # 振芯科技，恒生电子
df = jxcrawl.get_realtime_stock_data(code_arr)
返回结果（为了观看方便，这里转置后将列名显示在左侧，原数据 df 未转置。）：
                       0            1
date          2021-02-10   2021-02-10
time            16:30:00     15:00:00
code              300101       600570
name                振芯科技         恒生电子
last_close         15.49       105.65
open               15.58          105
high               15.91       107.68
low                15.38       104.66
price              15.55       106.35
volume          15198089     12258164
amount       2.37153e+08  1.30375e+09
ask5_price         15.59       106.39
ask5_volume        25719         1300
ask4_price         15.58       106.38
ask4_volume         3500          700
ask3_price         15.57       106.37
ask3_volume        32400        12000
ask2_price         15.56       106.36
ask2_volume        12300         2720
ask1_price         15.55       106.35
ask1_volume        13400        26604
bid1_price         15.54       106.34
bid1_volume        41800          100
bid2_price         15.53        106.3
bid2_volume        22900        70300
bid3_price         15.52       106.29
bid3_volume        60100         2000
bid4_price         15.51       106.28
bid4_volume        28700          100
bid5_price          15.5       106.27
bid5_volume        27700          400




# -----------------------------------------------------
2. 获取 K 线数据
code = '600570'     # 恒生电子
df = jxcrawl.get_k_data(code=code,xbegin='2021-01-01',xend='2021-02-01')

返回结果：

          date    code  name  last_close    open    high     low    volume  \
0   2021-01-04  600570  恒生电子      104.90  105.93  107.47  104.20  13887713
1   2021-01-05  600570  恒生电子      106.17  105.53  110.59  105.30  15178699
2   2021-01-06  600570  恒生电子      109.61  108.88  109.64  102.01  27879182
3   2021-01-07  600570  恒生电子      103.19  103.20  103.88   95.60  41259844
4   2021-01-08  600570  恒生电子       98.16   98.27  100.05   96.25  24074709
5   2021-01-11  600570  恒生电子       99.51   99.40  100.45   96.58  18952299
6   2021-01-12  600570  恒生电子       97.07   96.81  101.99   95.80  21403949
7   2021-01-13  600570  恒生电子      101.00  101.00  101.00   94.40  30610517
8   2021-01-14  600570  恒生电子       95.00   94.97   98.25   94.00  16740989
9   2021-01-15  600570  恒生电子       95.80   97.00   98.30   93.63  15541642
10  2021-01-18  600570  恒生电子       95.59   95.18   98.05   94.28  18087109
11  2021-01-19  600570  恒生电子       97.00   96.81   99.85   96.11  15583208
12  2021-01-20  600570  恒生电子       97.50   97.60   99.89   95.83  15003459
13  2021-01-21  600570  恒生电子       98.80   99.00  102.38   97.26  20427748
14  2021-01-22  600570  恒生电子      101.99  101.02  102.88   99.50  16446325
15  2021-01-25  600570  恒生电子       99.78   98.98   99.10   95.79  22354686
16  2021-01-26  600570  恒生电子       95.86   95.86   96.99   93.30  17032364
17  2021-01-27  600570  恒生电子       93.40   93.40   96.50   92.60  14596683
18  2021-01-28  600570  恒生电子       95.66   94.40   96.72   94.12  10379933
19  2021-01-29  600570  恒生电子       94.31   95.69  100.80   95.50  21239085
20  2021-02-01  600570  恒生电子       97.13   98.66  103.24   98.18  25870685

          amount   close  change   percent  turnover   total_value  \
0   1.476688e+09  106.17    1.27  0.012107  0.013301  1.108511e+11
1   1.656565e+09  109.61    3.44  0.032401  0.014538  1.144428e+11
2   2.913842e+09  103.19   -6.42 -0.058571  0.026702  1.077397e+11
3   4.073575e+09   98.16   -5.03 -0.048745  0.039517  1.024879e+11
4   2.372454e+09   99.51    1.35  0.013753  0.023058  1.038975e+11
5   1.864093e+09   97.07   -2.44 -0.024520  0.018152  1.013499e+11
6   2.121028e+09  101.00    3.93  0.040486  0.020500  1.054532e+11
7   2.960531e+09   95.00   -6.00 -0.059406  0.029318  9.918862e+10
8   1.621028e+09   95.80    0.80  0.008421  0.016034  1.000239e+11
9   1.492514e+09   95.59   -0.21 -0.002192  0.014885  9.980464e+10
10  1.749226e+09   97.00    1.41  0.014750  0.017323  1.012768e+11
11  1.523824e+09   97.50    0.50  0.005155  0.014925  1.017988e+11
12  1.467657e+09   98.80    1.30  0.013333  0.014370  1.031562e+11
13  2.050068e+09  101.99    3.19  0.032287  0.019565  1.064868e+11
14  1.658852e+09   99.78   -2.21 -0.021669  0.015752  1.041794e+11
15  2.166331e+09   95.86   -3.92 -0.039286  0.021411  1.000865e+11
16  1.614122e+09   93.40   -2.46 -0.025662  0.016313  9.751808e+10
17  1.383675e+09   95.66    2.26  0.024197  0.013980  9.987772e+10
18  9.900192e+08   94.31   -1.35 -0.014112  0.009942  9.846820e+10
19  2.086305e+09   97.13    2.82  0.029901  0.020342  1.014125e+11
20  2.628212e+09  103.21    6.08  0.062597  0.024778  1.077606e+11

    circulation_value
0        1.108511e+11
1        1.144428e+11
2        1.077397e+11
3        1.024879e+11
4        1.038975e+11
5        1.013499e+11
6        1.054532e+11
7        9.918862e+10
8        1.000239e+11
9        9.980464e+10
10       1.012768e+11
11       1.017988e+11
12       1.031562e+11
13       1.064868e+11
14       1.041794e+11
15       1.000865e+11
16       9.751808e+10
17       9.987772e+10
18       9.846820e+10
19       1.014125e+11
20       1.077606e+11


# --------------------------------------
3. 获取主力散户资金流进流出额

code = '600570'
df = jxcrawl.get_stock_fund_flow(code=code)

返回结果：
                           0
date                20210210
code                sh600570
name                    恒生电子
main_in          6.60679e+08
main_out         6.25079e+08
main_net_in         3.56e+07
personal_in       6.4307e+08
personal_out     6.78669e+08
personal_net_in  -3.5599e+07
total_fund_in    1.30375e+09



