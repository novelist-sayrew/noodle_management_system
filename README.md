# 1.アプリ名
*noodle_management_system*
<hr>

# 2.概要
登録したカップ麺の賞味期限を、一覧で確認することができるアプリです。
<hr>

# 3.使用例

(写真)<br>
▲登録したカップ麺の一覧画面では、あと何日で期限が切れるかを確認することができます。<br>
　残り期限が5日以内のものは黄色の文字、期限が過ぎたものは赤色の文字で表示されます。
 
(写真)<br>
▲賞味期限が切れた商品は、ページの最上部に一覧で表示されます。

(写真)<br>
▲期限が近いもののみを即座に確認できるように、別のページに一覧で表示されるようにしています。
<hr>

# 4.アプリの機能一覧
### ●外部機能一覧<br>
・ユーザー情報(ユーザー名・メールアドレス・パスワード)の登録・ログイン機能。<br>
・セッション管理によるログイン状態の保持機能。<br>
・トークン方式によるパスワードの再設定機能。<br>
・商品名・商品情報(賞味期限)の追加・閲覧・編集・削除機能。<br>
<hr>

### ●内部機能一覧
・Flask-Loginによる認証管理機能。<br>
・Werkzeugによるパスワードのハッシュ化機能。<br>
・パスワード再発行トークンの生成と、トークンの制限時間を管理する機能。<br>
・APSchedulerによる、期限切れトークンの自動削除機能。<br>
・Flask-WTFによるCSRF対策。<br>
・.envによる環境変数の管理。<br>
・author・noodleの機能ごとによるBlueprintの分離。<br>
・SQLAlchemyORMによる、SQLiteデータベースの管理。<br>
<hr>

# 5.使用した技術一覧
### ●言語・フレームワーク
・Python 3.x<br>
・Flask<br>
→Webのフレームワークとして使用。
<hr>

### ●ライブラリ・拡張機能
・Flask-Login<br>
→ユーザー認証・セッション管理機能として使用。<br>

・Flask-WTF<br>
→フォーム処理の管理機能・CSRF対策として使用。<br>

・Jinja2<br>
→テンプレートエンジンとして使用。<br>

・Werkzeug<br>
→パスワードをハッシュ化する機能として使用。<br>
<hr>

### ●データベース・ORM
・SQLite<br>
・SQLAlchemy ORM<br>
→モデルの管理・クエリ処理として使用。<br>
<hr>

### ●バックグランド処理
・APScheduler<br>
→期限切れトークンの自動削除機能として使用。<br>
<hr>

### ●環境管理・設定
・Python-dotenv<br>
→.envによる環境変数管理機能として使用。<br>

・config.py<br>
→設定ファイルとして使用。<br>

・SECRET_KEY<br>
<hr>

### ●その他の構造・設計
・Blueprint<br>
・create_app方式によるアプリの起動。<br>
・アプリケーションコンテキスト。<br>
<hr>

# 6.ファイル構造<br>
```
*noodle_management_system*
│
│
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
├── config.py
├── run.py
├── .env
└── .gitignore
```
<hr>

# 7.設計の工夫<br>
### 1.賞味期限が近い・または期限が切れた商品の視認性の高さ<br>
 それぞれの商品の賞味期限までの日数を、6日以上のものは黒色・5日～当日までのものを黄色・期限が切れたものを赤色の文字で表示されるようにしました。
また、商品名一覧のページにおいて、賞味期限が近い順番に商品名が並ぶようにしました。
<hr>

### 2.商品の状態ごとにおけるランク分け



 <hr>

