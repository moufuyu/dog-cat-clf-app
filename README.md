# 概要
アップロードされた犬あるいは猫の画像から、犬であるか猫であるかを判定するWebアプリケーション

# 実装の方針
ImageNetで重み付けされたVGG16を用いて、犬と猫のデータセットを学習（転移学習）。  
生成したモデルをapp.py内で読み込み、Flaskを用いてWebアプリケーションを構築した。

# 実行方法
python app.py でプログラムを実行し、以下の画像のように出力で指定されたアドレスにアクセスする。  
<img width="631" alt="image" src="https://user-images.githubusercontent.com/62968285/147832610-6eb0bdbd-558e-40c7-9382-e2ea7b93497f.png">  
  
そして、犬か猫の画像をアップロードすると、判定とともにその確率も提示される。

# アプリケーションの実行結果
・猫の画像をアップロード  

<img width="960" alt="image" src="https://user-images.githubusercontent.com/62968285/147834507-fe5e767b-d8f7-4f2e-83c2-2fabc274afbc.png">  
  
・犬の画像をアップロード  

<img width="959" alt="image" src="https://user-images.githubusercontent.com/62968285/147834548-11f704aa-0977-4cb0-9ace-a6290e4c96b4.png">

