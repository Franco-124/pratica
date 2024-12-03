import requests

def get_category():
    r=requests.get('http://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))

    categories = r.json()
    print(categories)

    for category in categories:
        print(category['name'])