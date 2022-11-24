import requests

def req():    
    r = requests.get('https://www.rtvslo.si/iskalnik?q=iskalni')
    print(r.text)


req()