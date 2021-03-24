import sys

def main():
  data_string = ""
  with open(sys.argv[1], "rb") as f:
    data = f.read()
    for character in data:
      if ((character >= b'\x20' and character <= b'\x7F') or character == b'\x0A'):
        data_string += character

  print(type(data_string))
  with open("markers", "w") as f:
    f.write(data_string)
  #   data_as_int = list(data)
  #   for i in range(len(data_as_int)):
  #     if ((data_as_int[i] < 32 or data_as_int[i] > 126) and data_as_int[i] != 10):
  #       data_as_int[i] = 0

  #   for i in range(len(data_as_int)-1, -1, -1):
  #     if (data_as_int[i] == 0):
  #       del data_as_int[i]
  
  # s = "".join([chr(c) for c in data_as_int])

  # with open("test.txt", "w") as b:
  #   b.write('this is a test')
  #   b.close()
  
  # with open("test.txt", "r") as b:
  #   print(b.read())
  #   b.close()

  # f = open("markers", "w")
  # if f.closed:
  #   print('f is not open')
  #   return -1
  # else:
  #   print('f is open')
  # f.write(s)
  # f.close()
  # if f.closed:
  #   print('f is not open')
  #   return -1
  # else:
  #   print('f is open')

if __name__ == "__main__":
  main()
