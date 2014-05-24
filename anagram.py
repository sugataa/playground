import collections


def sort_prehash(word):
    return ''.join(sorted(word))


def count_letters_prehash(word):
    return tuple(collections.Counter(word).items())


def group_anagrams(words, hash_function):
    result = {}
    for w in words:
        s = hash_function(w.lower())
        if s in result:
            result[s] |= {w}
        else:
            result[s] = {w}
    return result.values()

testList = ["tsar", "rat", "tar", "star", "tars", "cheese"]
print(group_anagrams(testList, count_letters_prehash))

