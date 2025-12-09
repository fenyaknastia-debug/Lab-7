n = float(input())
p = float(input())
m = float(input())

S = n * (1 + (p / 100) * m)

print("Вхідні дані:")
print(n)
print(p)
print(m)

print("Вихідні дані:")
print(f"{S:.2f}")