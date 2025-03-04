
invalid_files = ["aaa", "bbb", "ccc"]
if invalid_files:
    raise ValueError(f"許可されていないファイル形式が検出されました: {invalid_files}")
