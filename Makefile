format:
	black .

migrate:
	alembic revision --autogenerate && alembic upgrade head

seed:
	python seed.py

run:
	uvicorn main:app --reload