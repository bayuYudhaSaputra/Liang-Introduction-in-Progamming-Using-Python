# ============================================
# Mengacak Kartu
# ============================================

import random

# Generate rank
indeksRank = random.randint(1, 13)

if indeksRank == 1:
    rank = "Ace"
elif indeksRank == 2:
    rank = "2"
elif indeksRank == 3:
    rank = "3"
elif indeksRank == 4:
    rank = "4"
elif indeksRank == 5:
    rank = "5"
elif indeksRank == 6:
    rank = "6"
elif indeksRank == 7:
    rank = "7"
elif indeksRank == 8:
    rank = "8"
elif indeksRank == 9:
    rank = "9"
elif indeksRank == 10:
    rank = "10"
elif indeksRank == 11:
    rank = "Jack"
elif indeksRank == 12:
    rank = "Queen"
elif indeksRank == 13:
    rank = "King"

# Generate Clubs, diamonds, hearts, spades
indeksSuit = random.randint(1,4)

if indeksSuit == 1:
    suit = "Clubs"
elif indeksSuit == 2:
    suit = "Diamonds"
elif indeksSuit == 3:
    suit = "Hearts"
elif indeksSuit == 4:
    suit = "Spades"

print("---------------------------------------- \n",
    "The card you picked is the", rank, "of", suit, "\n"
    "------------------------------------------ "
    )