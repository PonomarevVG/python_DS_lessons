import pandas as pd

authors_dict = {
    "author_id": [1, 2, 3],
    "author_name": ['Тургенев', 'Чехов', 'Островский']
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

authors_price["min_price"] = authors_price["price"]
authors_price["max_price"] = authors_price["price"]
authors_price["mean_price"] = authors_price["price"]
authors_groups = authors_price.groupby("author_name")

authors_stat = authors_groups.agg({"min_price": "min", "max_price": "max", "mean_price": "mean"})

print("\nauthors_stat :")
print(authors_stat)
