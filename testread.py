from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url = "http://www.instagram.com/p/CpusuF5Oi1c/?igshid=MDJmNzVkMjY="
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

s = re.split(r'\n+', soup.get_text())

print(s)
