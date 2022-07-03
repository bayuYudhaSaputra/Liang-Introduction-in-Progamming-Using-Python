# ===================================
# Mengurutkan bilangan
# ===================================

bil1, bil2, bil3 = eval(input("Input tiga bilangan bulat yang berbeda:"))

if bil1 < bil2 < bil3:
    print("Urutan bilangan mulai dari yang terkecil hingga terbesar adalah :",
    bil1, ", ", bil2, ", ", bil3
    )
elif bil2 < bil3 < bil1:
    print("Urutan bilangan mulai dari yang terkecil hingga terbesar adalah :",
    bil2, ", ", bil3, ", ", bil1
    )
elif bil3 < bil1 < bil2:
    print("Urutan bilangan mulai dari yang terkecil hingga terbesar adalah :",
    bil3, ", ", bil1, ", ", bil2
    )
elif bil1 < bil3 < bil2:
    print("Urutan bilangan mulai dari yang terkecil hingga terbesar adalah :",
    bil1, ", ", bil3, ", ", bil2
    )
elif bil3 < bil2 < bil1:
    print("Urutan bilangan mulai dari yang terkecil hingga terbesar adalah :",
    bil3, ", ", bil2, ", ", bil1
    )
elif bil2 < bil1 < bil3:
    print("Urutan bilangan mulai dari yang terkecil hingga terbesar adalah :",
    bil2, ", ", bil1, ", ", bil3
    )
else:
    print("Maaf, anda tidak menginput 3 bilangan bulat berbeda!")