export FLASK_APP=entrypoint.py
export FLASK_ENV=development
# flask run --host=0.0.0.0
# gunicorn -w 4 -b 0.0.0.0:5000 app/__init__:
gunicorn -c gunicorn.py entrypoint:application