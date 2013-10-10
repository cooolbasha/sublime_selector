import unittest

import replace

class ReplaceTestCase(unittest.TestCase):

    def test_alpha_numeric(self):
        text = 'abc123'
        expected_text = 'abc123'
        output_text = replace.alpha_num(text)
        self.assertEqual(expected_text, output_text)

        text = 'abc 123 ***'
        expected_text = 'abc123'
        output_text = replace.alpha_num(text)
        self.assertEqual(expected_text, output_text)

        text = '***'
        expected_text = ''
        output_text = replace.alpha_num(text)
        self.assertEqual(expected_text, output_text)

    def test_slugify(self):
        text = 'foo-bar-buzz'
        expected_text = 'foo-bar-buzz'
        output_text = replace.slugify(text)
        self.assertEqual(expected_text, output_text)

        text = 'foo bar buzz !*('
        expected_text = 'foo-bar-buzz'
        output_text = replace.slugify(text)
        self.assertEqual(expected_text, output_text)

        text = ' '
        expected_text = ''
        output_text = replace.slugify(text)
        self.assertEqual(expected_text, output_text)

    def test_wrap(self):
        text = 'foo'
        expected_text = '<b>foo</b>'
        output_text = replace.wrap(text, '<b>', '</b>')
        self.assertEqual(expected_text, output_text)

    def test_classify(self):
        text = 'foo bar'
        expected_text = 'FooBar'
        output_text = replace.classify(text)
        self.assertEqual(expected_text, output_text)

    def test_title(self):
        text = 'i love biscuits'
        expected_text = 'I Love Biscuits'
        output_text = replace.title(text)
        self.assertEqual(expected_text, output_text)

