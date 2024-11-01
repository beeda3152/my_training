# def all_variants(text):
#     n = len(text)
#     for i in range(n):
#         for j in range(i+1, n+1):
#             a = text[i:j]
#             yield a
# for val in all_variants('abcd'):
#     print(val)

def all_variants1(text):
    n = len(text)
    for i in range(1, n+1):
        for j in range(n):
            if n >= i + j:
                a = text[j:i+j]
                yield a

for val in all_variants1('abcd'):
    print(val)