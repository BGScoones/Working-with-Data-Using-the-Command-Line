import read

data = read.load_data()

from collections import Counter

def most_common(number, words):
    n_most_common = Counter(words.split(" ")).most_common(number)
    return(n_most_common)

if __name__ == "__main__":
    headlines = data["headline"].str.cat(sep = " ").lower()
    hundred_most_common = most_common(100, headlines)
    print(hundred_most_common)