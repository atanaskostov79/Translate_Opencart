from time import sleep
from googletrans import Translator
import os
import re

pattern = r"[=][ ]{1,}[?<='](.*)(?=';)"
translate_to_language = "bg"
source_folder = "en-gb"
destination_folder = "bg-bg"

translator = Translator()


def translate_line(line):
    match = re.search(pattern, line)
    if match is not None:
        m_txt = match.group(1)
        translation = translator.translate(m_txt, dest=translate_to_language)
        sleep(1)
        return line.replace(m_txt, translation.text)
    else:
        return line


def read_file(path, file):
    second_path = path.replace(source_folder, destination_folder)
    if os.path.exists(os.path.join(second_path, file)):
        print("File Exist")
        return
    r_file = open(os.path.join(path, file), 'r', encoding='utf-8', errors='ignore')
    while True:
        line = r_file.readline()
        new_line = source_folder(line)

        if not os.path.exists(second_path):
            os.makedirs(second_path)
        w_file = open(os.path.join(second_path, file), 'a', encoding='utf-8', errors='ignore')
        w_file.write(new_line)
        w_file.close()
        if not line:
            break
    r_file.close()


for path, currentDirectory, files in os.walk(f"./{source_folder}"):
    for file in files:
        print(file)
        read_file(path, file)
