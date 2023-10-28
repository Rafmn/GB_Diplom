from db import DB
import ebookmeta


book = "dfg"
author = "ghjj"


# DB("Marat1", "a_book1", "filename.fgt", "/home/marat/GeekBrains/Diplom/Books/chelovek-mashina(1).fb2").add_book()
# DB().search_name_file("filename.fgt")
# DB().get_list_books()

meta = ebookmeta.get_metadata('/home/marat/GeekBrains/Diplom/Books/chelovek-mashina(1).fb2')  # returning Metadata class
print(meta.title)
print(meta.author_list)
print(meta.author_list_to_string)
print(meta.author_sort_list)
print(meta.cover_file_name)
print(meta.publish_info)
print(meta.description)