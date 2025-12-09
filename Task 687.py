def solve(n, m):
    # n – голови, m – лапи
    # x – курчата (2 лапи)
    # y – кролики (4 лапи)

    # y = (m - 2n) / 2
    if (m - 2 * n) % 2 != 0:
        return "NO SOLUTIONS!"

    y = (m - 2 * n) // 2
    x = n - y

    if x < 0 or y < 0:
        return "NO SOLUTIONS!"

    return f"{x} {y}"


print("Вхідні дані:")

data = []
while True:
    line = input().strip()
    if line == "":
        break
    n, m = map(int, line.split())
    data.append((n, m))

print("Вихідні дані:")
for n, m in data:
    print(solve(n, m))
