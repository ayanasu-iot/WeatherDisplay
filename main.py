from settings import *
import json
import requests
import subprocess


def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(r.content)


def main():
    url = API_BASEURL + API_KEY
    response = requests.get(url)

    res = response.json()
    json_data = json.dumps(res, indent=4)
    print(json_data)
    icon_url = ICON_BASEURL + res['weather'][0]['icon'] + "@2x.png"

    download_img(icon_url, 'icon.png')

    subprocess.run(['/usr/local/bin/led-image-viewer', 'icon.png', '--led-slowdown-gpio=2'])


if __name__ == '__main__':
    main()
