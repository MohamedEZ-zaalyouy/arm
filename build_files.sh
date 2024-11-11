echo "BUILD START V9"

# create a virtual environment named 'venv' if it doesn't already exist
python3.9 -m venv venv

# activate the virtual environment
source venv/bin/activate

pip install -r requirements.txt

# collect static files using the Python interpreter from venv
python manage.py collectstatic --noinput

echo "BUILD END"