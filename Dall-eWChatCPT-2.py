import openai
import requests
import matplotlib.pyplot as plt
import numpy as np
import cv2
import urllib.request as urllib

text = input("User: ")

openai.api_key = "KEY"

endpoint = "https://api.openai.com/v1/engines/text-davinci-002/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

data = {
    "prompt": f"I want dall-e to draw {text}, can you write it in a way that Dall-e would understand (write it without any commentary)",
    "max_tokens": 2048,
    "n": 1,
    "stop": None,
    "temperature": 1
}

def draw(text):
    response1 = requests.post(endpoint, headers=headers, json=data)
           
    if response1.status_code == 200:
        return response1.json()["choices"][0]["text"]
    else:
        print(response1.status_code)
        return "Failed"

response2 = openai.Image.create(
    model="image-alpha-001",
    prompt=draw(text)
)

url = response2["data"][0]["url"]

print(draw(text))
print("\n")
print(url)
print("\n")

def url_to_image(url):
	resp = urllib.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image

pltimg = plt.imshow(url_to_image(url))
plt.show()
