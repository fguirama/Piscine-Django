#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    @staticmethod
    def escape(s):
        """
        Replace special characters "&", "<" and ">" to HTML-safe sequences.
        If the optional flag quote is true (the default), the quotation mark
        characters, both double quote (") and single quote (') characters are also
        translated.
        """
        s = s.replace("&", "&amp;")  # Must be done first!
        s = s.replace("<", "&lt;")
        s = s.replace(">", "&gt;")
        s = s.replace('"', "&quot;")
        s = s.replace('\'', "&#x27;")
        return s

    @staticmethod
    def unscape(s):
        """
        The reverse of escape().
        """
        s = s.replace("&lt;", "<")
        s = s.replace("&gt;", ">")
        s = s.replace("&quot;", '"')
        s = s.replace("&#x27;", '\'')
        s = s.replace("&amp;", "&")  # Must be done last!
        return s

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return Text.escape(super().__str__()).replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """

    class ValidationError(Exception):
        def __init__(self, msg_error=None):
            if msg_error is None:
                msg_error = 'Validation Error: content must be of type Elem, Text or list of both.'
            super().__init__(msg_error)

    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        if tag_type not in ('double', 'simple'):
            raise Elem.ValidationError('Wrong tag_type value, must be "double" or "simple".')
        self.tag_type = tag_type
        self.attr = attr if attr is not None else {}
        self.content = []

        if content is not None:
            self.add_content(content)

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        attrs = self.__make_attr()
        result = f'<{self.tag}{attrs}'
        if self.tag_type == 'double':
            content = self.__make_content()
            if content:
                content = content.replace('\n', '\n  ', content.count('\n') - 1)
            result += f'>{content}</{self.tag}>'
        elif self.tag_type == 'simple':
            result += f' />'
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            if type(elem) is Text:
                elem = Text.unscape(elem)
            result += f'{elem}\n'
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    page = Elem('html', content=[
        Elem('head', content=[
            Elem('title', content=Text('"Hello ground!"')),
        ]),
        Elem('body', content=[
            Elem('h1', content=Text('"Oh no, not again!"')),
            Elem('img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
        ]),
    ])
    print(page)
