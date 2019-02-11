"""A package for converting XML to JSON in a predictable way"""

__version__ = '0.1'

import xml.etree.ElementTree as ET


def convert_from_elem(elem: ET.Element):
    return {
        'tag': elem.tag,
        'text': elem.text,
        'attrib': elem.attrib,
        'children': [convert_from_elem(child) for child in elem]
    }


def convert_to_elem(d) -> ET.Element:
    elem = ET.Element(d['tag'], attrib=d.get('attrib', {}))
    elem.extend([convert_to_elem(child) for child in d.get('children', [])])
    elem.text = d.get('text')
    return elem


def parse(xml: str):
    elem = ET.fromstring(xml)
    return convert_from_elem(elem)


def unparse(d, encoding='unicode') -> str:
    elem = convert_to_elem(d)
    return ET.tostring(elem, encoding=encoding)
