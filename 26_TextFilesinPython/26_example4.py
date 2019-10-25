oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open(r"26_TextFilesinPython\text_files\ocean.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")