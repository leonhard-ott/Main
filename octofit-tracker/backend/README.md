OctoFit Tracker — backend (Django)

Quickstart

1. Create venv (already created in this workspace):

   python3 -m venv venv

2. Activate venv:

   source venv/bin/activate

3. Install dependencies:

   pip install -r requirements.txt

4. Run migrations:

   python manage.py migrate

5. Run dev server (bind to all interfaces to access via forwarded port 8000):

   python manage.py runserver 0.0.0.0:8000

Notes
- The repository follows the OctoFit Tracker structure. The venv is in `venv/` under this backend directory; don't commit it.
- Ports: 8000 is the public dev server port for Django as specified in the project guidelines.
