from django.contrib.auth.models import User

try: 
    User.objects.create_superuser('admin', 'stifeev99@mail.ru', 'admin')
except:
    pass