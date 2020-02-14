from settings import *
import json
import requests
import subprocess


def main():
    url = API_BASEURL + API_KEY
    response = requests.get(url)

    res = response.json()
    json_data = json.dumps(res, indent=4)
    print(json_data)
    icon_uri = './images/' + res['weather'][0]['main'] + ".png"

    subprocess.run(['/usr/local/bin/led-image-viewer', icon_uri, '--led-slowdown-gpio=2'])


if __name__ == '__main__':
    main()
