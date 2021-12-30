# 概要
アップロードされた犬あるいは猫の画像から、犬であるか猫であるかを判定するWebアプリケーション

# 実装の方針
ImageNetで重み付けされたVGG16を用いて、犬と猫のデータセットを学習。  
生成したモデルをapp.py内で読み込み、Flaskを用いてWebアプリケーションを構築した。

# アプリケーションの実行結果
・猫の画像をアップロード  
<img width="317" alt="スクリーンショット 2021-12-30 230237" src="https://user-images.githubusercontent.com/62968285/147758775-663e6593-a4d4-4c65-9e58-ab8271aabff3.png">  
  
・犬の画像をアップロード  
<img width="367" alt="image" src="https://user-images.githubusercontent.com/62968285/147760396-30653e49-2d14-45ef-ac23-325d05ab17ab.png">

