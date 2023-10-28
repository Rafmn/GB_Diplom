from bs4 import BeautifulSoup
import ebookmeta

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
        
    def get_info_by_meta(self, furl, tag):
        meta = ebookmeta.get_metadata(furl)  # returning Metadata class
        match tag:
            case 'description':
                return meta.description
