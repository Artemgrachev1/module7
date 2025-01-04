class WordsFinder:

    def __init__(self, *file_txt):
        self.file_names = file_txt

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                file = file.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    file = file.replace(j, '')
                words = file.split()
                all_words[i] = words
        return all_words

    def find(self, word):
        finds = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                finds[name] = words.index(word.lower()) + 1

        return finds

    def count(self, word):
        count = {}
        for name, words in self.get_all_words().items():
            words_count = words.count(word.lower())
            count[name] = words_count
        return count

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
