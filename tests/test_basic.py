from xmltojson import parse, unparse
import unittest


class XMLToJSONTestCase(unittest.TestCase):
    def test_minimal(self):
        self.assertEqual(parse('<a />'), {
            'tag': 'a',
            'attrib': {},
            'text': None,
            'children': [],
        })

        self.assertEqual(unparse({
            'tag': 'a',
            'attrib': {},
            'text': None,
            'children': [],
        }), '<a />')

    def test_attrib(self):
        self.assertEqual(parse('<a foo="1" />'), {
            'tag': 'a',
            'attrib': {'foo': '1'},
            'text': None,
            'children': [],
        })

        self.assertEqual(unparse({
            'tag': 'a',
            'attrib': {'foo': '1'},
            'text': None,
            'children': [],
        }), '<a foo="1" />')

    def test_text(self):
        self.assertEqual(parse('<a>Hello, &lt;name&gt;!</a>'), {
            'tag': 'a',
            'attrib': {},
            'text': 'Hello, <name>!',
            'children': [],
        })

        self.assertEqual(unparse({
            'tag': 'a',
            'attrib': {},
            'text': 'Hello, <name>!',
            'children': [],
        }), '<a>Hello, &lt;name&gt;!</a>')

    def test_children(self):
        self.assertEqual(parse('<a><b /><c /><b /></a>'), {
            'tag': 'a',
            'attrib': {},
            'text': None,
            'children': [{
                'tag': 'b',
                'attrib': {},
                'text': None,
                'children': [],
            }, {
                'tag': 'c',
                'attrib': {},
                'text': None,
                'children': [],
            }, {
                'tag': 'b',
                'attrib': {},
                'text': None,
                'children': [],
            }],
        })

        self.assertEqual(unparse({
            'tag': 'a',
            'attrib': {},
            'text': None,
            'children': [{
                'tag': 'b',
                'attrib': {},
                'text': None,
                'children': [],
            }, {
                'tag': 'c',
                'attrib': {},
                'text': None,
                'children': [],
            }, {
                'tag': 'b',
                'attrib': {},
                'text': None,
                'children': [],
            }],
        }), '<a><b /><c /><b /></a>')

    def test_all(self):
        self.assertEqual(parse('<a foo="2"><b bar="4" /><c>Hello</c><b /></a>'), {
            'tag': 'a',
            'attrib': {
                'foo': '2',
            },
            'text': None,
            'children': [{
                'tag': 'b',
                'attrib': {
                    'bar': '4',
                },
                'text': None,
                'children': [],
            }, {
                'tag': 'c',
                'attrib': {},
                'text': 'Hello',
                'children': [],
            }, {
                'tag': 'b',
                'attrib': {},
                'text': None,
                'children': [],
            }],
        })

        self.assertEqual(unparse({
            'tag': 'a',
            'attrib': {
                'foo': '2',
            },
            'text': None,
            'children': [{
                'tag': 'b',
                'attrib': {
                    'bar': '4',
                },
                'text': None,
                'children': [],
            }, {
                'tag': 'c',
                'attrib': {},
                'text': 'Hello',
                'children': [],
            }, {
                'tag': 'b',
                'attrib': {},
                'text': None,
                'children': [],
            }],
        }), '<a foo="2"><b bar="4" /><c>Hello</c><b /></a>')
