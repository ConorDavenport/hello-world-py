import sys
import json

class doc(object):
  # all derived classes append strings to document
  document = []

  # concatenates document to a string to be written to a html file
  def compile(self, path):
    with open(path, 'w') as f:
      f.write(''.join(self.document))

# inherits document from doc class
# with tag(div):     <div> appended to document
#   with tag(span):
#     text('blah')   blah appended to document
#                    </div> appended to document when with leaves scope
# with tag(div):
class tag(doc):
  # called at start of with statement
  def __init__(self, tag_type, clss=None, id_=None, style=None):
    self.tag_type = tag_type
    self.clss = clss
    self.id = id_
    self.style = style

  # called at start of with statement after __init__()
  # opens html tag and applies attributes
  def __enter__(self):
    if self.tag_type == 'html':
      self.document.append('<!DOCTYPE html><' + self.tag_type + '>')
    else:
      self.document.append('<' + self.tag_type)
      if self.clss != None:
        self.document.append(' class="' + self.clss + '"')
      if self.id != None:
        self.document.append(' id="' + self.id + '"')
      if self.style != None:
        self.document.append(' style="' + self.style + '"')
      self.document.append('>')

  # called when with statement leaves scope
  # closes html tag that was opened at start of with statement
  def __exit__(self, exception_type, exception_value, traceback):
    self.document.append('</' + self.tag_type + '>')

# inherits document from doc class and appends string
class text(doc):
  def __init__(self, string):
    self.document.append(string)

def main():
  # Example of data passed to script
  # [
  #   {
  #     project_name: project1, 
  #     project_configuration: config1,
  #     configuration_build_result: passed/failed,
  #     messages:"[{path:foo,message:bar}]"
  #   },
  #   {
  #     project_name: project1, 
  #     project_configuration: config2,
  #     configuration_build_result: passed/failed,
  #     messages:"[{path:foo,message:bar}]"
  #   }
  #   {
  #     project_name: project2, 
  #     project_configuration: config1,
  #     configuration_build_result: passed/failed,
  #     messages:"[{path:foo,message:bar}]"
  #   }
  # ]

  with open(sys.argv[1]) as f:
    data = json.load(f)

  # Example of projects list
  # [
  #   {
  #     project_name: project1,
  #     project_configurations: [
  #       {
  #         configuration_name: config1,
  #         configuration_build_result: passed/failed,
  #         messages:[{path:foo,message:bar}]
  #       },
  #       {
  #         configuration_name: config2,
  #         configuration_build_result: passed/failed,
  #         messages:[{path:foo,message:bar}]
  #       },
  #     ]
  #   },
  #   {
  #     project_name: project2,
  #     project_configurations: [
  #       {
  #         configuration_name: config1,
  #         configuration_build_result: passed/failed
  #         messages:[{path:foo,message:bar}]
  #       }
  #     ]
  #   }
  # ]
  # 

  # sort data from json passed to script into a list of objects
  # each object containing the name of the example project
  # and a list of the build configurations
  projects = []
  for entry in data:
    name = entry['project_name']

    duplicate = False
    for project in projects:
      if project['project_name'] == name:
        duplicate = True

    if duplicate == False:
      configs = []
      for entry in data:
        if entry['project_name'] == name:
          configs.append({'configuration_name':entry['project_configuration'],
                          'configuration_build_result':entry['configuration_build_result'],
                          'messages':json.loads(entry['messages'])})
      projects.append({'project_name':name,'project_configurations':configs})

  d = doc()
  with tag('html'):
    with tag('head'):
      with tag('style'):
        text('''h1, h2 {
                  text-align:center;
                }
                .markers {
                  margin-left: 20px;
                }
                .project {
                  margin-left: 0px;
                }
                .config {
                  margin-left: 20px;
                }
                .messageContainer {
                  margin-left: 20px;
                }
                .messagePath {
                  margin-left: 20px;
                }
                .messageInfo {
                  margin-left: 30px;
                }
                .summary {
                  margin-left: 20px;
                }
                .failed {
                  color: red;  
                      color: red;  
                  color: red;  
                }
                .passed {
                  color: green;
                }''')
    with tag('body'):
      with tag('h1'):
        text('Test Report')
      with tag('h2'):
        text('Summary')
      with tag('div'):
        text('Driver: ' + sys.argv[2])
      with tag('div'):
        passed = 0
        total = 0
        failed = []

        for entry in data:
          total += 1
          if entry['configuration_build_result'] == 'passed':
            passed += 1
          else:
            failed.append(entry)
        text('(%i/%i) build configurations successfully compiled' % (passed, total))
        
        for project in projects:
          with tag('div',clss='summary'):
            text(project['project_name'])
            for config in project['project_configurations']:
              with tag('div',clss='summary'):
                text(config['configuration_name'] + ' ')
                with tag('span',clss=config['configuration_build_result']):
                  text(config['configuration_build_result'])

      with tag('h2'):
        text('Detailed Summary')
      with tag('div',clss='project'):
        for project in projects:
          with tag('h3'):
            text('%s summary' % project['project_name'])
          for config in project['project_configurations']:
            with tag('div',clss='config'):
              text(project['project_name'] + config['configuration_name'])
              with tag('span',clss=config['configuration_build_result']):
                text(' ' + config['configuration_build_result'])
              with tag('div',clss='messageContainer'):
                for message in config['messages']:
                  with tag('div',clss='messagePath'):
                    text(message['path'])
                  with tag('div',clss='messageInfo'):
                    text(message['message'])

  # concatenate document to a single string and write to file report.html
  d.compile('report.html')

if __name__ == "__main__":
    main()