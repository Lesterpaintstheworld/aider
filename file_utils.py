 
def safe_read_files(fnames):
    for fname in fnames:
        try:
            with open(fname, "r", encoding="utf-8") as f:
                content = f.read()
            yield fname, content
        except Exception as e:
            print(f"Error reading {fname}: {e}")
            yield fname, None
