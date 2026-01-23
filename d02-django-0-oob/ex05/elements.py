from elem import Elem, Text


class ElemText(Elem):
    def __init__(self, tag, attr=None, content=None):
        if type(content) is str:
            content = Text(content)

        if type(content) is list:
            for i, c in enumerate(content):
                if isinstance(c, str):
                    content[i] = Text(c)
        super().__init__(tag, attr, content)


class Html(Elem):
    def __init__(self, content=None, **attr):
        super().__init__('html', attr, content)


class Head(Elem):
    def __init__(self, content=None, **attr):
        super().__init__('head', attr, content)


class Body(Elem):
    def __init__(self, content=None, **attr):
        super().__init__('body', attr, content)


class Title(ElemText):
    def __init__(self, content, **attr):
        super().__init__('title', attr, content)


class Meta(Elem):
    def __init__(self, **attr):
        super().__init__('meta', attr, tag_type='simple')


class Img(Elem):
    def __init__(self, **attr):
        super().__init__('img', attr, tag_type='simple')


class Table(Elem):
    def __init__(self, content=None, **attr):
        super().__init__('table', attr, content)


class Th(ElemText):
    def __init__(self, content=None, **attr):
        super().__init__('th', attr, content)


class Tr(Elem):
    def __init__(self, content=None, **attr):
        super().__init__('tr', attr, content)


class Td(Elem):
    def __init__(self, content=None, **attr):
        super().__init__('td', attr, content)


class Ul(Elem):
    def __init__(self, content=None, **attr):
        super().__init__('ul', attr, content)


class Ol(Elem):
    def __init__(self, content=None, **attr):
        super().__init__('ol', attr, content)


class Li(ElemText):
    def __init__(self, content=None, **attr):
        super().__init__('li', attr, content)


class H1(ElemText):
    def __init__(self, content=None, **attr):
        super().__init__('h1', attr, content)


class H2(ElemText):
    def __init__(self, content=None, **attr):
        super().__init__('h2', attr, content)


class P(ElemText):
    def __init__(self, content=None, **attr):
        super().__init__('p', attr, content)


class Div(Elem):
    def __init__(self, content=None, **attr):
        super().__init__(attr=attr, content=content)


class Span(ElemText):
    def __init__(self, content=None, **attr):
        super().__init__('span', attr, content)


class Hr(Elem):
    def __init__(self, **attr):
        super().__init__('hr', attr, tag_type='simple')


class Br(Elem):
    def __init__(self, **attr):
        super().__init__('br', attr, tag_type='simple')


if __name__ == '__main__':
    print(Html([Head(), Body()]))

    print('\n-------------------------\n')

    print(Html([
        Head(
            Title('"Hello ground!"')
        ),
        Body([
            H1('"Oh no, not again!"'),
            Img(src='http://i.imgur.com/pfp3T.jpg')
        ]),
    ]))

    print('\n-------------------------\n')

    # ⚠️ IA Use -> here, AI was used to generate an HTML page with all the tags and features. And then I translated the HTML page into Python code
    print(Html([
        Head([
            Title('HTML Test Page'),
            Meta(charset='UTF-8'),
            Meta(name='description', content='HTML test page using all required tags'),
        ]),
        Body([
            H1('HTML Tags Test'),
            Hr(),

            H2('Paragraph and Inline Elements'),
            P([
                'This is a paragraph with an',
                Span('inline span', style='font-style: italic'),
                'inside it.'
            ]),
            Br(),

            H2('Image'),
            Img(src='http://i.imgur.com/pfp3T.jpg', alt='Test image'),
            Br(),
            Br(),

            H2('Lists'),
            Div([
                P('Unordered list:'),
                Ul([
                    Li('Item one'),
                    Li('Item two'),
                    Li('Item three'),
                ]),

                P('Ordered list:'),
                Ol([
                    Li('First'),
                    Li('Second'),
                    Li('Third'),
                ])
            ]),

            H2('Table'),
            Table([
                Tr([
                    Th('Name'),
                    Th('Age'),
                    Th('Role'),
                ]),
                Tr([
                    Th('Alice'),
                    Th('30'),
                    Th('Developer'),
                ]),
                Tr([
                    Th('Bob'),
                    Th('25'),
                    Th('Designer'),
                ]),
            ], border='1'),
            Br(),

            H2('Layout'),
            Div(
                P([
                    'This is',
                    Span('content', style='font-weight: bold'),
                    'inside a div element.'
                ])
            ),

            Hr(),

            P('End of the test page.'),
        ]),
    ]))
