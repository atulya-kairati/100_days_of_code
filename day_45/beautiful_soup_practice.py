from bs4 import BeautifulSoup

html_file = open('my_site/Index.html')
html_text = html_file.read()
html_file.close()

soup = BeautifulSoup(html_text, 'html.parser')
# print(soup.prettify())
print(soup.a)
print(soup.title.string)
print(soup.p)
print(soup.img)

a_tags = soup.find_all(name='a')

for a in a_tags:
    print(f'{a.getText()} --> {a.get("href")}')

contact_id_tag = soup.find(id='me')
print(contact_id_tag)
contact_id_tag = soup.find(name="img", id='me')
print(contact_id_tag)
heading_class_tag = soup.find(name="h1", class_='heading')
print(heading_class_tag)

# using css selectors
print(soup.select_one('#me'))  # using id
print(soup.select('.topic'))   # using class
print(soup.select('div .skills h2'))  # using combination of tag name and class

