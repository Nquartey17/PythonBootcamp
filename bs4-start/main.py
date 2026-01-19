from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get(("href")))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3",class_="heading") #class is a keyword in python. Use class_ instead

company_url = soup.select_one(selector="p a") #get link in <p><a>
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading") #select returns list
print(headings)