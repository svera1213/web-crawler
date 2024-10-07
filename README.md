# web-crawler

### 1) Setup Docker images: Django and Postgres
- Setup Dockerfile
- Setup requirements.txt
- Setup docker-compose.yml

### 2) Build images
    docker compose up -d

### 3) Run migrations
    docker compose exec web python manage.py migrate

### 4) Create user to access Admin `http://localhost:8000/admin`
    docker compose exec web python manage.py createsuperuser

### 5) Run script `load_news_headlines`
    docker compose exec web python manage.py runscript load_news_headlines

A page argument can be added to load more headlines from Hacker News. Currently, 30 headlines per page.

    docker compose exec web python manage.py runscript load_news_headlines --script-args <number of pages to load>

### 6) Call endpoint `GET /api/hacker-news/headlines` to load the scrapped Hacker News headlines
The parameter `ordering_type` accepts `A` or `B`: `GET /api/hacker-news/headlines?ordering_type=<A or B>`
