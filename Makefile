format:
	black .

migrate:
	alembic revision --autogenerate && alembic upgrade head
