## Python XML processing

### Get tag name
https://stackoverflow.com/questions/1896628/lxml-objectify-documentelement-tagname


### Basic example of lxml parser
https://stackoverflow.com/questions/3106480/really-simple-way-to-deal-with-xml-in-python

```
>>> from lxml import objectify
>>> tree = objectify.fromstring(your_xml)
>>> tree.weather.attrib["module_id"]
'0'
>>> tree.weather.forecast_information.city.attrib["data"]
'Mountain View, CA'
>>> tree.weather.forecast_information.postal_code.attrib["data"]
'94043'
```

### Check if lxml tag exists
https://stackoverflow.com/questions/5385821/python-lxml-objectify-checking-whether-a-tag-exists