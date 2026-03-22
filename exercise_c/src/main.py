from services.word_frequency_analyzer import analyze_word_frequency


def main():
    file_path = "data/quijote.txt"

    frequencies = analyze_word_frequency(file_path)

    sorted_words = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    print("\nTop 10 most frequent words:")
    for i, (word, count) in enumerate(sorted_words[:10], start=1):
        print(f"{i}) {word}: {count}")

if __name__ == "__main__":
    main()