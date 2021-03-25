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
        matches = line.split(r'TODO')
        todo_info = matches[0]
        print(todo_info)
        file_path = re.match(r'mpfs.*(?=org)', todo_info)
        print(file_path)
        todo_message = matches[1]
        print(todo_message)
      if ('fatal error' in line):
        print(line)

if __name__ == "__main__":
  main()