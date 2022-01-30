from django.contrib.auth.models import User


# Создание пользователя и сохранение его в базе данных
def createAdmin():
    print("create admin")
    user = User.objects.create_user('admin', 'test@test.com', 'admin')

    user.first_name = 'Admin'
    user.last_name = 'Admin'
    user.save()


