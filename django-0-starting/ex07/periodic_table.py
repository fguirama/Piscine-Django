class ChemicalElement:
    def __init__(self, line):
        self.electron: str = ''
        self.position: int = 0

        name, attr = line.split('=')
        self.name = name.strip()

        attrs = attr.split(',')
        for attr in attrs:
            k, v = attr.split(':')
            setattr(self, k.strip(), v.strip())
        self.total_electron = sum(map(int, self.electron.split(' ')))
        self.electron_plural = 's' if self.total_electron > 1 else ''
        self.position = int(self.position)


def main():
    body = '<tr>\n'
    elements = []
    try:
        with open('periodic_table.txt') as f:
            read_file = f.read()
            for line in read_file.splitlines():
                elements.append(ChemicalElement(line))
    except FileNotFoundError as err:
        print(err)
        exit(1)
    p = 0
    for element in elements:
        if element.position == 0 and element.total_electron > 1:
            body += '</tr>\n<tr>\n'.format(element.name)
            p = 0
        if element.position != p:
            body += f'<td colspan="{element.position - p}" class="empty-cells"></td>\n'
            p = element.position
        body += generate_element_cell(element)
        p += 1
    body += '</tr>\n'
    try:
        with open('periodic_table.html', 'w') as f:
            html_txt = generate_html_template(body)
            f.write(html_txt)
    except PermissionError as err:
        print(err)
        exit(1)
    print('Successfully generated periodic table `periodic_table.html`.')


def generate_element_cell(element):
    template = '''<td style="border: 1px solid black; padding:10px">
    <h4>{name}</h4>
    <ul>
        <li>No {number}</li>
        <li>{small}</li>
        <li>{molar}</li>
        <li>{total_electron} electron{electron_plural}</li>
    </ul>
</td>
'''
    return template.format_map(element.__dict__)


def generate_html_template(table):
    table_header = '\n'.join([f'<th>{i + 1}</th>' for i in range(18)])
    template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Periodic Table</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <table>
        <thead>
            <tr>
{table_header}
            </tr>
        </thead>
        <tbody>
{table}
        </tbody>
    </table>
</body>
</html>'''
    return template.format(table_header=table_header, table=table)


if __name__ == '__main__':
    main()
