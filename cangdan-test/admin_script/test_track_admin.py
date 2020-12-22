import time

from other.Commonlib import Commonshare
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

from other.other_script import Date_add_clear


class TestTrackAdmin(Date_add_clear):
    """预备舱单申报"""


