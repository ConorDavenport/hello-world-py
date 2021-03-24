import sys

def main():
  dataString = ""
  with open(".markers", "rb") as f:
    data = f.read()
    data_as_int = list(data)
    for i in range(len(data_as_int)):
      if ((data_as_int[i] < 32 or data_as_int[i] > 126) and data_as_int[i] != 10):
        data_as_int[i] = 0
    
    for i in range(len(data_as_int)-1, -1, -1):
      if (data_as_int[i] == 0):
        del data_as_int[i]

    s = "".join([chr(c) for c in data_as_int])

    with open("markers", "w") as f:
      f.write(s)

if __name__ == "__main__":
  main()
