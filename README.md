# Django-news
 **Описание**:  

Новостной сайт на Django.

 **Как запустить проект?**: 
 
  Установить все зависимости
  
 ```
 pip install -r requirements.txt
```

и прописать команду:
 ```
python manage.py runserver
```
Далее перейти по локальному адресу. В Django это обычно http://localhost:8000 или http://127.0.0.1:8000. 

Так же сделано API:

GET /api/categories/ - список категорий

POST /api/categories/ - создать категорию

GET/PUT/PATCH/DELETE /api/categories/<id>/ - работа с конкретной категорией

Новости:

GET /api/news/ - список новостей (с фильтрацией по категории и поиском)

POST /api/news/ - создать новость

GET/PUT/PATCH/DELETE /api/news/<id>/ - работа с конкретной новостью

GET /api/news/<id>/comments/ - комментарии к новости

Комментарии:

GET /api/comments/ - список комментариев

POST /api/comments/ - создать комментарий

GET/PUT/PATCH/DELETE /api/comments/<id>/ - работа с конкретным комментарием

