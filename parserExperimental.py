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

  prev_file_path = ''
  with open ("markers", "r") as markers:
    for line in markers.readlines():
      if ('TODO' in line):
        matches = line.split(r'TODO ')

        todo_info = matches[0]

        file_path = prev_file_path
        search_file_path = re.search(r'mpfs.*?\..', todo_info)
        if search_file_path != None:
          file_path = search_file_path.group()
          prev_file_path = file_path

        line_number = ''
        search_line_number = re.search(r'(?<=lineNumber).*?(?=\/mpfs)', todo_info)
        if search_line_number != None:
          line_number = search_line_number.group()
        else:
          search_line_number = re.search(r'(?<=lineNumber).*?(?=source)', todo_info)
          if search_line_number != None:
            line_number = search_line_number.group()

        print('TODO ' + file_path + '[' + line_number + ']')

        todo_message = matches[1]
        if re.search(r'priority$', todo_message) != None:
          todo_message = re.split(r'priority$', todo_message)[0]

        print(todo_message)
      if ('fatal error' in line):
        matches = line.split(r'fatal error: ')

        error_info = matches[0]

        file_path = prev_file_path
        search_file_path = re.search(r'mpfs.*?\..', error_info)
        if search_file_path != None:
          file_path = search_file_path.group()
          prev_file_path = file_path

        line_number = ''
        search_line_number = re.search(r'(?<=lineNumber).*?(?=\/mpfs)', error_info)
        if search_line_number != None:
          line_number = search_line_number.group()

        print('ERROR ' + file_path + '[' + line_number + ']')

        error_message = matches[1]
        print(error_message)

if __name__ == "__main__":
  main()