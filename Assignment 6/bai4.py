import re

def top5_word_proportion(text):
    # Normalize text and extract words
    words = re.findall(r'\b\w+\b', text.lower())

    # Count frequencies using a dictionary
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Sort words by frequency (descending)
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Get top 5
    top5 = dict(sorted_words[:5])

    total_words = len(words)
    top5_total = sum(top5.values())
    proportion = (top5_total / total_words) * 100

    print("Top 5:", top5)
    print("Total number of words:", total_words)
    print(f"Proportion of 5 most common words: {top5_total} / {total_words} = {proportion:.2f}%")

# Example
text = "the world is mine and the world is big and the world is beautiful the world is mine out out out out"
top5_word_proportion(text)