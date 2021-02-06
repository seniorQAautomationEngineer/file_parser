import json
import xml.etree.ElementTree as ET
import datetime as dt
from datetime import date
from datetime import timedelta as td
from nested_lookup import nested_delete


# 1. Create a python method that takes arguments int X and int Y, and updates departdate and returndate fields  in test_payload1.xml:
# - departdate gets set to X days in the future from the current date
# (whatever the current date is at the moment of executing the code)
# - returndate gets set to Y days in the future from the current date

# 2. Create a python method that takes a json element as an argument, and removes that element from test_payload.json.

# 3.Please enhance the python method for updating dates in the XML file:
# Make the method accept additional arguments: depart_tag, return_tag, date_format,
 # so that the method can modify dates in either test_payload1.xml or test_payload2.xml (attached).
# Please use any python libraries that are best suited for working on these input files.
# Please send back python3 code that can be executed.

def update_xml(x: int, y: int, xml: str, leave_tag: str, return_tag: str, date_format: str, ):
    today = date.today()
    tree = ET.parse(xml)
    root = tree.getroot()
    if 'combined' in date_format:
        for child in root.iter(leave_tag):
            child.text = (today + td(days=+x)).strftime('%Y%m%d')
        for child in root.iter(return_tag):
            child.text = (today + td(days=+y)).strftime('%Y%m%d')
    if 'simple' in date_format:
        for child in root.iter(leave_tag):
            child.text = f'{dt.date.today() + td(days=+x)}'
        for child in root.iter(return_tag):
            child.text = f'{dt.date.today() + td(days=+y)}'
    tree.write('new_' + xml)



update_xml(x=10, y=13, xml='test_payload1.xml', leave_tag='departdate', return_tag='returndate', date_format='simple')
update_xml(x=10, y=13, xml='test_payload2.xml', leave_tag='DEP', return_tag='RET', date_format='combined')


def remove_element_from_json(json_elem, json_file):
    with open(json_file) as f:
        data = json.load(f)

    data = nested_delete(data, json_elem)
    with open('new_' + json_file, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=True, indent=4)


remove_element_from_json('statecode', 'test_payload.json')
