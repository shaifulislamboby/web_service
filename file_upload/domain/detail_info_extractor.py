from dataclasses import dataclass
from pathlib import Path
from collections import Counter


@dataclass
class FileDetail:
    """
    for ensuring the data integrity
    """
    line_content: str
    line_length: int
    line_number: int
    most_occurred_letter: str


def check_txt_file(file) -> bool:
    """
    This function will check if the file is txt file or not.
    If any file other than txt format is uploaded than, that
    will be saved in the Document model, and the file will
    remain in our media, but we will not parse it.
    :param file:
    :return:
    """
    try:
        if Path(file.name).suffix == '.txt':
            return True
        return False
    except Exception as error:
        print(error)
        return False


def create_file_content_list(file) -> list:
    """
    This function will ignore the lines that are empty or '\r\n'
    :param file:
    :return:
    """
    file_content_list = []
    if check_txt_file(file):
        try:
            lines = file.readlines()
            for index, line in enumerate(lines):
                """As data is being transmitted in byte, to 
                    convert it to string we need to decode,strip has been used for removing newlines """
                line = line.decode('utf-8').strip()
                if len(line) > 0:
                    file_content_list.append(add_line_related_elements_in_dict(index=index, line=line))

        except Exception as error:
            """Here logging can be used, for trace """
            print(error)
        finally:
            return file_content_list


def add_line_related_elements_in_dict(index: int, line: str) -> FileDetail:
    """
    This method will create FileDetail instance and return
    :param index:
    :param line:
    :return:
    """
    return FileDetail(line_content=line,
                      line_length=len(line),
                      line_number=index,
                      most_occurred_letter=find_most_occurred_letter(line=line))


def find_most_occurred_letter(line: str) -> str:
    """
    Return the max occurred letter.
    if all occurs equal number of time then the first letter
    :param line:
    :return:
    """
    word_dict = Counter(line)
    return max(word_dict, key=word_dict.get)
