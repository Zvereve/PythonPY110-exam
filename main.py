import random
import json
from conf import MODEL
from faker import Faker


def pk(value = 1):
    """Функция счетчик"""
    while True:
        yield value
        value += 1


def tit():
    """Функция возврта из файла рандомного наименования книги"""
    with open('books.txt', 'r') as f:
        x = random.randint(0, len(f.readlines())-1)

    with open('books.txt', 'r', encoding="utf-8") as f:
        y = list(f.readlines())
    return y[x].replace("\n", "")


def ff():
    """Функция возвращающая рандомный международный стандартный код книги"""
    fake = Faker()
    return fake.bothify(text="%%%-%-%%%%%-%%%-%")


def autors():
    """Функция возвращает авторов книг от 1 до 3х"""
    st = []
    fake = Faker()
    for i in range(random.randint(1, 3)):
        st.append(fake.name())
    return st


def booklist():
    """Функция возвращает словарь"""
    yield {
               "model": MODEL,
               "pk": next(coun),
               "fields": {
                          "title": tit(),
                          "year": random.randint(1900, 2021),
                          "pages": random.randint(100, 2000),
                          "isbn13": ff(),
                          "rating": round(random.triangular(0, 5), 2),
                          "price": round(random.triangular(100, 10000), 2),
                          "author": [
                                     autors()
                                    ]
                          }
               }


def main():
    """Функция генератор списка книг и записи списка в фаил"""
    st = []
    for _ in range(100):
        st.append(next(booklist()))
        print(st)
    with open('UserList.json', 'w', encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    coun = pk()
    main()