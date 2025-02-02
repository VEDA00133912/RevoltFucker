# RevoltFucker
pythonのRevoltで使えるスパムツールです

![image](https://user-images.githubusercontent.com/67917586/160219979-c99c5705-7ca1-4378-8890-4446d0f99d7d.png)
![image](https://user-images.githubusercontent.com/67917586/160219993-6a312099-a606-4653-a610-0b6ee60d1c30.png)

# Tokenの取得
- 開発者ツールのNetworkタブを開いてリロードします
- Fetch/XHRを選択します
- Nameがfetchのところを開いて一番下までスクロールします
- x-session-tokenの値がユーザーTokenです。
- Revolt用のアカウントGenがあったみたいですが消えてました
![image](https://github.com/user-attachments/assets/735ad96b-1c00-4d1b-9764-6ee1cca9beab)

# 注意点
- RevoltはAPI制限結構きついのであんまり火力はないです
- 利用規約に引っかかる可能性があります。自己責任で
- アカウントがオフライン状態だとspammerが動かなかったので一度オンラインにする処理を挟んでからしたほうがいいのかもしれない(めんどいからやってません)
- 元コードは3年前のものです
- 毎回新しいTokenが生成されるのか？
