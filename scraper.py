from lxml import html
from lxml import etree
from lxml.etree import tostring
import requests

def prettyprint(element, **kwargs):
  xml = etree.tostring(element, **kwargs)
  return xml.decode()

# Make a GET request to the website
page = requests.get('https://zero.estate/category/zero/chugoku/okayama/')
hp = etree.HTMLParser(encoding='utf-8')
tree = html.fromstring(page.content, parser=hp)

# Use XPath to select the desired element(s)
#items = tree.xpath('//div[class="kanren "]/dl/dd/h3/text()')
properties = tree.xpath('//h3/a')
print(prettyprint(properties[0]))

dates = tree.xpath('//div[@class="blog_info"]/p/i')
print(prettyprint(dates[0]))

# Only save the top item in the HTML file
filename = 'okayama.md'
with open(filename, 'w') as modified:
  modified.write('<dl><dd>' + prettyprint(dates[0]) + ' ' + prettyprint(properties[0]) + '</dd></dl>\n')
