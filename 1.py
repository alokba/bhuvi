#adding html tags to strings
def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)


print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
print(add_tags('a','href'))