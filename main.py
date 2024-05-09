# ABDURAHIMOV SAMIR
# N42 GROUP

# 1-MASALA
#
# import psycopg2
#
# conn = psycopg2.connect(database='postgers',
#                         user='postgres',
#                         password='123',
#                         host='localhost',
#                         port=5432
#                         )
# cur = conn.cursor()
#

# create_table_query = '''
#     create table if not exists Product(
#         id serial PRIMARY KEY,
#         name varchar(100) not null,
#         price float  not null,
#         image varchar(100) not null,
#     );
# '''
# cur.execute(create_table_query)
# conn.commit()
#


# 2-MASALA

# def insert_query_product():
#     insert_into_query = """insert into Product7 (name,price,color,image)
#     values (%s,%s,%s,%s)
#     """
#     insert_multiple_rows = [('flower',22,'yellow','http/samirflowers'), ('water',5,'white,','http/water.com'), ('phone',300,'white','http/phone.net')]
#     for record in insert_multiple_rows:
#         cur.execute(insert_into_query,record)
#     conn.commit()
#     cur.close()
#     conn.close()
#     print("Product inserted successfully")
#
#
# def select_all_product():
#     select_query = 'select * from Product;'
#     cur.execute(select_query)
#     rows = cur.fetchall()
#     for row in rows:
#         print(str(row)
#     print('product successfully inserted')
#
#
# def update_product():
#     select_all_product()
#     _id = int(input('Enter product id : '))
#     name = str(input('Enter new product name : '))
#     update_query = 'update Product set name = %s, author = %s where id =%s;'
#     update_query_params = (name, id)
#     cur.execute(update_query, update_query_params)
#     conn.commit()
#     cur.close()
#     conn.close()
#     print_response('Successfully updated product')
#
# def delete_product():
#     select_all_product()
#     _id = int(input('Enter book id : '))
#     delete_query = 'delete from Product where id = %s;'
#     cur.execute(delete_query, (_id,))
#     conn.commit()
#     cur.close()
#     conn.close()
#     print_response('Successfully deleted product')
#
#
#   3- MASALA
#
# class Alphabet:
#     def __init__(self, sequence):
#         self._sequence = sequence
#         self._index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._index >= len(self._sequence):
#             raise StopIteration
#         else:
#             result = self._sequence[self._index]
#             self._index += 1
#             return result
#
#
# arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' , 'k', 'l', 'm', 'n', 'o', 'p' , 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# sequences = Alphabet(arr)
#
# print(next(sequences))
# for i in sequences:
#     print(i)


#   4- MASALA
# import threading
# import time
#
#
# def print_numbers():
#     for i in range(5):
#         print(f'Number => {i}')
#         time.sleep(1)
#
#
# #
# def print_letters():
#     for i in 'ABCDE':
#         print(f'Letters => {i}')
#         time.sleep(1)
#
#
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
#
# thread1.start()
# thread2.start()

# 5- MASALA

# class Save():
    # def __init__(self , ):





# 6- MASALA

class DbConnect:
    def __init__(self, database, user, password, host, port):
        host = 'localhost'
        user = 'postgres'
        password = '123'
        database = 'postgres'
        port = 5432
        conn = psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port
                        )
        cur = conn.cursor()

    def __enter__(self):
        self.conn = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host, port=self.port)
        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

with DbConnect(database="postgres", user="postgres", password=123, host="localhost", port=5432) as (conn, cur):
    cur.execute("select *from Product")
    rows = cur.fetchall()
    for row in rows:
        print(row)

