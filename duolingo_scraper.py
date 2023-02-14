# Selenium imports.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException

# Other imports.
import time
from keys import username, password
# Class for learning OOP


class Duolingo:
    def __init__(self):
        self.driver = webdriver.Chrome()# Selenium imports.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException

# Other imports.
import time
from keys import username, password
# Class for learning OOP


class Duolingo:
    def __init__(self):
        self.driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()

        # Comment the line below to switch OFF incognito mode.
        chrome_options.add_argument("--incognito")
        # Uncomment the line below to not open a browser window.
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def closeBrowser(self):
        self.driver.close()

    def loginDuo(self, username, password):
        driver = self.driver
        driver.get("https://www.duolingo.com/?isLoggingIn=true")
        time.sleep(3)

        # Hardcoded XPaths.
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/button').click()
        time.sleep(1)

        # Insertinf credentials.
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/div/form/div[1]/div[1]/div[1]/label/div/input').send_keys(username)
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/div/form/div[1]/div[1]/div[2]/label/div[1]/input').send_keys(password)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[1]/button').click()
        time.sleep(5)

    def autoXP(self, sents):
        driver = self.driver

        try:
            driver.get("https://www.duolingo.com/skill/de/Flirting/practice")
            time.sleep(10)
            try:
                driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/button").click()
                time.sleep(1)
            except:
                pass
            while True:
                words = driver.find_elements_by_xpath("//button[@data-test='challenge-tap-token']")
                word_text = []
                for i in words:
                    word_text.append(i.text)

                for i in sents:
                    if sorted(word_text) == sorted(i):
                        for a in i:
                            for b in words:
                                if a == b.text:
                                    b.click()
                                    words.remove(b)
                                    break
                        break

                driver.find_element_by_xpath("//button[@data-test='player-next']").click()
                time.sleep(1)
                driver.find_element_by_xpath("//button[@data-test='player-next']").click()
                time.sleep(2)

        # Debugging code.

        # except:
        #     pass
        except ElementClickInterceptedException:
            print("Done")
        except NoSuchElementException:
            print("Ok")
        except StaleElementReferenceException:
            print("Ok")


Duo = Duolingo()
Duo.loginDuo(username, password)

# Duolingo data
idiom_sents = [
    ['It', 'is', 'raining', 'cats', 'and', 'dogs'],
    ['Chin', 'up'],
    ['Out', 'of', 'sight', ',', 'out', 'of', 'mind'],
    ['Every', 'dog', 'has', 'its', 'day'],
    ['The', 'pen', 'is', 'mightier', 'than', 'the', 'sword'],
    ['He', 'is', 'known', 'all', 'over', 'town'],
    ['That', 'is', 'yesterday', '\'s', 'news'],
    ['Laughter', 'is', 'the', 'best', 'medicine'],
    ['I', '’ll', 'keep', 'my', 'fingers', 'crossed', 'for', 'you'],
    ['German', 'is', 'hard'],
    ['Too', 'many', 'cooks', 'spoil', 'the', 'broth'],
    ['The', 'straw', 'that', 'breaks', 'the', 'camel', '\'s', 'back'],
    ['Practice', 'makes', 'perfect'],
    ['All', '\'s', 'well', 'that', 'ends', 'well']
]

flirt_sents = [
    ["I", "think", "you", "are", "nice"],
    ["I", "am", "new", "here", ",", "and", "you"],
    ["I", "would", "like", "to", "get", "to", "know", "you", "better"],
    ["I", "think", "you", "'re", "cute"],
    ["Do", "you", "want", "to", "dance"],
    ["The", "coffee", "is", "on", "me"],
    ["You", "look", "like", "my", "next", "girlfriend"],
    ["May", "I", "kiss", "you"],
    ["Your", "eyes", "are", "like", "stars"],
    ["May", "I", "invite", "you", "to", "dinner"],
    ["Can", "I", "call", "you"],
    ["You", "are", "funny"],
    ["You", "are", "smart"],
    ["Can", "I", "order", "you", "a", "drink"],
    ["I", "love", "you"],
    ["I", "like", "you"],
    ["You", "can", "dance", "well"],
    ["I", "have", "fallen", "in", "love", "with", "you"],
    ["Do", "you", "want", "to", "go", "out", "with", "me"],

]

