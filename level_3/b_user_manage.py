"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str) -> None:
        try:
            self.usernames.remove(username)
        except ValueError:
            print("Такого пользователя не существует.")


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        self.usernames.clear()


if __name__ == '__main__':
    user_manager = UserManager()
    user_manager.add_user('foo')
    user_manager.add_user('bar')
    print(user_manager.get_users())

    admin_manager = AdminManager()
    admin_manager.add_user('foo')
    admin_manager.add_user('bar')
    print(admin_manager.get_users())
    admin_manager.ban_username('foo')
    print(admin_manager.get_users())
    admin_manager.ban_username('foo')
    print(admin_manager.get_users())

    super_admin_manager = SuperAdminManager()
    super_admin_manager.add_user('foo')
    super_admin_manager.add_user('bar')
    super_admin_manager.add_user('spam')
    print(super_admin_manager.get_users())
    super_admin_manager.ban_username('foo')
    print(super_admin_manager.get_users())
    super_admin_manager.ban_all_users()
    print(super_admin_manager.get_users())
