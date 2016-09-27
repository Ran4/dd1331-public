
def num2binary(n):
    if n <= 1:
        return [n]
    else:
        return num2binary(n // 2) + [n%2]

print(num2binary(1))
print(num2binary(2))
print(num2binary(3))
print(num2binary(4))
