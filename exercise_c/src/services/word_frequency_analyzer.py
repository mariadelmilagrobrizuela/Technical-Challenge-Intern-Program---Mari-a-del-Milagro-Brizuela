import re


def analyze_word_frequency(file_path):
    frequencies = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.lower()
            
            line = re.sub(r'[^a-záéíóúüñ\s]', " ", line)

            words = line.split()

            for word in words:
                frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies