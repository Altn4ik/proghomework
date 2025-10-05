books = [
    {"id": 1, "title": "Мастер и Маргарита", "author": "Булгаков", "year": 1966},
    {"id": 2, "title": "Преступление и наказание", "author": "Достоевский", "year": 1866},
    {"id": 3, "title": "Война и мир", "author": "Толстой", "year": 1869},
    {"id": 4, "title": "Анна Каренина", "author": "Толстой", "year": 1877},
    {"id": 5, "title": "Собачье сердце", "author": "Булгаков", "year": 1925}
]

def bubble_sort(books):
    n=len(books)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if books[j+1]["year"] < books[j]["year"]:
                books[j], books[j+1] = books[j+1], books[j]
                swapped = True
        if not swapped:
            break
    return books
# print(bubble_sort(books))

def linear_sort(books):
    target = input('Введите книгу: ').lower()
    for i in range(len(books)):
        if books[i]['title'].lower() == target:
            return books[i]
    return None
# print(linear_sort(books))


def search_author(books):
    author_find = input('Введите автора: ').capitalize()
    books_autors=[]
    for i in range(len(books)):
        if books[i]['author'] == author_find:
            books_autors.append(books[i]['title'])
    print(books_autors)
# search_author(books)

def filter_books_by_years(books):
    lower_limit=int(input('Введите с кого года произвести поиск: '))
    upper_limit=int(input('По какой: '))
    books_filtered = []
    for i in range(len(books)):
        if lower_limit <= books[i]['year'] <= upper_limit:
            books_filtered.append(books[i])
    print(books_filtered)
# filter_books_by_years(books)

