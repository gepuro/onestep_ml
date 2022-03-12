# ビルド方法

```
PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.9.7
pyenv local 3.9.7
pip install poetry
poetry install
poetry run python -m eel main.py web --onefile --noconsole --hidden-import=sklearn.utils._weight_vector --hidden-import=sklearn.utils._weight_vector --hidden-import=sklearn.utils._typedefs
```

# ビルドしたファイルの実行

```
./dist/main
```

# 開発時の実行

```
poetry run python main.py
```
