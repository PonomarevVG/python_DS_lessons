import pandas as pd

authors_dict = {
    "author_id": [1, 2, 3],
    "authors_name": ['Тургенев', 'Чехов', 'Островский']
}

authors = pd.DataFrame(authors_dict)
print("Датафрейм authors:")
print(authors)

book_dict = {
    "author_id": [1, 1, 1, 2, 2, 3, 3],
    "book_title": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    "price": [450, 300, 350, 500, 450, 370, 290]
}

print("\nДатафрейм book_dict:")
book = pd.DataFrame(book_dict)
print(book)

print("\nДатафрейм authors_price")
authors_price = pd.merge(authors, book, on='author_id')
print(authors_price)
