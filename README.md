# skill-sheets-analysis
指定したkeywordに該当するスキルシートを抽出する。

<br>

# Requirement
以下の環境で動作確認済み<br>
- [docker-develop-for-python](https://github.com/NaoyaOgura0828/docker-develop-for-python)で構築したPython3.12環境

<br>

# Installation
1. git cloneコマンドで本Repositoryを任意のディレクトリ配下にcloneする。
2. 下記のコマンドでパッケージをInstallする。

    ```bash
    pip install -r requirements.txt
    ```

<br>

# Settings


1. [skill_sheets_analysis.py](./skill_sheets_analysis.py)内の下記のリストに抽出対象のkeywordを指定する。

    ```python
    keywords = ['tensorflow', 'sklearn', 'xgboost', 'lightgbm', 'keras', 'mxnet', 'nltk', 'spacy', 'transformers', 'pandas', 'numpy', 'matplotlib', 'seaborn', 'pyplot', 'pytorch']
    ```

2. [skill_sheets_analysis.py](./skill_sheets_analysis.py)と同じ階層に`skill_sheets/`というディレクトリを作成する。

    ```bash
    mkdir skill_sheets
    ```

3. [skill_sheets/](./skill_sheets/)に検索対象のスキルシートを格納する。

    ```
    skill_sheets/
    |-- skill_sheet_A
    |-- skill_sheet_B
    `-- skill_sheet_C
    ```

> [!IMPORTANT]
> スキルシートは、`.xlsx`または`.xls`形式のみをサポートする。

<br>

# Usage
下記のコマンドを実行する。

```bash
python3.12 skill_sheets_analysis.py
```

> [!TIP]
> 実行環境のpythonコマンドのPATH設定によって、実行コマンドは適宜変更する。
> ```bash
> # e.g.
> python skill_sheets_analysis.py
> python3 skill_sheets_analysis.py
> ```

<br>
