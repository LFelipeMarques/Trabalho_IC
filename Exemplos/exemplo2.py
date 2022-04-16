#"parsing" de .txt := usa os espaços em branco como separadores
with open('teste.txt') as f:
    lines = f.read()
print(lines.split())
