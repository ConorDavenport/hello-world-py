import os
import sys

# function to return a string that can be processed by Jenkins:
# pinput is the repo name, output is a formated string that
# Jenkins can parse. src tells Jenkins that it is a src repo
# mss_x is the reformatting of the driver name for the platform
# drivers/x is the location the files should be saved to
def getDriverPath(driver):
    return {
        'mss-can-src':"src:mss_can driver:drivers/mss_can",
        'mss-envm-src':"src:mss_envm driver:drivers/mss_envm",
        'mss-ethernet-mac-src':"src:mss_ethernet_mac driver:drivers/mss_ethernet_mac",
        'mss-gpio-src':"src:mss_gpio driver:drivers/mss_gpio",
        'mss-hal-src':"src:mss_hal driver:hal",
        'mss-i2c-src':"src:mss_i2c driver:drivers/mss_i2c",
        'mss-mmc-src':"src:mss_mmc driver:drivers/mss_mmc",
        'mss-mmuart-src':"src:mss_mmuart driver:drivers/mss_mmuart",
        'mss-mpfs-hal-src':"src:mss_mpfs_hal driver:mpfs_hal",
        'mss-mpfs-sbi-src':"src:mss-mpfs-sbi:mpfs_sbi", 
        'mss-pdma-src':"src:mss_pdma driver:drivers/mss_pdma",
        'mss-qspi-src':"src:mss_qspi driver:drivers/mss_qspi",
        'mss-rtc-src':"src:mss_rtc driver:drivers/mss_rtc",
        'mss-spi-src':"src:mss_spi driver:drivers/mss_spi",
        'mss-sys-services-src':"src:mss_sys_services driver:drivers/mss_sys_services",
        'mss-timer-src':"src:mss_timer driver:drivers/mss_timer",
        'mss-usb-src':"src:mss_usb driver:drivers/mss_usb",
        'mss-watchdog-src':"src:mss_watchdog driver:drivers/mss_watchdog",
        'pf-pcie-src':"src:pf_pcie driver:drivers/pf_pcie",
        'mss-can-examples':"examples:mss-can examples:examples/mss-can",
        'mss-pdma-examples':"examples:mss-pdma examples:examples/mss-pdma",
        'mss-mmc-examples':"examples:mss-mmc examples:examples/mss-mmc",
        'mss-envm-examples':"examples:mss-envm examples:examples/mss-envm",
        'mss-ethernet-mac-examples':"examples:mss-ethernet-mac examples:examples/mss-ethernet-mac",
        'mss-gpio-examples':"examples:mss-gpio examples:examples/mss-gpio",
        'mss-i2c-examples':"examples:mss-i2c examples:examples/mss-i2c",
        'mss-mmuart-examples':"examples:mss-mmuart examples:examples/mss-mmuart",
        'mss-mpfs-hal-examples':"examples:mss-mpfs-hal examples:examples/mpfs-hal",
        'mss-qspi-examples':"examples:mss-qspi examples:examples/mss-qspi",
        'mss-rtc-examples':"examples:mss-rtc examples:examples/mss-rtc",
        'mss-spi-examples':"examples:mss-spi examples:examples/mss-spi",
        'mss-sys-services-examples':"examples:mss-sys-services examples:examples/mss-sys-services",
        'mss-timer-examples':"examples:mss-timer examples:examples/mss-timer",
        'mss-usb-examples':"examples:mss-usb examples:examples/mss-usb",
        'mss-watchdog-examples':"examples:mss-watchdog examples:examples/mss-watchdog",
        'pf-pcie-examples':"examples:pf-pcie examples:examples/pf-pcie",
        'mss-platform-config-reference-src':"config:platform_config_reference:platform_config_reference",
        'polarfire-soc-configuration-generator':"config:soc_config_generator:soc_config_generator",
        'h2':"==============================================================================",
    }[driver]

def main():
    return getDriverPath(sys.argv[1])


if __name__ =='__main__':
    main()