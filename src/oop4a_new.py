class DataBase:
    # Паттерн проектирование Singleton
    # Начало паттерна
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None
    # Конец паттерна

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        print('Чтение данных из БД')

    def write(self, data):
        print(f'Запись в БД {data}')

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(id(db))
print(id(db2 ))

db.connect()
db2.connect()