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
&nbsp; 以下の1～6の手順に従い、アプリを起動してください。<br>
<hr>

### 推奨環境<br>
・Python3.10～3.12<br>
・Ubuntu(Linax)(Windowsユーザーの場合は、こちらのインストールをおすすめします)
・Gitのホームページ(本アプリのコードをコピーしたい場合、ログインが必要となります)<br>
<hr>

### 1.アプリをclone(コードを複製・コピーすること)する<br>
&nbsp; Ubuntuのターミナルに「git clone https://github.com/novelist-sayrew/noodle_management_system」 を入力し、アプリをcloneする。<br>
<hr>

### 2.仮想環境を有効化する<br>
&nbsp; 1.Ubuntuのターミナルに「cd ~/workspace/noodle_management_system」を入力し、カレントディレクトリをアプリのフォルダにする。<br>
&nbsp; 2.Ubuntuのターミナルに「python3 -m venv venv」を入力し、新しい仮想環境を作成する。<br>
&nbsp; 3.Ubuntuのターミナルに「source venv/bin/activate」を入力し、仮想環境を有効化する。<br>
<hr>

### 3.「.env」ファイルを作成する<br>
&nbsp; 本アプリを動かすためには、.envファイルの作成が必要不可欠となっております。
&nbsp; .envという名前のファイルをrun.pyやconfig.pyなどのファイルと同じ階層に作成し、下記の項目を作成してください。

SECRET_KEY = A<br>
MAIL_USERNAME = B<br>
MAIL_DEFAULT_SENDER = C<br>
MAIL_PASSWORD = D<br>
DATABASE_URL = E<br>
<hr>

#### 3-A.---SECRET_KEY<br>
&nbsp; Flaskがセッションを保護するために必要となる秘密鍵を設定します。<br>
&nbsp; Ubuntuのターミナルに python -c "import secrets; print(secrets.token_hex(32))" と入力すると、ランダムな英数字が混ざった64桁の文字列が出力されるため、そちらを入力してください。<br>

【例】SECRET_KEY = 92f3a8c4e1b9d0f7c2a1e4b8f9d3c7a2e1f0b9c4d7a8e3f1c2b4d6e8f0a1b3<br>
※実際にアプリで使っているものではありません。<br>
<hr>

#### 3-B.---MAIL_USERNAME<br>
&nbsp; アプリを使用する際に利用するメールアドレスを設定します。<br>

【例】MAIL_USERNAME = example@gmail.com<br>
<hr>

#### 3-C.---MAIL_DEFAULT_SENDER<br>
&nbsp; パスワード再設定メールを送る送信元となるメールアドレスを設定します。MAIL_USERNAMEに設定したメールアドレスと同じでも問題ありません。<br>

【例】MAIL_DEFAULT_SENDER = example@gmail.com<br>
<hr>

#### 3-D.---MAIL_PASSWORD<br>
&nbsp; メールアプリを利用するために使用するパスワードを設定します。<br>

・Gmail(Google) …… abcd efgh ijkl mnop などの、4桁の英字×4組の16字。<br>
・yahoo!メール …… ログイン時に設定したパスワード。 <br>
・Outlook(Microsoft) …… ログイン時に設定したパスワード。<br> 
・iCloud(Apple) …… abcd-efgh-ijkl-mn-op などの、ハイフンが入った4桁の英字×4組の16字。<br>
など。(メールアプリごとに仕様が異なります)<br>

【例】MAIL_PASSWORD = abcd efgh ijkl mnop<br>
<hr>

#### 3-E.---DATABASE_URL <br>
&nbsp; 使用するデータベースのURLを設定します。<br>
&nbsp; 本アプリではSQLiteを推奨しています。<br>

【例】DATABASE_URL = sqlite:///example.db<br>
<hr>

### 4.アプリを起動するために必要な機能(モジュール)をインストールする<br>
&nbsp; Ubuntuのターミナルに「pip install -r requirements.txt」を入力し、アプリを起動するために必要なモジュールをインストールする。<br>
&nbsp; requirements.txtは、アプリを動かすために必要な様々な機能を一括でインストールすることができるテキストファイルです。<br>
<hr>

### 5.データベースの初期化・実装<br>
&nbsp; 1.Ubuntuのターミナルに「flask db init」を入力する。<br>
&nbsp; 2.Ubuntuのターミナルに「flask db migrate -m "Initial migration"」を入力する。<br>
&nbsp; 3.Ubuntuのターミナルに「flask db upgrade」を入力する。<br>
<hr>

### 6.アプリの起動
&nbsp; Ubuntuのターミナルに「python run.py」を入力し、アプリを起動する。<br>
<br>
<P align="right">以上</P>
<hr>

# 9.デプロイ(試作品)が掲載されたサイトのURL
現在準備中です。<br>
<hr>

# 10.製作者情報
●製作者 : 藤井 雄也<br>
●役割 : アプリ全般の制作。<br>
●目的 : プログラミングの勉強のため。
