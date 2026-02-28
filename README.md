# vscode-mryl

<p align="left">
  <img src="assets/icon_512x512.png" width="200" alt="Mryl"/>
</p>

# これはなに？
[Mryl 言語](https://github.com/Mryl-Dev/Mryl) を VSCode で開発するうえで  
必要なシンタックス強調、タグジャンプ、エラー解析といった拡張機能を提供します。

# 開発環境
* Windows 11 Pro 25H2
* Node.js: v18.x 以上（最新の LTS 推奨）
* npm: v9.x 以上
* Python: 3.x（Language Server の実行に必要
* Visual Studio Code: 最新版
* VSCode 拡張機能:
  * ESLint (コード品質管理)
  * TypeScript Nightly (推奨)

# セットアップ方法
* リポジトリをクローンした後、以下の手順で開発を開始できます。
    1. 依存ライブラリのインストール  
        ターミナルでプロジェクトのルートディレクトリに移動し、ライブラリをインストールします。
        ```
        npm install
        ```
    2. 開発用ビルドと監視 (Watch モード)
        コードの変更を自動的に検知してビルドするために、以下のコマンドを実行します。
        ```
        npm run watch
        ```
    3. デバッグの開始
        VSCode で F5 キー を押します。
        新しい VSCode ウィンドウ（拡張機能開発ホスト）が立ち上がります。  
        .ml ファイルを開くと、シンタックスハイライトと LSP（Language Server）が動作します。
    4. パッケージの作成 (.vsix)  
        拡張機能として配布可能なパッケージを作成するには、以下のコマンドを使用します。
        ```
        # vsce が未インストールの場合は: npm install -g @vscode/vsce
        vsce package --no-verify --allow-missing-repository
        ```
# ライセンス
* MIT License
