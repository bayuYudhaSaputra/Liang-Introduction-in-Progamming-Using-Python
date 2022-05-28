# ===============================================
# Hitung Luas Area 4 Kota
# ===============================================

import math
# 1. Tentukan titik koordinat dan radius bumi:
latAtlanta = math.radians(33.75393329550227) # Latitude Atlanta diubah ke radian
longAtlanta = math.radians(-84.38765761114344) # Longitude Atlanta diubah ke radian

latOrlando = math.radians(28.539025723774394) # Latitude Orlando diubah ke radian
longOrlando = math.radians(-81.40173011581405) # Longitude Orlando diubah ke radian

latSavannah = math.radians(32.08237582514256) # Latitude Savannah diubah ke radian
longSavannah = math.radians(-81.09756761997859) # Longitude Savannah diubah ke radian

latCharlotte = math.radians(35.29255216599908) # Latitude Charlotte diubah ke radian
longCharlotte = math.radians(-80.85086495981042) # Longitude Charlotte diubah ke radian

radiusBumi = 6371.01

# 2. Tentukan jarak :
# 2a. Atlanta - Orlando
jarakAtlantaOrlando = radiusBumi * math.acos(math.sin(latAtlanta) * math.sin(latOrlando) + math.cos(latAtlanta) * math.cos(latOrlando) * math.cos(longOrlando - longAtlanta))

# 2b. Orlando - Savannah
jarakOrlandoSavannah = radiusBumi * math.acos(math.sin(latOrlando) * math.sin(latSavannah) + math.cos(latOrlando) * math.cos(latSavannah) * math.cos(longSavannah - longOrlando))

# 2c. Savannah - Atlanta
jarakSavannahAtlanta = radiusBumi * math.acos(math.sin(latSavannah) * math.sin(latAtlanta) + math.cos(latSavannah) * math.cos(latAtlanta) * math.cos(longAtlanta - longSavannah))

# 3. Hitung luas area Atlanta-Savannah-Orlando
jumlahS1 = (jarakAtlantaOrlando + jarakOrlandoSavannah + jarakSavannahAtlanta) / 2

luas1 = math.sqrt(jumlahS1 * (jumlahS1 - jarakAtlantaOrlando) * (jumlahS1 - jarakOrlandoSavannah) * (jumlahS1 - jarakSavannahAtlanta))

# 4. Tentukan jarak antara :
# 4a. Atlanta - Charlotte
jarakAtlantaCharlotte = radiusBumi * math.acos(math.sin(latAtlanta) * math.sin(latCharlotte) + math.cos(latAtlanta) * math.cos(latCharlotte) * math.cos(longCharlotte - longAtlanta))

# 4b. Savannah - Charlotte
jarakSavannahCharlotte = radiusBumi * math.acos(math.sin(latSavannah) * math.sin(latCharlotte) + math.cos(latSavannah) * math.cos(latCharlotte) * math.cos(longCharlotte - longSavannah))

# 5. Hitung luas Atlanta-Savannah-Charlotte
jumlahS2 = (jarakSavannahAtlanta + jarakAtlantaCharlotte + jarakSavannahCharlotte) / 2

luas2 = math.sqrt(jumlahS2 * (jumlahS2 - jarakSavannahAtlanta) * (jumlahS2 - jarakAtlantaCharlotte) * (jumlahS2 - jarakSavannahCharlotte))

# 6. Hitung jumlah luas
luasArea = round(luas1 + luas2, 2)

# 7. Tampilkan luas area
print(
        "Luas area yang dibatasi oleh kota: Atlanta, Savannah, Charlotte, dan Orlando adalah : \n",
        luasArea,
        "Km2"
)
