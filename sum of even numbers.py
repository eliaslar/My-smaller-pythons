# total = 0
# for number in range(1, 101):
#    total += number
# print(total)

target = int(input())
total = 0

x = range(2, target + 1, 2)
for n in x:
    if n%2 == 0:
        total += n
print(total)