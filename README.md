# ProjectIdeas
Platform to uplaod you project ideas or get project ideas


## Run
1. Install all requirements
```console
$ pip3 install -r requirements.txt
```

2. Create the DB:
```console
$ python3
```
```python
from app import db
db.create_all()
exit()
```

3. Run
```console
$ python3 app.py
```