#revert words in string
s="how are you in python"
s1=s.split()
s2=s1[::-1]
print(' '.join(s2))


def reverse_string_words(text):
    for line in text.split('\n'):
        return (' '.join(line.split()[::-1]))
print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))