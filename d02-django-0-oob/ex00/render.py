import re
import sys


def main():
    if len(sys.argv) != 2:
        raise Exception('Usage: python3 render.py <filename.template>')

    filename = sys.argv[1]
    if not filename.endswith('.template'):
        raise Exception('Filename must end with .template')

    with open(filename) as f:
        readfile = f.read()

    body = replace_variables(readfile)
    write_output(filename, body)


def replace_variables(readfile):
    import settings

    vars_to_replace = re.findall(r'\{([a-zA-Z_][a-zA-Z0-9_]*)}', readfile)
    for var in vars_to_replace:
        try:
            replace_by = settings.__getattribute__(var)
            if not isinstance(replace_by, str):
                replace_by = str(replace_by)
                print(f'[WARNING] The variable "{{{var}}}" is not a string, it will be replaced by "{replace_by}"')
        except AttributeError:
            print(f'[WARNING] The variable "{{{var}}}" is not defined, it will be replaced by ""')
            replace_by = ''
        readfile = readfile.replace('{' + var + '}', replace_by)
    return readfile


def write_output(filename, body):
    output = filename.replace('.template', '.html')
    with open(output, 'w') as f:
        f.write(generate_html_template(body))
        print(f'Successfully created to `{output}`')


def generate_html_template(body):
    template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CV</title>
</head>
<body>
{body}
</body>
</html>'''
    return template.format(body=body)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error:', e)
        exit(1)
