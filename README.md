Under Development.
# linkwire
A gamified critical thinking worksheet for adults.

## Technologies
- Django
- Ajax

## Get it to work
- Clone this repo
- Change into the same directory as manage.py. 
- Create a file called secret.py with content:
```python
# secret.py
key = ')8^((t2xw*p969aqa=h5cf*xl4+z^a(c(p40ix^%x&5z8tx8$g'
```
- Next run:

`python3 virtualenv`

`source env/bin/activate`

`pip install requirements.txt`

`python3 manage.py migrate`

`python3 manage.py runserver`
- go to localhost:8000

## To do list:
- Add the frontend functionality with Ajax
- Deploy to Heroku

### Future Plans
- Make it a React Native app
