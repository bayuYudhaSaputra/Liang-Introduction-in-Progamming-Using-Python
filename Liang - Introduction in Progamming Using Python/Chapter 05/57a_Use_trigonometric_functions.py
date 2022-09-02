from cmath import cos
import math

print("\n===================================")
print("|", format("Degree", "5s"), "|", format("Sin","7s"), "|", format("Cos", "7s"), "|")
print("-----------------------------------\n")

for i in range(1,37):
    nilaiSin = format(math.sin(i * 10 * math.pi / 180),"7.4f")
    nilaiCos = format(math.cos(i * 10 * math.pi / 180),"7.4f")
    print("|", format(i * 10, "6d"), "|", nilaiSin, "|", nilaiCos, "|")
print("-----------------------------------\n")
    