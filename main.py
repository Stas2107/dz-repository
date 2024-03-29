# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень
# доступа и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список
# экземпляров User).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам
# через методы (например, get и set методы).

class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__access_level = 'user'

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__access_level = 'admin'
        self.__user_list = []

    def add_user(self, user):
        if isinstance(user, User):
            self.__user_list.append(user)

    def remove_user(self, user):
        if user in self.__user_list:
            self.__user_list.remove(user)

    def show_users(self):
        for user in self.__user_list:
            print(user.get_name())


admin = Admin(0, 'Admin')
user1 = User(1, 'User1')
user2 = User(2, 'User2')

admin.add_user(user1)
admin.add_user(user2)

admin.show_users()  # Выводит: 'User1', 'User2'

admin.remove_user(user1)

admin.show_users()  # Выводит: 'User2'