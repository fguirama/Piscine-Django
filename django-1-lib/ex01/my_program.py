from local_lib import path


def main():
    file_path = path.Path('my_folder/test_file.txt')
    file_path.parent.mkdir()
    file_path.write_text('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
    content_file = file_path.read_text()
    print(content_file)


if __name__ == '__main__':
    main()
