from django.test import Client, TestCase
from faker import Faker
import os
import random
import hashlib
import urllib3
from filmapp_main.settings import PATH_2_DRIVER
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class FilmViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_post_get(self):
        N = 10
        http = urllib3.PoolManager()
        
        path_to_covers = "../Обложки/"
        listdir = os.listdir(path_to_covers)
        N_covers = len(listdir)
        check_sums = [None] * N_covers
        for i in range(N_covers):
            check_sums[i] = hashlib.md5(open(path_to_covers + listdir[i], "rb").read()).hexdigest()
        
        field_names = ["name", "original_name", "year"]
        
        fake = Faker()
        fake_ru = Faker(locale="Ru_ru")
        
        for i in range(N):
            data = {"name": fake_ru.sentence(nb_words=random.randint(1, 10), ext_word_list=None),
                    "original_name": fake.sentence(nb_words=random.randint(1, 10), ext_word_list=None),
                    "year": random.randint(1900, 2022),
                    "cover": open(path_to_covers + listdir[i % N_covers], "rb")}
            
            response = self.client.post("/api/film/", data)
            content = response.data
            self.assertTrue("status" in content)
            self.assertTrue("id" in content)
            self.assertTrue(content["status"] == "OK")
            film_id = content["id"]
            
            response = self.client.get("/api/film/" + str(film_id) + "/")
            content = response.data
            self.assertTrue("id" in content)
            for field in field_names:
                self.assertTrue(field in content)
                self.assertTrue(content[field] == data[field])
            self.assertTrue("cover" in content)
            response = http.request("GET", content["cover"])
            check_sum2 = hashlib.md5(response.data).hexdigest()
            self.assertTrue(check_sums[i % N_covers] == check_sum2)
        
    def tearDown(self):
        pass
    
class DirectorViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_post_get(self):
        N = 10
        
        field_names = ["name", "year"]
        
        fake_ru = Faker(locale="Ru_ru")
        
        for i in range(N):
            data = {"name": fake_ru.name(),
                    "year": random.randint(1900, 2022)}
            
            response = self.client.post("/api/director/", data)
            content = response.data
            self.assertTrue("status" in content)
            self.assertTrue("id" in content)
            self.assertTrue(content["status"] == "OK")
            director_id = content["id"]
            
            response = self.client.get("/api/director/" + str(director_id) + "/")
            content = response.data
            self.assertTrue("id" in content)
            for field in field_names:
                self.assertTrue(field in content)
                self.assertTrue(content[field] == data[field])
        
    def tearDown(self):
        pass

class IndexTest(TestCase):
    def setUp(self):
        pass
        
    def test_post_get(self):
        url = "http://localhost:8000/"
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(PATH_2_DRIVER,
                                  options=chrome_options)
        driver.get(url)

        try:
            element = driver.find_element_by_xpath("//input[@name='text_box']")
        except:
            self.AssertTrue(False)

        fake_ru = Faker(locale="Ru_ru")
        message = fake_ru.sentence(nb_words=random.randint(4, 8), ext_word_list=None)

        for i in range(len(message)):
            element.send_keys(message[i])
            time.sleep(0.1)
        
        try:
            reset = driver.find_element_by_xpath("//button[@type='reset']")
            reset.click()
        except:
            self.AssertTrue(False)
        time.sleep(0.1)
        driver.quit()
        
    def tearDown(self):
        pass