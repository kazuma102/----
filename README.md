# ネトプロ最終課題

## サーバーに関して

### ローカルでの起動手順
・コマンドにて、server.pyを起動する  
    -> python server.py
・POST、GETリクエストの内容はターミナルで確認

### Dockerを使った起動
・tarファイルからイメージを取り込む

    -> docker load -i netpro-score-app 
・イメージを実行する(今回は8080ポート)

    -> docker run -p 8080:8080 netpro-score-app

### Renderへのアクセスをする場合
・そのままゲームを起動して大丈夫  
※スコアボードになかなか反映されない可能性があります(Renderの仕様上)  
    __→その場合はローカル(またはDocker)での実行をして、「Unity/Assets/Scripts/Web/JsonToServer」の14,15行目のアドレス部分をlocalhostに変更してください__

## ゲームプレイに関して

### Unityバージョンに関して
使用バージョン：Unity2021.3.8f1

### 起動手順
・サーバーを起動する  
・exeファイルを起動してゲームプレイ！

### 操作方法
・UI操作

    画面表示の通りX、Zキーを使用します。  
・ゲームプレイ

    移動：WASD  
    エイム：マウスカーソル  
    ショット：左クリック