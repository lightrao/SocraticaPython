oceans = ["Pacifc", "Atlantic", "Indian", "Southern", "Arctic"]

with open(r"26_TextFilesinPython\text_files\oceans2.txt", "w") as f:
    for ocean in oceans:
        print(ocean, file=f)

with open(r"26_TextFilesinPython\text_files\oceans2.txt", "a") as f:
    print(23*"=", file=f)
    print("These are the 5 oceans.", file=f)

