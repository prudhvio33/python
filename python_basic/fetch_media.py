import webbrowser
import json
from urllib.request import urlopen


def get_media(site: str, era: str):

    if site and era is not None:
        url = f'http://archive.org/wayback/available?url={site}&timestamp={era}'
        res = urlopen(url)
        contents = res.read()
        text = contents.decode('utf-8')
        data = json.loads(text)
        if data is not None:
            try:
                old_site = data['archived_snapshots']['closest']['url']
                webbrowser.open(old_site)
            except Exception as e:
                print("enable to open the old site", e)

# Example payload to test
object = get_media("lolcats.com", "20151022")
print(object)
