# I. Installation
+ Python 3
+ Browsers Firefox, Chrome, PhantomJS and IE

# II. Download drivers

| Browser          | Supported OS        		| Maintained by   | Download |
| :---             |    :----:           		|          ---:   |  ---:    |
| Chromium/Chrome  | Windows/macOS/Linux 		| Google          | [Download](https://chromedriver.storage.googleapis.com/index.html) |
| Firefox          | Windows/macOS/Linux 		| Mozilla         | [Download](https://github.com/mozilla/geckodriver/releases) |
| Edge             | Windows 10          		| Microsoft       | [Download](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) |
| Internet Explorer| Windows             		| Selenium Project| [Download](https://selenium-release.storage.googleapis.com/index.html) |
| Safari           | macOS El Capitan and newer | Apple 		  | Built in |
| Opera            | Windows/macOS/Linux 		| Opera			  | [Download](https://github.com/operasoftware/operachromiumdriver/releases) |


# III. How to run tests
+ python testcase.py
+ python testsuite.py
+ python testsuite_html_report.py

### Run with variable from Terminal
+ `export BROWSER=firefox` (for Mac)
+ `set BROWSER=firefox` (for Windows)

# Start Selenium Server Standalone
```
java -jar <path>/Drivers/selenium-server-standalone-<version>.jar 
```
