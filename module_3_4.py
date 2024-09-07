def single_root_words(root_word, *other_words):
    same_words = []
    s1 = root_word.lower()
    for st in other_words:
        s2 = st.lower()
        if s1 in s2:
            same_words.append(st)
        if s2 in s1:
            same_words.append(st)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
