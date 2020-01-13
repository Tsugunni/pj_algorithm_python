#  jupyter_notebookフォルダのローカルでの動かし方

## 0.jupyter_notebook環境で仮想環境の作成
> cd jupyter_notebook

> virtualenv .venv

.venv という仮想環境を作成(ローカルが汚れない)

> source .venv/bin/activate

.venv/　というフォルダがある階層で実行
*source .venv/bin/activate は MacOS環境*
(.venv)という環境が確認できたらok

## 1.ローカル環境へのJupyter Notebook環境インストール
このコマンドで実行に必要なライブラリをインストールします
> pip install -r requirements.txt
*このコマンドで `requirements.txt` に記載のライブラリをインストールします*

## 2.Jupyter Notebookの起動
> $ jupyter notebook
でローカルでjupyter notebookが実行される

## 3.Jupyter Notebookで対象ファイルを選択し実行

> jupyter_notebook/contents/.

以下に.ipynbというjupyter notebookで実行できるファイルがある
<<<<<<< HEAD
 
## 4.Jupyter Notebookの仮想環境から抜ける

> deactivate
=======
>>>>>>> 8036296aa11374ede7fc2cd647f443aa3484dfa3
