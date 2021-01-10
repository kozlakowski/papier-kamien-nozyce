import pyperclip

f = open("temp.txt", "r")
content = f.read().split("\n\n")

for i in range(len(content)):
    pyperclip.copy(content[i])
    print(content[i])
    input()

print("KONIEC")
