# absolutely-stop-aws-instances
AWSのインスタンス絶対に止めるマン

## 対応しているサービス
- EC2
- RDS

## 通知のサンプル
Slackに通知される

![image](https://user-images.githubusercontent.com/8668892/138576878-e619a535-8578-4fc5-a0c4-00455cad8dfc.png)

## Setup
セットアップ方法を記す

### 1. SSMパラメータストアの登録
serverless.ymlに記載のキーでSSMパラメータストアに登録する

### 2. デプロイ
#### 2-1. venv
```bash
$ python -m venv myvenv
$ source ./myvenv/bin/activate
```

#### 2-2. 必要なパッケージの取得
```bash
$ make pip_install
```

#### 2-3. Serverless Frameworkのインストール
```bash
## node v14.17.0以上
$ npm install -g serverless
$ npm install --save serverless-python-requirements
$ npm install --save serverless-prune-plugin
```

#### 2-4. デプロイの実行
Dockerが必要。デプロイしたいAWSアカウントに切り替えてから実行すること
```bash
make deploy
```
