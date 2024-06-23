# Шаблон FastPAI для быстрого старта

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" title="fastapi" width="40" height="40"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" title="mysql" width="40" height="40"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" title="redis" width="40" height="40"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nginx/nginx-original.svg" title="nginx" width="40" height="40"/>&nbsp;

### Шаблон создан для того, что бы можно было писать проект с бизнес-логики, без затрат времени на:
1. подключения синхронного / асинхронного движка `MySQL`
2. подключения `Alembic` миграций
3. подключение прокси `Nginx`
4. подключение кеша `Redis`
5. установку 'портабельных' зависимостей через `Dockerfile` / `docker-compose.yaml`

### Запуск
1. ```cp .env.example .env```
2. ```docker-compose up --build```
