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
      if (('TODO' in line or 'fatal error' in line) and 'mpfs_hal' in line):
        if 'TODO' in line:
          matches = line.split(r'TODO')
        elif 'fatal error' in line:
          matches = line.split(r'fatal error')

        message_info = matches[0]
        file_path = re.search(r'mpfs.*(?=org)', message_info)
        line_number = re.search(r'(?<=lineNumber).*?(?=\/mpfs)', message_info).group()
        print(file_path.group() + '[' + line_number + ']')
        message = matches[1]
        print(message)

if __name__ == "__main__":
  main()