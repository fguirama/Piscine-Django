from elem import Text
from elements import *


class Page:
    def __init__(self, _page):
        if not isinstance(_page, Elem):
            raise TypeError
        self.page = _page

    def __str__(self):
        doctype = ''
        if self.page.tag == 'html':
            doctype = '<!DOCTYPE html>\n'
        return f'{doctype}{self.page}'

    def is_valid(self):
        try:
            Page.__check_every_node(self.page, Html)
        except ValueError:
            return False

        if self.page.content[0].tag != 'head' or self.page.content[1].tag != 'body':
            return False

        return True

    @staticmethod
    def __check_every_node(checked_node, valid_class):
        if not isinstance(checked_node, valid_class):
            raise ValueError
        if isinstance(checked_node, Text):
            return

        require_len = None
        min_len = None
        if checked_node.tag == 'html':
            valid_child_class = (Head, Body)
            require_len = 2
        elif checked_node.tag == 'head':
            valid_child_class = Title
            require_len = 1
        elif checked_node.tag in ('body', 'div'):
            valid_child_class = (H1, H2, Div, Table, Ul, Ol, Span, Text)
        elif checked_node.tag == 'p':
            valid_child_class = Text
        elif checked_node.tag == 'span':
            valid_child_class = (Text, P)
        elif checked_node.tag in ('ul', 'ol'):
            valid_child_class = Li
            min_len = 1
        elif checked_node.tag == 'tr':
            valid_child_class = (Th, Td)
            if isinstance(checked_node.content, list) and len(checked_node.content) > 0:
                first_tag = checked_node.content[0].tag
                if first_tag == 'th':
                    valid_child_class = Th
                elif first_tag == 'td':
                    valid_child_class = Td
            min_len = 1
        elif checked_node.tag == 'table':
            valid_child_class = Tr
        else:
            valid_child_class = Text
            require_len = 1

        if isinstance(checked_node.content, list):
            if (require_len is not None and len(checked_node.content) != require_len) or (min_len is not None and len(checked_node.content) < min_len):
                raise ValueError

            for node in checked_node.content:
                Page.__check_every_node(node, valid_child_class)
        else:
            if min_len > 1 or (require_len is not None and require_len != 1):
                raise ValueError

            Page.__check_every_node(checked_node.content, valid_child_class)

    def write_to_file(self, _filename):
        try:
            with open(_filename, 'w') as _f:
                _f.write(str(self))
                print('Successfully wrote to', _filename)
        except PermissionError as err:
            print(err)


if __name__ == '__main__':
    # ⚠️ IA Use -> here, AI was used to generate some test. I need to add more test to be sure

    # Valid_minimal_html
    page = Page(
        Html([
            Head([Title([Text('Hello')])]),
            Body([Text('World')])
        ])
    )
    assert page.is_valid() is True

    # Valid_complex_page
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
    assert page.is_valid() is True

    # ---------- INVALID TAG ---------- #
    # Invalid_unknown_tag
    class Foo(Elem):
        pass

    page = Page(Foo([Text('invalid')]))
    assert page.is_valid() is False

    # Invalid_type
    try:
        Page('invalid string')
        assert False
    except TypeError:
        assert True

    # ---------- HTML STRUCTURE ---------- #
    # Html_must_have_head_then_body
    page = Page(
        Html([
            Body([Text('body')]),
            Head([Title([Text('title')])])
        ])
    )
    assert page.is_valid() is False

    # Html_missing_head
    page = Page(
        Html([
            Body([Text('body')])
        ])
    )
    assert page.is_valid() is False

    page = Page(
        Html(Body([Text('body')]))
    )
    assert page.is_valid() is False

    # Html_have_two_body
    page = Page(
        Html([
            Body([Text('body')]),
            Body([Text('body')])
        ])
    )
    assert page.is_valid() is False

    # ---------- HEAD RULES ---------- #
    # Head_must_have_one_title
    page = Page(
        Html([
            Head([]),
            Body([Text('body')])
        ])
    )
    assert page.is_valid() is False

    # Head_must_not_have_multiple_titles
    page = Page(
        Html([
            Head([
                Title([Text('A')]),
                Title([Text('B')])
            ]),
            Body([Text('body')])
        ])
    )
    assert page.is_valid() is False

    # ---------- BODY / DIV RULES ---------- #
    # Body_invalid_child
    page = Page(
        Html([
            Head([Title([Text('Title')])]),
            Body([Meta()])
        ])
    )
    assert page.is_valid() is False

    # ---------- TEXT-ONLY ELEMENTS ---------- #
    # H1_multiple_texts
    page = Page(
        Html([
            Head([Title([Text('Title')])]),
            Body([
                H1([Text('A'), Text('B')])
            ])
        ])
    )
    assert page.is_valid() is False

    # Th_only_text
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
    assert page.is_valid() is False

    # ---------- SPAN RULES ---------- #
    # Span_with_text_and_p
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
    assert page.is_valid() is True

    # Span_invalid_child
    page = Page(
        Html([
            Head([Title([Text('Title')])]),
            Body([
                Span([Div()])
            ])
        ])
    )
    assert page.is_valid() is False

    # ---------- UL / OL RULES ---------- #
    # Ul_without_li
    page = Page(
        Html([
            Head([Title([Text('Title')])]),
            Body([Ul([])])
        ])
    )
    assert page.is_valid() is False

    # Ul_with_non_li
    page = Page(
        Html([
            Head([Title([Text('Title')])]),
            Body([
                Ul([Li([Text('ok')]), P([Text('bad')])])
            ])
        ])
    )
    assert page.is_valid() is False

    # ---------- TABLE RULES ---------- #
    # Tr_with_mixed_th_td
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
    assert page.is_valid() is False

    # Table_only_tr
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
    assert page.is_valid() is True

    # ---------- PAGE OUTPUT ---------- #
    # Print_with_doctype
    page = Page(
        Html([
            Head([Title([Text('Title')])]),
            Body([Text('Hello')])
        ])
    )
    output = str(page)
    assert output.startswith('<!DOCTYPE html>')

    # Print_without_doctype
    page = Page(Div([Text('Hello')]))
    output = str(page)
    assert not output.startswith('<!DOCTYPE html>')

    # ---------- FILE OUTPUT ---------- #
    # Write_to_file_with_doctype
    filename = 'test_output1.html'
    page = Page(
        Html([
            Head([Title([Text('Title')])]),
            Body([Text('Hello')])
        ])
    )
    page.write_to_file(filename)
    with open(filename) as f:
        content = f.read()
    assert content.startswith('<!DOCTYPE html>')

    # Write_to_file_without_doctype
    filename = 'test_output2.html'
    page = Page(
        Body([Text('Hello')])
    )
    page.write_to_file(filename)
    with open(filename) as f:
        content = f.read()
    assert not content.startswith('<!DOCTYPE html>')

    print("✅ All tests passed successfully")
