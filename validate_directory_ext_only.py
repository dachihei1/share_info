def validate_directory_xlsx_only(directory: str) -> None:
    """
    指定ディレクトリ内の全ファイルが.xlsx形式であることを検証
    
    Args:
        directory (str): 検証対象ディレクトリのパス
        
    Raises:
        InvalidFileExtensionError: 非.xlsxファイルが存在する場合
        FileNotFoundError: ディレクトリが存在しない場合
        NotADirectoryError: 指定パスがディレクトリでない場合
    """
    target_dir = Path(directory)

    if not target_dir.exists():
        raise FileNotFoundError(f"ディレクトリが存在しません: {directory}")
    if not target_dir.is_dir():
        raise NotADirectoryError(f"ディレクトリではありません: {directory}")

    invalid_files = []

    prohibited_ext = {".xls", ".xlsb", ".xlsm"}
    for entry in target_dir.iterdir():
        if entry.is_file() and entry.suffix.lower() in prohibited_ext:
            invalid_files.append(entry.name)

    if invalid_files:
        raise ValueError(f"許可されていないファイル形式が検出されました: {invalid_files}")