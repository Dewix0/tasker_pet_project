# Tasker — Pet Project for DRF Junior

## Стек
- Python 3.13
- Django Rest Framework
- PostgreSQL
- Celery
- Docker

## Запуск проекта
```bash
git clone https://github.com/Dewix0/tasker_pet_project.git
docker-compose up -d --build
```

## API
	•	GET /api/tasks/ → Получить список задач.
	•	POST /api/tasks/ → Создать новую задачу.
	•	GET /api/tasks/1/ → Получить задачу с ID 1.
	•	PUT /api/tasks/1/ → Обновить задачу с ID 1.
	•	DELETE /api/tasks/1/ → Удалить задачу с ID 1.




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





