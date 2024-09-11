name = "Birender Kumar"

vol_count = 0
volwel = 'aeiouAEIOU'
vol_letter = []
for letter in name:
    if letter in volwel:
        vol_letter.append(letter)
        vol_count += 1

print(vol_count)
print(vol_letter)
