# CodingIdeas 🟩
Platform to upload you project ideas or get project ideas

https://www.codingideas.org/

Feel free to add you CodingIdeas!

## How to use CodingIdeas:
If a great idea for coding comes to your mind, visit codingideas.org, click on `new` and add it - its simple.

You can also use codingideas.org if you want to get inspiration: Browse ideas or just click on `random` to get one randomly.

## Run:
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

## TODO:
- [ ] Dark mode
- [ ] category search
- [ ] category random idea
- [ ] help button
- [ ] account
- [ ] account: Mark idea as done
- [ ] account: Like idea / mark as fav
- [ ] Auto mail after created idea
- [ ] add creator to idea page
- [ ] list top ideas and top creator
- [ ] report idea (+duplicate ideas)
