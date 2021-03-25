import sys
import re

def main():
  data_string = ""
  with open(sys.argv[1], "rb") as f:
    data = f.read()
    for character in data:
      if ((character >= b'\x20' and character <= b'\x7F') or character == b'\x0A'):
        data_string += character

  data_string_unicode = data_string.encode('utf-8')
  with open("markers", "w") as f:
    f.write(data_string_unicode)

  with open ("markers", "r") as markers:
    for line in markers.readlines():
      if ('TODO' in line and 'mpfs_hal' in line):
        matches = line.split(r'TODO ')
        todo_info = matches[0]
        file_path = re.search(r'mpfs.*?\..', todo_info)
        if 'lineNumber' in todo_info:
          line_number = re.search(r'(?<=lineNumber).*?(?=\/mpfs)', todo_info).group()
        else:
          line_number = ''
        print('TODO ' + file_path.group() + '[' + line_number + ']')
        todo_message = matches[1]
        print(todo_message)
      if ('fatal error' in line and 'mpfs' in line):
        matches = line.split(r'fatal error: ')
        error_info = matches[0]
        file_path = re.search(r'mpfs.*?\..', error_info)
        if 'lineNumber' in error_info:
          line_number = re.search(r'(?<=lineNumber).*?(?=\/mpfs)', error_info).group()
        else:
          line_number = ''
        print('ERROR ' + file_path.group() + '[' + line_number + ']')
        error_message = matches[1]
        print(error_message)

if __name__ == "__main__":
  main()