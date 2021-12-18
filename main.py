import random
from conf import MODEL
from faker import Faker


def pk(start=1):
    while True:
        yield start
        start += 1


def tit():
    with open('books.txt', 'r') as f:
        x = random.randint(1, len(f.readlines()))

    return x


def ff():
    fake = Faker()
    return fake.bothify(text="%%%-%-%%%%%-%%%-%")


def autors():
    x = random.randint(1, 3)
    st =[]
    fake = Faker()
    for i in range(x):
        st.append(fake.name())
    return st


def booklist():
    yield {
            "model": MODEL,
            "pk": next(pk()),
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
    #stt = {}
    for x in range(100):
        print(next(booklist()))




if __name__ == '__main__':
    main()
