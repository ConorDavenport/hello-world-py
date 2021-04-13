import re

def main():
  jobURL = 'https://ci.devops.microchip.com/job/FPGA_PFSOC_ES/job/mss-usb-examples/job/develop-ci-testing-report/48/'
  print(re.search(r'\d*\/$',jobURL)[0])

if __name__ == "__main__":
    main()