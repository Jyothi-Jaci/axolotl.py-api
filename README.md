# axolotl.py
 A simple API for axolotl fans

# Api link
https://axoltlapi.herokuapp.com/

# How to use
Example in python
```py
import requests,json
d=requests.get('https://axoltlapi.herokuapp.com/').content
d=d.decode('utf-8')
r=json.loads(d)
print(r)
```

# Repository Dependencies
- Python 3.8 or later
- [fastapi](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [gunicorn](https://gunicorn.org/)


