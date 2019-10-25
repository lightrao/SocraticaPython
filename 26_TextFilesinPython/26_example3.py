try:
    with open("future_lottery_numbers.txt") as f:
        text = f.read()
except FileNotFoundError:
    text = None

print(text)

try:
    with open(r"26_TextFilesinPython\text_files\guidao_bio.txt") as f:
        text = f.read()
except FileNotFoundError:
    text = None

print(text)