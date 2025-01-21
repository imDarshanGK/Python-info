from bs4 import BeautifulSoup

html_content = "<html><head><title>My Simple Page</title></head><body></body></html>"
soup = BeautifulSoup(html_content, 'html.parser')
title = soup.title.string

print(title)
