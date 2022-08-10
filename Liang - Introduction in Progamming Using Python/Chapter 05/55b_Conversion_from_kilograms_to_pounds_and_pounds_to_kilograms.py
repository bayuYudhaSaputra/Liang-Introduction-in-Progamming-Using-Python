kilogram1 = 1
pound2 = 1

print("======================================================")
print("||", "No.", "|",format("kilogram","8s"), "|", format("Pounds","8s"),
    "||", format("Pounds","8s"), "|", format("Kilogram","8s"), "||"
    )
print("------------------------------------------------------")
for i in range(1,200):
    pound1 = 2.2 * kilogram1
    kilogram2 = 0.45 * pound2
    print("||", format(i,"3d") ,"|", format(kilogram1, "8.3f"), "|", format(pound1,"8.3f"),
        "||", format(pound2,"8.3f"), "|", format(kilogram2,"8.3f"), "||"
        )
    kilogram1 += 1
    pound2 += 1

print("------------------------------------------------------")    