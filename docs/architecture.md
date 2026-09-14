# 内部設計説明書<br>
<br>

## 1. 概要<br>
このページは、noodle_management_systemにおける内部設計や処理内容における詳細な情報をまとめた資料です。<br>
READMEで簡略化して記載した内容を、ここでは詳細に説明します。<br>
<br>

## 2. 外部機能における内部処理<br>
### 2-1. ユーザー情報の登録・ログイン<br>
・Flask-Loginによる認証管理<br>
・user_loader によるユーザー情報の読み込み<br>
・Werkzeugによるパスワードのハッシュ化<br>
・Flask-WTFによるCSRFの保護<br>

### 2-2. パスワード再設定機能（トークン方式）<br>
・secretsによるトークンの生成<br>
・datetimeによる有効期限（30分）の管理<br>
・APSchedulerによる期限が切れたトークンの自動削除(1時間ごと)<br>

### 2-3. 商品情報に関するCRUD処理<br>
・SQLAlchemy ORMによるDB操作<br>
・登録された賞味期限の自動計算<br>
・期限別による文字色の色分け処理（黒・黄・赤）<br>
・期限が近い順による自動ソート処理<br>
<br>

## 3. 内部機能<br>
### 3-1. 認証処理（Flask-Login）<br>
・LoginManagerの初期化<br>
・login_requiredの動作<br>
・セッション管理<br>

### 3-2. 賞味期限計算ロジック<br>
・datetime.dateによる日付管理<br>
・(賞味期限 - 今日) の差分計算による、期限までの日数の自動算出<br>

### 色分け条件<br>
・6日以上：黒<br>
・5日以内：黄<br>
・期限切れ：赤<br>

### 3-3. APSchedulerのジョブ設計<br>
・intervalジョブ（1時間ごとに一回）<br>
・Flaskコンテキストを使ったDBアクセス<br>
・トークン削除処理<br>
<br>

## 4. その他の構造・設計<br>
### 4-1. Blueprint構成<br>
●auth(認証機能)<br>
・forgot_passwordページによるパスワード再設定メールの送信<br>
・loginページによるユーザーのログイン認証<br>
・registerによるユーザー情報の登録<br>
・reset_passwordによる再設定されたユーザー情報の登録<br>

●noodle(商品管理機能)<br>
・formページによるエラーの表示<br>
・listページによる期限ごとに文字色を変えた表示<br>
・warningページによる賞味期限が近い商品の分離<br>

### 4-2. create_app()パターン<br>
・create_app()パターンによるアプリ初期化の流れ<br>
・拡張機能の登録（LoginManager、SQLAlchemy、APSchedulerなど）<br>
・Blueprintの登録<br>

### 4-3. データベース設計<br>
●Userモデル<br>
・id<br>
・username<br> 
・email<br>
・password_hash<br>

●Noodleモデル<br>
・id<br>
・name<br>
・year、month、day<br>  
・リレーション無し（全ユーザーで同じデータを共有するため）<br>

## 5. 今後の展望・改善点<br>
・同時編集によるデータ整合性の問題<br>
・商品バーコード読み取り機能の実装など利便性の向上<br>
・編集履歴・削除履歴の実装<br>

