from bs4 import BeautifulSoup


class Fb2_info:
    def __init__(self, fname=None) -> None:
        self.fname = fname

    # Извлечение данных из файла
    def get_fb2_info(self, fname, tag):
        with open(fname, 'r', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'xml')
        if soup.find(tag, {'value': True}):
            return soup.find(tag, {'value': True})['value']
        elif soup.find(tag):
            return soup.find(tag).text

    # Создание списка книг с данными
    def create_list_books(self, list_of_files):
        myList = []
        for i in enumerate(list_of_files):
            author_f = self.get_fb2_info(f'./Books/{i[1]}', 'author').replace("\n", " ")
            book_title_f = self.get_fb2_info(f'./Books/{i[1]}', 'book-title').replace("\n", " ")
            s = str(i[0]+1) + '. ' + '"' + book_title_f + '"' + ',' + ' ' + author_f
            myList.append(s)
        return myList
