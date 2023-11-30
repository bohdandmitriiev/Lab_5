with open("TEXT.txt", mode="rt") as file:
    text = file.read()

max_line_length = int(input("Введіть максимальну довжину рядка: "))

words = text.split()
lines = []
current_line = ""

for word in words:
    if len(current_line) + len(word) <= max_line_length:
        current_line += " " + word
    else:
        lines.append(current_line)
        current_line = word

lines.append(current_line)

formatted_text = "\n".join(lines)

with open("output.txt", mode="wt") as file:
    file.write(formatted_text)
