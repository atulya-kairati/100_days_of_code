nato_list = "Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliet, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu".split(', ')

print([nato_list[ord(alphabet) - 65] for alphabet in input('Enter a word: ').upper() if 65 <= ord(alphabet) <= 90])
