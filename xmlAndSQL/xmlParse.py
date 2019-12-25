import dicttoxml
from xml.dom.minidom import parseString
import os

d =[ 3, 'person',
    {"name":'zhangt', "age":18, 'sal': 200},
    {"name":'zhangf', "age":40, 'sal': 5000},
    {"name":'zhangz', "age":10, 'sal': 14.5}
]

bxml = dicttoxml.dicttoxml(d, custom_root='persons');

xml = bxml.decode('utf-8')

print (xml)

dom = parseString(xml)

prettyXml = dom .toprettyxml(indent='    ')

os.makedirs('files', exist_ok=True)
f= open('files/persons.xml', 'w+', encoding='utf-8')

f.write(prettyXml)
f.close()

