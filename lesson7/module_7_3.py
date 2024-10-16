import io
class WordsFinder():
    def __init__(self, *files):
        self.files = files
    def get_all_words(self):
        fil_words = {}
        del_symbol = [',', '.', '=', '!', '?', ';', ':']
        lin_wor = []
        for fil in self.files:
            lin_wor = []
            with open(fil, 'r', encoding='utf-8') as file:
                for line in file:
                    lin = line.lower()
                    for sym in del_symbol:
                        lin = lin.replace(sym, '')
                        lin = lin.replace(' - ', ' ')

                    lin_wor.extend(lin.split())
                fil_words[fil] = lin_wor
        return fil_words

    def find(self,word):
        first_pos = {}
        word = word.lower()
        dic_fil = self.get_all_words()
        for fil, wor in dic_fil.items():
            if word in wor:
                first_pos[fil] = wor.index(word) + 1
        return first_pos

    def count(self, word):
        wor_coun ={}
        word = word.lower()
        dic_fil = self.get_all_words()
        for fil, wor in dic_fil.items():
            coun = wor.count(word)
            wor_coun[fil] = coun
        return  wor_coun




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))