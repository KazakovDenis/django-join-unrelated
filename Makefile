style:
	poetry run isort -c .
	poetry run pflake8
	poetry run mypy

migrate:
	poetry run python manage.py migrate

test:
	poetry run coverage run
	poetry run coverage report

publish:
	poetry publish --build
