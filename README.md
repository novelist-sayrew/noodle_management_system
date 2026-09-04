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
## ●外部機能一覧<br>
・ユーザー情報(ユーザー名・メールアドレス・パスワード)の登録・ログイン機能。<br>
・セッション管理によるログイン状態の保持機能。<br>
・トークン方式によるパスワードの再設定機能。<br>
・商品名・商品情報(賞味期限)の追加・閲覧・編集・削除機能。<br>
<hr>

## ●内部機能一覧
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
## ●言語・フレームワーク
・Python 3.x<br>
・Flask<br>
→Webのフレームワークとして使用。

## ●ライブラリ・拡張機能
・Flask-Login<br>
→ユーザー認証・セッション管理機能として使用。<br>

・Flask-WTF<br>
→フォーム処理の管理機能・CSRF対策として使用。<br>

・Jinja2<br>
→テンプレートエンジンとして使用。<br>

・Werkzeug<br>
→パスワードをハッシュ化する機能として使用。<br>

## ●データベース・ORM
・SQLite<br>
・SQLAlchemy ORM<br>
→モデルの管理・クエリ処理として使用。<br>

## ●バックグランド処理
・APScheduler<br>
→期限切れトークンの自動削除機能として使用。<br>

## ●環境管理・設定
・Python-dotenv<br>
→.envによる環境変数管理機能として使用。<br>

・config.py<br>
→設定ファイルとして使用。<br>

・SECRET_KEY<br>

## ●その他の構造・設計
・Blueprint<br>
・create_app方式によるアプリの起動。<br>
・アプリケーションコンテキスト。<br>
<hr>

# 6.ファイル構造<br>
*noodle_management_system* <br>
│ <br>
│ <br>
│ <br>
├───app <br>
│ 　  ├───  forms.py <br>
│ 　  ├───  models.py <br>
│ 　  ├───  scheduler.py <br>
│ 　  ├───  utils.py <br>
│ 　  ├───  __init__.py <br>
│ 　  ├─── <br>
　  ├─auth <br>
　  │  │  routes.py <br>
　  │  │  __init__.py <br>
　  │  │ <br>
　  │  └─templates <br>
　  │  　  └─auth <br>
　  │  　          forgot_password.html <br>
　  │  　          login.html <br>
　  │  　          register.html <br>
　  │  　          reset_password.html <br>
　  │ <br>
　  └─noodle <br>
　  　  │  routes.py <br>
　  　  │  __init__.py <br>
　  　  │ <br>
　  　  └─templates <br>
　  　  　  └─noodle <br>
　  　  　          base.html <br>
　  　  　          form.html <br>
　  　  　          list.html <br>
　  　  　          warning.html <br>

├──  config.py <br>
├──  run.py <br>
├──  .env <br>
└──  .gitignore <br>

