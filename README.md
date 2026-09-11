# 1.アプリ名
**noodle_management_system**
<hr>

# 2.概要
登録したカップ麺の賞味期限を、一覧で確認することができるアプリです。<br>
プログラミングの勉強用に作成しました。<br>
<hr>

# 3.使用例

(画像)<br>
**---色分けの一覧---**<br>
・期限が6日以上 …… 黒<br>
・期限が5日以内 …… 黄<br>
・期限切れ …… 赤<br>
<br>
商品一覧画面では、賞味期限が近い順に商品名が並びます。<br>
また、賞味期限が切れた商品は、ページの最上部にまとめて表示されます。<br>

(画像)<br>
▲賞味期限が5日以内の商品は、別のページに一覧で表示されます。<br>
<br>
※画像は全てイメージです。実際のものとは異なる場合があります。
<hr>

# 4.アプリの機能一覧
・ユーザー情報の登録・ログイン。<br>
・セッション管理によるログイン状態の保持。<br>
・パスワード再設定機能(トークン方式)。<br>
・商品情報(商品名・賞味期限)の追加・編集・削除。<br>
・賞味期限の自動計算・日数による色分け表示。<br>
・期限が近い商品の専用ページによる表示。<br>
<hr>

# 5.使用した技術一覧
### ●言語・フレームワーク
・Python 3.x<br>
・Flask<br>
<hr>

### ●ライブラリ・拡張機能
・Flask-Login<br>
・Flask-WTF<br>
・Jinja2<br>
・Werkzeug<br>
<hr>

### ●データベース・ORM
・SQLite<br>
・SQLAlchemy ORM<br>
<hr>

### ●バックグランド処理
・APScheduler<br>
<hr>

### ●環境管理・設定
・Python-dotenv<br>
・config.py<br>
・SECRET_KEY<br>
<hr>

### ●その他の構造・設計
・Blueprint<br>
・create_app方式によるアプリの起動。<br>
・アプリケーションコンテキスト。<br>
<hr>

# 6.ファイル構造
```
noodle_management_system
│
├──app
│    ├── forms.py
│    ├── models.py
│    ├── scheduler.py
│    ├── utils.py
│    ├── __init__.py
│    │
│    ├──auth
│    │    ├── routes.py
│    │    ├── __init__.py
│    │    │
│    │    └─templates
│    │  　     └─auth
│    │  　         ├── forgot_password.html
│    │  　         ├── login.html
│    │  　         ├── register.html
│    │  　         └── reset_password.html
│    │
│    └───noodle
│         ├── routes.py
│         ├── __init__.py
│         │
│         └─templates
│       　     └─noodle
│       　         ├── base.html
│       　         ├── form.html
│       　         ├── list.html
│       　         └── warning.html
│
├── Procfile
├── requirements.txt
├── config.py
├── run.py
├── .env
└── .gitignore
```
<hr>

# 7.設計の工夫
・賞味期限を色分けしたことによる視認性の向上。<br>
・期限が近い商品のみをまとめた専用ページ。<br>
・ユーザーの動線に沿ったUI設計。<br>
・年・月・日による賞味期限の管理。<br>
<hr>

# 8.閲覧者がアプリを起動できるようにするためのセットアップ<br>
### 推奨環境<br>
・Python3.10～3.12<br>
・Ubuntu(Linax)<br>
・Gitのホームページ<br>
<hr>

### 実装手順<br>
1.リポジトリをcloneする。<br>
2.仮想環境を作成し、有効化する。<br>
3. .envファイルを作成し、SECRET_KEY・DATABASE_URLなどを設定。<br>
4.必要なパッケージのインストール。<br>
5.DBの初期化。<br>
6.アプリを起動する。<br>
<hr>

# 9.デプロイ(試作品)が掲載されたサイトのURL
現在準備中です。<br>
<hr>

# 10.製作者情報
●製作者 : 藤井 雄也<br>
●役割 : アプリ全般の制作。<br>
●目的 : プログラミングの勉強のため。
