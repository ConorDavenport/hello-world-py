import sys
import re
import json

# get the file path for the todo/error
def getFilePath(prev_file_path, info):
  file_path = prev_file_path
  search_file_path = re.search(r'mpfs.*?\..', info)
  if search_file_path != None:
    file_path = search_file_path.group()
    return file_path
  else:
    # consecutive todos/errors from the same file don't contain
    # the file path in the log file, return the file path
    # of the previously processed todo/error
    return prev_file_path

def main():
  sys.stdout.flush()
  # search json file for the name of the repo currently being
  # tested in the pipeline. Get the name of the corresponding
  # entry in platform
  platform_entry = ""
  with open("bitbucket_project_description.json") as f:
    data = json.load(f)
    repositories = data["repositories"]
    for repo in repositories:
      if repo["name"] == sys.argv[2]:
        platform_entry = repo["platform_entry"]

  clean_data = []
  with open(sys.argv[1], "rb") as f:
    data = f.readlines()
    for line in data:
      # remove illegal characters
      line_decoded = line.decode('utf-8','replace')
      # remove characers that aren't alphanumeric, certain punctuation
      # or space
      clean_line = re.sub(r'[^A-Za-z0-9/\-. ]+', '', line_decoded)
      print(clean_line)
      clean_data.append(clean_line)

  with open("markers.json", "w") as f:
    formatted_data = []
    prev_file_path = ''
    for line in clean_data:
      # filter out only todos that are revelant to this repo
      if ('TODO' in line and platform_entry in line):
        matches = line.split(r'TODO ')

        todo_info = matches[0]

        file_path = getFilePath(prev_file_path, todo_info)
        if file_path != prev_file_path: prev_file_path = file_path

        line_number = ''
        search_line_number = re.search(r'(?<=lineNumber).*?(?=\/mpfs)', todo_info)
        if search_line_number != None:
          line_number = search_line_number.group()
        else:
          search_line_number = re.search(r'(?<=lineNumber).*?(?=source)', todo_info)
          if search_line_number != None:
            line_number = search_line_number.group()

        todo_path = 'TODO ' + file_path + '[' + line_number + ']'
        print(todo_path)

        # remove trailing 'priority' from todo message
        todo_message = matches[1]
        if re.search(r'priority$', todo_message) != None:
          todo_message = re.split(r'priority$', todo_message)[0]

        print(todo_message)

        formatted_data.append({'path':todo_path, 'message':todo_message})

      if ('fatal error' in line):
        matches = line.split(r'fatal error: ')

        error_info = matches[0]

        file_path = getFilePath(prev_file_path, error_info)
        if file_path != prev_file_path: prev_file_path = file_path

        line_number = ''
        search_line_number = re.search(r'(?<=lineNumber).*?(?=\/mpfs)', error_info)
        if search_line_number != None:
          line_number = search_line_number.group()

        error_path = 'ERROR ' + file_path + '[' + line_number + ']'
        print(error_path)

        error_message = matches[1]
        print(error_message)

        formatted_data.append({'path':error_path, 'message':error_message})

    json.dump(clean_data, f)

if __name__ == "__main__":
  main()