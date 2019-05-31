def raindrops(number):
    sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    raindrops = ''.join([sounds[factor] for factor in sounds.keys() if number % factor == 0])
    return raindrops or str(number)