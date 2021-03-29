import sys
import json

def main():
  with open(sys.argv[1]) as f:
    data = json.load(f)

  html = open('report.html', 'w')
  html.write('<!DOCTYPE html><html><body>')
  for build in data:
    example = build['name']
    config = build['config']
    result = build['result']
    message = build['message']
    if result == 'passed':
      colour = 'green'
    elif result == 'failed':
      colour = 'red'
    html.write('''<div>
                %s%s: <span style="color:%s;">%s</span>
              </div>''' % (example, config, colour, result))

    
    html.write('<div>')
    message_data = json.loads(message)
    for entry in message_data:
      html.write('<div>%s</div>' % entry[path])
      html.write('<div>%s</div>' % entry[message])

    html.write('</div>')
  print(message)
  html.write('</body></html>')
  html.close()

if __name__ == "__main__":
    main()