# Implement a function which search for the most common word in the file `data/lorem_ipsum.txt`
import re


def most_common_words(path: str, number_of_words=3) -> list:
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()
        lst = re.findall(r'[a-zA-Z]+', txt)
        counts = {}
        for word in lst:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

    list_of_words = sorted([(k, v) for k, v in counts.items()], key=lambda x: x[1], reverse=True)
    return list_of_words[0:number_of_words]


if __name__ == '__main__':
    filename = 'data/lorem_ipsum.txt'
    print(f"\nThe list with most common word(s) in {filename}: {most_common_words(filename)}")