while True:
    Duo.autoXP(flirt_sents)

        chrome_options = webdriver.ChromeOptions()

        # Comment the line below to switch OFF incognito mode.
        chrome_options.add_argument("--incognito")
        # Uncomment the line below to not open a browser window.
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def closeBrowser(self):
        self.driver.close()

    def loginDuo(self, username, password):
        driver = self.driver
        driver.get("https://www.duolingo.com/?isLoggingIn=true")
        time.sleep(3)

        # Hardcoded XPaths.
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/button').click()
        time.sleep(1)

        # Insertinf credentials.
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/div/form/div[1]/div[1]/div[1]/label/div/input').send_keys(username)
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div/div/form/div[1]/div[1]/div[2]/label/div[1]/input').send_keys(password)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[1]/button').click()
        time.sleep(5)

    def autoXP(self, sents):
        driver = self.driver

        try:
            driver.get("https://www.duolingo.com/skill/de/Flirting/practice")
            time.sleep(10)
            try:
                driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/div/div/div[2]/div/div/div/button").click()
                time.sleep(1)
            except:
                pass
            while True:
                words = driver.find_elements_by_xpath("//button[@data-test='challenge-tap-token']")
                word_text = []
                for i in words:
                    word_text.append(i.text)

                for i in sents:
                    if sorted(word_text) == sorted(i):
                        for a in i:
                            for b in words:
                                if a == b.text:
                                    b.click()
                                    words.remove(b)
                                    break
                        break

                driver.find_element_by_xpath("//button[@data-test='player-next']").click()
                time.sleep(1)
                driver.find_element_by_xpath("//button[@data-test='player-next']").click()
                time.sleep(2)

        # Debugging code.

        # except:
        #     pass
        except ElementClickInterceptedException:
            print("Done")
        except NoSuchElementException:
            print("Ok")
        except StaleElementReferenceException:
            print("Ok")


Duo = Duolingo()
Duo.loginDuo(username, password)

# Duolingo data
idiom_sents = [
    ['It', 'is', 'raining', 'cats', 'and', 'dogs'],
    ['Chin', 'up'],
    ['Out', 'of', 'sight', ',', 'out', 'of', 'mind'],
    ['Every', 'dog', 'has', 'its', 'day'],
    ['The', 'pen', 'is', 'mightier', 'than', 'the', 'sword'],
    ['He', 'is', 'known', 'all', 'over', 'town'],
    ['That', 'is', 'yesterday', '\'s', 'news'],
    ['Laughter', 'is', 'the', 'best', 'medicine'],
    ['I', '’ll', 'keep', 'my', 'fingers', 'crossed', 'for', 'you'],
    ['German', 'is', 'hard'],
    ['Too', 'many', 'cooks', 'spoil', 'the', 'broth'],
    ['The', 'straw', 'that', 'breaks', 'the', 'camel', '\'s', 'back'],
    ['Practice', 'makes', 'perfect'],
    ['All', '\'s', 'well', 'that', 'ends', 'well']
]

flirt_sents = [
    ["I", "think", "you", "are", "nice"],
    ["I", "am", "new", "here", ",", "and", "you"],
    ["I", "would", "like", "to", "get", "to", "know", "you", "better"],
    ["I", "think", "you", "'re", "cute"],
    ["Do", "you", "want", "to", "dance"],
    ["The", "coffee", "is", "on", "me"],
    ["You", "look", "like", "my", "next", "girlfriend"],
    ["May", "I", "kiss", "you"],
    ["Your", "eyes", "are", "like", "stars"],
    ["May", "I", "invite", "you", "to", "dinner"],
    ["Can", "I", "call", "you"],
    ["You", "are", "funny"],
    ["You", "are", "smart"],
    ["Can", "I", "order", "you", "a", "drink"],
    ["I", "love", "you"],
    ["I", "like", "you"],
    ["You", "can", "dance", "well"],
    ["I", "have", "fallen", "in", "love", "with", "you"],
    ["Do", "you", "want", "to", "go", "out", "with", "me"],

]

while True:
    Duo.autoXP(flirt_sents)
