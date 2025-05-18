import os
import requests

# Correct chord data
chord_data = {
    "Gm7": ("353333", "-23144"),
    "Am7": ("x02010", "-0102-"),
    "F": ("133211", "134211"),
    "A7": ("x02020", "-0102-"),
    "Bbmaj7": ("x13231", "-1324-"),
    "C": ("x32010", "-32-1-"),
    "Dm": ("xx0231", "---132")
}

# Config
output_dir = "chords"
os.makedirs(output_dir, exist_ok=True)
base_url = "https://chordgenerator.net"

# Normalize fingering to 6 characters with hyphens
def normalize_fingers(f):
    result = ""
    for c in f:
        if c in "1234":
            result += c
        else:
            result += "-"
    return result.ljust(6, "-")

# Download each chord diagram
for chord, (positions, fingers) in chord_data.items():
    # Ensure fingering string is valid
    normalized_f = normalize_fingers(fingers)
    url = f"{base_url}/{chord}.png?p={positions}&f={normalized_f}&s=2&b=false"
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{output_dir}/{chord}.png", 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {chord}")
    else:
        print(f"Failed to download {chord} — HTTP {response.status_code} — URL: {url}")
