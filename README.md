# ToDoList Project

### В рамках курса *Профессия Python разработчик* создаю приложение - планировщик задач.

стек сpython3.9, Django, Postgres

## **Этап 1**

Для запуска проекта требуется
- установить зависимости из файла requirements.txt 
- в корне проекта создать файл .env и прописать в него переменные окружения:   
SECRET_KEY можно сгенерировать командой в терминале:     
python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'   
DEBUG=True   
DATABASE_URL по маске для postgres psql://<user>:<password>@<host>:<port>/<database_name>

### app Core
models.py
Модель пользователя User наследуется от AbstractUser,  
добавлено необязательного поле дата рождения.  

admin.py  
В админку добавлены фильтры пользователей по полям is_staff, is_active, is_superuser.
