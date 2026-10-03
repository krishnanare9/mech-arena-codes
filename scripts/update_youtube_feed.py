import json
import os
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

CHANNEL_ID = "UCt-8e3_yiRWmeVetN49Rxag"
FEED_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
OUTPUT = Path("data/youtube-videos.json")
NS = {"atom": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}

request = urllib.request.Request(FEED_URL, headers={"User-Agent": "MechNovaSiteFeed/1.0"})
with urllib.request.urlopen(request, timeout=30) as response:
    xml_data = response.read()
root = ET.fromstring(xml_data)
entries = []
for entry in root.findall("atom:entry", NS):
    video_id = entry.findtext("yt:videoId", default="", namespaces=NS)
    title = entry.findtext("atom:title", default="", namespaces=NS)
    published = entry.findtext("atom:published", default="", namespaces=NS)
    if video_id and title:
        entries.append({"id": video_id, "title": title, "published": published})
if not entries:
    raise RuntimeError("Feed returned no usable video entries; keeping previous JSON unchanged")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Saved {len(entries)} latest uploads to {OUTPUT}")
