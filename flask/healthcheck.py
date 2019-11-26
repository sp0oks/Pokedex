import requests

if __name__ == '__main__':
    try:
        r = requests.get('http://127.0.0.1:5000')
        if r.ok:
            exit(0)
        exit(1)
    except Exception as e:
        print(e)
        exit(1)
