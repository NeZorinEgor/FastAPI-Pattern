# Шаблон FastPAI для быстрого старта

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" title="fastapi" width="40" height="40"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" title="mysql" width="40" height="40"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" title="redis" width="40" height="40"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nginx/nginx-original.svg" title="nginx" width="40" height="40"/>&nbsp;

### Шаблон создан для того, что бы можно было писать проект с бизнес-логики, без затрат времени на:
1. подключения синхронного / асинхронного движка `MySQL`
2. подключения `Alembic` миграций
3. подключение прокси `Nginx`
4. подключение кэша `Redis`
5. установку 'портабельных' зависимостей через `Dockerfile` / `docker-compose.yaml`

### [Зависимость для работы с базой данных](src/database.py)
```python
# sample: session: AsyncSession = Depends(get_session)
async def get_session() -> AsyncSession:
    async with session_factory() as session:
        yield session
```

### [Установка моделей для миграций](migrations/env.py)
```python
from src.database import Base
# Your models here ↓
from src.<your_service_name>.model imaport SomeModel

target_metadata = Base.metadata
```

### [Проксирование fastapi контейнера](nginx/conf.d/default.conf)
```
upstream backend {
    server fastapi:5000;
}

server {
    listen 80;
    location / {
        proxy_pass http://backend;
        }
}
```
### Ревизии миграции:
1. ```
   alembic revision --autogenerate -m "<migration message>"
   ```
   
2. ```python
   alembic upgrade head
   ```

### Запуск

1. ```
   git clone https://github.com/NeZorinEgor/FastAPI-Pattern.git
   ```
   
2. ```
   cd  FastAPI-Pattern
   ```
   
3. ```
   cp .env.example .env
   ```
   
4. ```
   docker-compose up --build
   ```
   
