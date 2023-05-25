reset:
	rm -rf media/*.pdf
	rm -rf manager/migrations
	rm -f db.sqlite3
	python3 manage.py makemigrations manager
	python3 manage.py migrate
	@echo "from manager.models import Profile; Profile.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python3 manage.py shell
