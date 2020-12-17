def reverse_words(s: str) -> str:
    return " ".join([x[::-1] for x in s.split(" ")])

print(reverse_words("Let's take LeetCode contest"))