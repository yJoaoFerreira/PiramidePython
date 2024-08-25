print(f"Coloque apenas números de 1 único digito, pois se não irá deformar a pirâmide.")
print("")

n = 5
for i in range (n):
    print((n-i-1)*" ", (str(n-i) + " ") * i + str(n-i))
