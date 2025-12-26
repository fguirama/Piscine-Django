import unittest
import os

from elem import Elem, Text
from Page import Page

from elements import (
    Html, Head, Body, Title, Meta, Img,
    Table, Tr, Th, Td,
    Ul, Ol, Li,
    H1, H2, P, Div, Span,
    Hr, Br
)


class TestPageValidation(unittest.TestCase):

    # ---------- VALID CASES ----------

    def test_valid_minimal_html(self):
        page = Page(
            Html([
                Head([Title([Text('Hello')])]),
                Body([Text('World')])
            ])
        )
        self.assertTrue(page.is_valid())

    def test_valid_complex_page(self):
        page = Page(
            Html([
                Head([Title([Text('Title')])]),
                Body([
                    H1([Text('Header')]),
                    Div([
                        Span([
                            Text('Span text'),
                            P([Text('Paragraph')])
                        ])
                    ]),
                    Ul([
                        Li([Text('Item 1')]),
                        Li([Text('Item 2')])
                    ]),
                    Table([
                        Tr([Th([Text('A')]), Th([Text('B')])]),
                        Tr([Th([Text('C')]), Th([Text('D')])])
                    ])
                ])
            ])
        )
        self.assertTrue(page.is_valid())

    # ---------- INVALID TAG ----------

    def test_invalid_unknown_tag(self):
        class Foo(Elem):
            pass

        page = Page(Foo([Text('invalid')]))
        self.assertFalse(page.is_valid())

    def test_invalid_type(self):
        try:
            page = Page('invalid string')
        except TypeError:
            page = None
        self.assertIsNone(page)

    # ---------- HTML STRUCTURE ----------

    def test_html_must_have_head_then_body(self):
        page = Page(
            Html([
                Body([Text('body')]),
                Head([Title([Text('title')])])
            ])
        )
        self.assertFalse(page.is_valid())

    def test_html_missing_head(self):
        page = Page(
            Html([
                Body([Text('body')])
            ])
        )
        self.assertFalse(page.is_valid())

        page = Page(
            Html(Body([Text('body')]))
        )
        self.assertFalse(page.is_valid())

    def test_html_have_two_body(self):
        page = Page(
            Html([
                Body([Text('body')]),
                Body([Text('body')])
            ])
        )
        self.assertFalse(page.is_valid())

    # ---------- HEAD RULES ----------

    def test_head_must_have_one_title(self):
        page = Page(
            Html([
                Head([]),
                Body([Text('body')])
            ])
        )
        self.assertFalse(page.is_valid())

    def test_head_must_not_have_multiple_titles(self):
        page = Page(
            Html([
                Head([
                    Title([Text('A')]),
                    Title([Text('B')])
                ]),
                Body([Text('body')])
            ])
        )
        self.assertFalse(page.is_valid())

    # ---------- BODY / DIV RULES ----------

    def test_body_invalid_child(self):
        page = Page(
            Html([
                Head([Title([Text('Title')])]),
                Body([Meta()])
            ])
        )
        self.assertFalse(page.is_valid())

    # ---------- TEXT-ONLY ELEMENTS ----------

    def test_h1_multiple_texts(self):
        page = Page(
            Html([
                Head([Title([Text('Title')])]),
                Body([
                    H1([Text('A'), Text('B')])
                ])
            ])
        )
        self.assertFalse(page.is_valid())

    def test_th_only_text(self):
        page = Page(
            Html([
                Head([Title([Text('Title')])]),
                Body(
                    Table([
                        Tr(
                            Th([Span(Text('invalid'))])
                        ),
                        Tr([
                            Th([Text('valid')]),
                            Th([Text('valid')])
                        ])
                    ])
                )
            ])
        )
        self.assertFalse(page.is_valid())

    # ---------- SPAN RULES ----------

    def test_span_with_text_and_p(self):
        page = Page(
            Html([
                Head([Title([Text('Title')])]),
                Body([
                    Span([
                        Text('ok'),
                        P([Text('ok')])
                    ])
                ])
            ])
        )
        self.assertTrue(page.is_valid())

    def test_span_invalid_child(self):
        page = Page(
            Html([
                Head([Title([Text('Title')])]),
                Body([
                    Span([Div()])
                ])
            ])
        )
        self.assertFalse(page.is_valid())

    # ---------- UL / OL RULES ----------

    def test_ul_without_li(self):
        page = Page(
            Html([
                Head([Title([Text('Title')])]),
                Body([Ul([])])
            ])
        )
        self.assertFalse(page.is_valid())

    def test_ul_with_non_li(self):
        page = Page(
            Html([
                Head([Title([Text('Title')])]),
                Body([
                    Ul([Li([Text('ok')]), P([Text('bad')])])
                ])
            ])
        )
        self.assertFalse(page.is_valid())

    # ---------- TABLE RULES ----------

    def test_tr_with_mixed_th_td(self):
        page = Page(
            Html([
                Head([Title([Text('Title')])]),
                Body([
                    Table([
                        Tr([
                            Th([Text('A')]),
                            Td([Text('B')])
                        ])
                    ])
                ])
            ])
        )
        self.assertFalse(page.is_valid())

    def test_table_only_tr(self):
        page = Page(
            Html([
                Head([Title([Text('Title')])]),
                Body([
                    Table([
                        Tr([Td([Text('A')])])
                    ])
                ])
            ])
        )
        self.assertTrue(page.is_valid())

    # ---------- PAGE OUTPUT ----------

    def test_print_with_doctype(self):
        page = Page(
            Html([
                Head([Title([Text('Title')])]),
                Body([Text('Hello')])
            ])
        )
        output = str(page)
        self.assertTrue(output.startswith('<!DOCTYPE html>'))

    def test_print_without_doctype(self):
        page = Page(Div([Text('Hello')]))
        output = str(page)
        self.assertFalse(output.startswith('<!DOCTYPE html>'))

    # ---------- FILE OUTPUT ----------

    def test_write_to_file_with_doctype(self):
        filename = 'test_output.html'
        page = Page(
            Html([
                Head([Title([Text('Title')])]),
                Body([Text('Hello')])
            ])
        )
        page.write_to_file(filename)

        with open(filename) as f:
            content = f.read()

        self.assertTrue(content.startswith('<!DOCTYPE html>'))
        os.remove(filename)

    def test_write_to_file_without_doctype(self):
        filename = 'test_output.html'
        page = Page(
            Body([Text('Hello')])
        )
        page.write_to_file(filename)

        with open(filename) as f:
            content = f.read()

        self.assertFalse(content.startswith('<!DOCTYPE html>'))
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
