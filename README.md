# Tasker — Pet Project for DRF Junior

## Стек
- Python 3.13
- Django Rest Framework
- PostgreSQL
- Docker

## Запуск проекта
```bash
git clone https://github.com/Dewix0/tasker_pet_project.git
docker-compose up -d --build
```


### API Эндпоинты

#### Аутентификация

**Регистрация пользователя**  
`POST /api/register/`  
- **Описание:** Регистрация нового пользователя.  
- **Тело запроса:**  
  ```json
  {
    "username": "user1",
    "email": "user1@example.com",
    "password": "password123",
    "password2": "password123"
  }
  ```
- **Ответ (201 Created):**  
  ```json
  {
    "username": "user1",
    "email": "user1@example.com"
  }
  ```

---

**Вход в систему**  
`POST /api/login/`  
- **Описание:** Авторизация пользователя и получение JWT-токенов.  
- **Тело запроса:**  
  ```json
  {
    "username": "user1",
    "password": "password123"
  }
  ```
- **Ответ (200 OK):**  
  ```json
  {
    "refresh": "your-refresh-token",
    "access": "your-access-token"
  }
  ```

---

#### Задачи

**Получить список задач**  
`GET /api/tasks/`  
- **Описание:** Возвращает список задач текущего пользователя.  
- **Заголовки:**  
  - `Authorization: Bearer your-access-token`
- **Ответ (200 OK):**  
  ```json
  [
    {
      "Task_ID": 1,
      "User_ID": 1,
      "Status": "NS",
      "Description": "Купить молоко",
      "Priority": "H",
      "Deadline": "2025-03-20"
    }
  ]
  ```

---

**Создать новую задачу**  
`POST /api/tasks/`  
- **Описание:** Создает новую задачу для текущего пользователя.  
- **Заголовки:**  
  - `Authorization: Bearer your-access-token`
- **Тело запроса:**  
  ```json
  {
    "Description": "Сделать домашнее задание",
    "Status": "NS",
    "Priority": "M",
    "Deadline": "2025-03-22"
  }
  ```
- **Ответ (201 Created):**  
  ```json
  {
    "Task_ID": 2,
    "User_ID": 1,
    "Status": "NS",
    "Description": "Сделать домашнее задание",
    "Priority": "M",
    "Deadline": "2025-03-22"
  }
  ```

---

**Получить задачу по ID**  
`GET /api/tasks/{id}/`  
- **Описание:** Возвращает детальную информацию о задаче по её ID.  
- **Заголовки:**  
  - `Authorization: Bearer your-access-token`
- **Ответ (200 OK):**  
  ```json
  {
    "Task_ID": 2,
    "User_ID": 1,
    "Status": "NS",
    "Description": "Сделать домашнее задание",
    "Priority": "M",
    "Deadline": "2025-03-22"
  }
  ```

---

**Обновить задачу по ID**  
`PUT /api/tasks/{id}/`  
- **Описание:** Полностью обновляет данные задачи.  
- **Заголовки:**  
  - `Authorization: Bearer your-access-token`
- **Тело запроса:**  
  ```json
  {
    "Status": "ACT",
    "Description": "Сделать домашнее задание",
    "Priority": "H",
    "Deadline": "2025-03-25"
  }
  ```
- **Ответ (200 OK):**  
  ```json
  {
    "Task_ID": 2,
    "User_ID": 1,
    "Status": "ACT",
    "Description": "Сделать домашнее задание",
    "Priority": "H",
    "Deadline": "2025-03-25"
  }
  ```

---

**Частично обновить задачу**  
`PATCH /api/tasks/{id}/`  
- **Описание:** Позволяет изменить часть полей задачи.  
- **Заголовки:**  
  - `Authorization: Bearer your-access-token`
- **Тело запроса:**  
  ```json
  {
    "Status": "DN"
  }
  ```
- **Ответ (200 OK):**  
  ```json
  {
    "Task_ID": 2,
    "User_ID": 1,
    "Status": "DN",
    "Description": "Сделать домашнее задание",
    "Priority": "H",
    "Deadline": "2025-03-25"
  }
  ```

---

**Удалить задачу**  
`DELETE /api/tasks/{id}/`  
- **Описание:** Удаляет задачу по её ID.  
- **Заголовки:**  
  - `Authorization: Bearer your-access-token`
- **Ответ (204 No Content):**  
  ```json
  {
    "message": "Вы удалили задачу, без возможности восстановления"
  }
  ```
```  



# Чек-лист по подготовке к собесу

### Python
- Алгоритмы: сортировки, поиск, списки, множества
- Асинхронность: asyncio, async def, task group (3.11+)
- ООП: классы, наследование, миксины
- Новое в Python 3.13

### DRF
- Сериалайзеры
- ViewSets и Generic Views
- Фильтры и сортировки
- Permissions
- Аутентификация и авторизация

### База
- SQL-запросы (SELECT с JOIN, WHERE, GROUP BY)
- Индексы
- Миграции
- Связи ForeignKey, ManyToMany

### Docker
- Как запустить Django в контейнере
- Docker Compose для зависимостей (PostgreSQL + Redis)

### Celery
- Как работает, зачем нужен, пример задачи





