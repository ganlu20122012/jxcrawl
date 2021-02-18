<p class="has-line-data" data-line-start="0" data-line-end="1">QQ交流群：1001030977</p>
<p class="has-line-data" data-line-start="2" data-line-end="6">包名：jxcrawl<br>
本项目用 python （3.X）编写，专注于获取公开（股市行情）数据。<br>
安装方法：<br>
pip install jxcrawl</p>
<p class="has-line-data" data-line-start="7" data-line-end="8">申明：</p>
<ol>
<li class="has-line-data" data-line-start="8" data-line-end="10">
<p class="has-line-data" data-line-start="8" data-line-end="9">调用本包中的接口，将直接从公开网站拿公开数据.</p>
</li>
<li class="has-line-data" data-line-start="10" data-line-end="13">
<p class="has-line-data" data-line-start="10" data-line-end="12">本包作者不对数据的真实性，准确性，时效性等负责，本包接口返回的数据都是来自公开网站的公开数据。<br>
调用者调用本包接口返回数据用于决策、计算等等，引发的自身经济损失或法律问题由使用者自己承担，和本包作者无关。</p>
</li>
<li class="has-line-data" data-line-start="13" data-line-end="15">
<p class="has-line-data" data-line-start="13" data-line-end="14">本包仅用于学习研究，禁止用来向各接口所指向的网站发起攻击或频繁调用使其不堪重负或瘫痪。</p>
</li>
</ol>
<h1 class="code-line" data-line-start=15 data-line-end=16 ><a id="_15"></a>-------------------------------------------------------------</h1>
<p class="has-line-data" data-line-start="16" data-line-end="17">一些示例：</p>
<ol>
<li class="has-line-data" data-line-start="18" data-line-end="54">获取指定股票的实时行情数据<br>
code_arr=[‘300101’,‘600570’]      # 振芯科技，恒生电子<br>
df = jxcrawl.get_realtime_stock_data(code_arr)<br>
返回结果：<br>
0            1<br>
date          2021-02-10   2021-02-10<br>
time            16:30:00     15:00:00<br>
code              300101       600570<br>
name                振芯科技         恒生电子<br>
last_close         15.49       105.65<br>
open               15.58          105<br>
high               15.91       107.68<br>
low                15.38       104.66<br>
price              15.55       106.35<br>
volume          15198089     12258164<br>
amount       2.37153e+08  1.30375e+09<br>
ask5_price         15.59       106.39<br>
ask5_volume        25719         1300<br>
ask4_price         15.58       106.38<br>
ask4_volume         3500          700<br>
ask3_price         15.57       106.37<br>
ask3_volume        32400        12000<br>
ask2_price         15.56       106.36<br>
ask2_volume        12300         2720<br>
ask1_price         15.55       106.35<br>
ask1_volume        13400        26604<br>
bid1_price         15.54       106.34<br>
bid1_volume        41800          100<br>
bid2_price         15.53        106.3<br>
bid2_volume        22900        70300<br>
bid3_price         15.52       106.29<br>
bid3_volume        60100         2000<br>
bid4_price         15.51       106.28<br>
bid4_volume        28700          100<br>
bid5_price          15.5       106.27<br>
bid5_volume        27700          400</li>
</ol>
<h1 class="code-line" data-line-start=58 data-line-end=59 ><a id="_58"></a>-----------------------------------------------------</h1>
<ol start="2">
<li class="has-line-data" data-line-start="59" data-line-end="63">获取 K 线数据<br>
code = ‘600570’     # 恒生电子<br>
df = jxcrawl.get_k_data(code=code,xbegin=‘2021-01-01’,xend=‘2021-02-01’)</li>
</ol>
<p class="has-line-data" data-line-start="63" data-line-end="64">返回结果：</p>
<pre><code>      date    code  name  last_close    open    high     low    volume  \
</code></pre>
<p class="has-line-data" data-line-start="66" data-line-end="87">0   2021-01-04  600570  恒生电子      104.90  105.93  107.47  104.20  13887713<br>
1   2021-01-05  600570  恒生电子      106.17  105.53  110.59  105.30  15178699<br>
2   2021-01-06  600570  恒生电子      109.61  108.88  109.64  102.01  27879182<br>
3   2021-01-07  600570  恒生电子      103.19  103.20  103.88   95.60  41259844<br>
4   2021-01-08  600570  恒生电子       98.16   98.27  100.05   96.25  24074709<br>
5   2021-01-11  600570  恒生电子       99.51   99.40  100.45   96.58  18952299<br>
6   2021-01-12  600570  恒生电子       97.07   96.81  101.99   95.80  21403949<br>
7   2021-01-13  600570  恒生电子      101.00  101.00  101.00   94.40  30610517<br>
8   2021-01-14  600570  恒生电子       95.00   94.97   98.25   94.00  16740989<br>
9   2021-01-15  600570  恒生电子       95.80   97.00   98.30   93.63  15541642<br>
10  2021-01-18  600570  恒生电子       95.59   95.18   98.05   94.28  18087109<br>
11  2021-01-19  600570  恒生电子       97.00   96.81   99.85   96.11  15583208<br>
12  2021-01-20  600570  恒生电子       97.50   97.60   99.89   95.83  15003459<br>
13  2021-01-21  600570  恒生电子       98.80   99.00  102.38   97.26  20427748<br>
14  2021-01-22  600570  恒生电子      101.99  101.02  102.88   99.50  16446325<br>
15  2021-01-25  600570  恒生电子       99.78   98.98   99.10   95.79  22354686<br>
16  2021-01-26  600570  恒生电子       95.86   95.86   96.99   93.30  17032364<br>
17  2021-01-27  600570  恒生电子       93.40   93.40   96.50   92.60  14596683<br>
18  2021-01-28  600570  恒生电子       95.66   94.40   96.72   94.12  10379933<br>
19  2021-01-29  600570  恒生电子       94.31   95.69  100.80   95.50  21239085<br>
20  2021-02-01  600570  恒生电子       97.13   98.66  103.24   98.18  25870685</p>
<pre><code>      amount   close  change   percent  turnover   total_value  \
</code></pre>
<p class="has-line-data" data-line-start="89" data-line-end="110">0   1.476688e+09  106.17    1.27  0.012107  0.013301  1.108511e+11<br>
1   1.656565e+09  109.61    3.44  0.032401  0.014538  1.144428e+11<br>
2   2.913842e+09  103.19   -6.42 -0.058571  0.026702  1.077397e+11<br>
3   4.073575e+09   98.16   -5.03 -0.048745  0.039517  1.024879e+11<br>
4   2.372454e+09   99.51    1.35  0.013753  0.023058  1.038975e+11<br>
5   1.864093e+09   97.07   -2.44 -0.024520  0.018152  1.013499e+11<br>
6   2.121028e+09  101.00    3.93  0.040486  0.020500  1.054532e+11<br>
7   2.960531e+09   95.00   -6.00 -0.059406  0.029318  9.918862e+10<br>
8   1.621028e+09   95.80    0.80  0.008421  0.016034  1.000239e+11<br>
9   1.492514e+09   95.59   -0.21 -0.002192  0.014885  9.980464e+10<br>
10  1.749226e+09   97.00    1.41  0.014750  0.017323  1.012768e+11<br>
11  1.523824e+09   97.50    0.50  0.005155  0.014925  1.017988e+11<br>
12  1.467657e+09   98.80    1.30  0.013333  0.014370  1.031562e+11<br>
13  2.050068e+09  101.99    3.19  0.032287  0.019565  1.064868e+11<br>
14  1.658852e+09   99.78   -2.21 -0.021669  0.015752  1.041794e+11<br>
15  2.166331e+09   95.86   -3.92 -0.039286  0.021411  1.000865e+11<br>
16  1.614122e+09   93.40   -2.46 -0.025662  0.016313  9.751808e+10<br>
17  1.383675e+09   95.66    2.26  0.024197  0.013980  9.987772e+10<br>
18  9.900192e+08   94.31   -1.35 -0.014112  0.009942  9.846820e+10<br>
19  2.086305e+09   97.13    2.82  0.029901  0.020342  1.014125e+11<br>
20  2.628212e+09  103.21    6.08  0.062597  0.024778  1.077606e+11</p>
<pre><code>circulation_value
</code></pre>
<p class="has-line-data" data-line-start="112" data-line-end="133">0        1.108511e+11<br>
1        1.144428e+11<br>
2        1.077397e+11<br>
3        1.024879e+11<br>
4        1.038975e+11<br>
5        1.013499e+11<br>
6        1.054532e+11<br>
7        9.918862e+10<br>
8        1.000239e+11<br>
9        9.980464e+10<br>
10       1.012768e+11<br>
11       1.017988e+11<br>
12       1.031562e+11<br>
13       1.064868e+11<br>
14       1.041794e+11<br>
15       1.000865e+11<br>
16       9.751808e+10<br>
17       9.987772e+10<br>
18       9.846820e+10<br>
19       1.014125e+11<br>
20       1.077606e+11</p>
<h1 class="code-line" data-line-start=135 data-line-end=136 ><a id="_135"></a>--------------------------------------</h1>
<ol start="3">
<li class="has-line-data" data-line-start="136" data-line-end="138">获取主力散户资金流进流出额</li>
</ol>
<p class="has-line-data" data-line-start="138" data-line-end="140">code = ‘600570’<br>
df = jxcrawl.get_stock_fund_flow(code=code)</p>
<p class="has-line-data" data-line-start="141" data-line-end="153">返回结果：<br>
0<br>
date                20210210<br>
code                sh600570<br>
name                    恒生电子<br>
main_in          6.60679e+08<br>
main_out         6.25079e+08<br>
main_net_in         3.56e+07<br>
personal_in       6.4307e+08<br>
personal_out     6.78669e+08<br>
personal_net_in  -3.5599e+07<br>
total_fund_in    1.30375e+09</p>
<h1 class="code-line" data-line-start=154 data-line-end=155 ><a id="_154"></a>=======================================</h1>
<p class="has-line-data" data-line-start="155" data-line-end="156">QQ交流群：1001030977</p>
