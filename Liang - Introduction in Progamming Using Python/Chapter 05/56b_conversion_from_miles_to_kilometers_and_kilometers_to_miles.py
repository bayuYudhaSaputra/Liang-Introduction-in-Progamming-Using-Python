kilometer1 = 1
mile2 = 20

print("===============================================================")
print("||", "No.", "|",format("Kilometer","10s"), "|", format("Miles","10s"),
    "| |", format("Miles","10s"), "|", format("Kilometers","10s"), "||"
    )
print("---------------------------------------------------------------")
for i in range(0,10):
    mile1 = 1.609 * kilometer1
    kilometer2 = 0.621 * mile2
    print("||", format(i,"3d") ,"|", format(kilometer1, "10.3f"), "|", format(mile1,"10.3f"),
        "| |", format(mile2,"10.3f"), "|", format(mile2,"10.3f"), "||"
        )
    kilometer1 += 1
    mile2 += 5
print("===============================================================")