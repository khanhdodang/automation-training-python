import os
import shutil
import tempfile
import time
import unittest

from selenium import webdriver

class DownloadFile(unittest.TestCase):

  def setUp(self):
    self.download_dir = tempfile.mkdtemp()

    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.dir", self.download_dir)
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference(
      "browser.helperApps.neverAsk.saveToDisk",
      "images/jpeg, application/pdf, application/octet-stream")
    profile.set_preference("pdfjs.disabled", True)
    self.driver = webdriver.Firefox(firefox_profile=profile)

  def test_download(self):
    driver = self.driver
    driver.get("http://the-internet.herokuapp.com/download")
    download_link = driver.find_element_by_css_selector(".example a")
    download_link.click()

    time.sleep(5)  # necessary for slow download speeds

    files = os.listdir(self.download_dir)
    files = [os.path.join(self.download_dir, f)
             for f in files]  # add directory to each filename
    assert len(files) > 0, "no files were downloaded"
    assert os.path.getsize(files[0]) > 0, "downloaded file was empty"

  def tearDown(self):
    self.driver.quit()
    shutil.rmtree(self.download_dir)

if __name__ == "__main__":
  unittest.main()
