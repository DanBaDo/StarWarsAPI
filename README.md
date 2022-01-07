## Configuration

`./.env`

### Install dependencies into virtual environment (Linux/Mac version)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Reset database

```bash
rm sqlite/star_wars.db
rm migrations -rf
flask db init
flask db migrate
flask db upgrade
```
