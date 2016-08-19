# ソートアルゴリズムと行列演算

今回の目標はPython慣れすることと、機械学習に向けて行列演算の方法を学ぶことです。

ソートアルゴリズムはあらためて実装するまでもなく、最近の言語処理系では既にソートするための関数が組み込まれています。

しかし考え方を学ぶ・言語に慣れるという点ではとても有意義なことなので、今回はそれをやります。

また行列演算ですが、こちらはそれに特化したライブラリを利用します。

行列演算の関数を独自に実装するのも面白いですが、それだけではどうしても計算の速度差が出てしまうので、専門の方々が築き上げたものを活用しましょう。

これはPythonに限らずC++などでも同じことが言えます。

以下にミッションを示します。

3まで出来て合格とします。合格した人は強いです。

頑張れば霊長類最強にも勝てるんじゃないでしょうか。

1. [1,14,51,4,1,9,19,8,10,8,9,3] という中身の配列(リスト)を作成し、sortメソッドで昇順に並び替えよ。
2. クイックソートまたはバブルソートを実装し、1の結果と比較せよ。

    ```
    def quicksort(alist):
		# hogehoge
		return sorted
	def bubblesort(alist);
		# hogehoge
		return sorted
    ```
3. 行列演算ライブラリNumpyを読み込み、3x3の単位行列を作れ。

    ```
	# pip install numpy        numpyをインストール
    ```

    ```
    import numpy as np        # numpy を np として読み込む
    ```
4. Numpyを読み込み、x + y * z を計算せよ。

    ```
    x = [[2.0, 4.2],
         [3.3, 5.7]]
    y = [[3.5, 0.9],
         [7.2, 1.2]]
    z = [[1.0, 0.0],
         [0.0, 1.0]]
    ```

解答例は後で示すので、とりあえず自由に作ってみましょう。

ミッション以外に「俺の書いた自慢のプログラムを見てくれないか……？」という場合にもどんどん提出してください。

提出する場合にはプルリクエストでお願いします。

何か分からないことがあれば[Issues](https://github.com/PBL-2016/prepare/issues/)へ。