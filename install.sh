python -m venv env && \
source env/bin/activate && \
pip install -r requirements.txt && \ 
python manage.py createsuperuser && \
python manage.py migrate 