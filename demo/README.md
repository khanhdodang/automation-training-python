# Automation Python Search page

**Test case:** Verify that the response fetched for a particular keyword is correct and related to the keyword, containing links to the particular webpage.

### **Steps:**

1. Launch the Firefox or Chrome browser
1. Enter the URL [python.org](http://www.python.org) and open
1. Enter "`python`" text into the **Search** textbox
1. Press **Enter** key

**Expected:** The results that are returned contain the search keyword.


**Installations:**

1. brew install operadriver - https://www.npmjs.com/package/operadriver
2. brew install chromedriver - https://formulae.brew.sh/cask/chromedriver
3. brew install geckodriver - https://formulae.brew.sh/formula/geckodriver
4. https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari

Install pip & selenium
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
pip2 install selenium
```
