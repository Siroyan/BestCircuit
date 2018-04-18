# BestCircuit
主にユニバーサル基板を用いた配線作業をするときに、
最も効率のよい部品配置,配線を教えてくれるソフトです。

## 開発経緯
私自身が大学のサークルや趣味として電子回路を組むことがあり、
その際に「**最も効率の良い部品配置,配線はどれか**」
ということに悩まされていたからです。  
回路設計ソフトの[Eagle](https://www.autodesk.co.jp/products/eagle/overview)
にも自動配線機能が付いているのですが、それはあくまで **配線** だけの話で、
**部品の配置** まではやってくれません。
(おそらく実務では部品の配置までコンピューターに投げてしまう、ということは無いからでしょうか)  
趣味の範囲で、ユニバーサル基板等で回路を組むときには、部品の配置まで効率化されてくれるとありがたいのです。  
そこで開発に踏み切りました。

## 今できること
一点から一点への最短経路候補を算出し、任意のコストによって評価できる。

##次の課題
現在一般的に利用されているアルゴリズム(迷路法,線形探索法etc...)について学習し、実際にプログラムを動かしてみる。

##最終目標
ニューラルネットワークと遺伝的アルゴリズムを用いることで、配置配線問題の最適解を見つける。
