from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver.exe')
   # переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

class element_has_css_class(object):
  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class

  def __call__(self, driver):
    element = driver.find_element(*self.locator)
    if self.css_class in element.get_attribute("class"):
        return element
    else:
        return False


def test_petfriends(selenium):
   selenium.get("https://petfriends.skillfactory.ru/")

   pytest.driver.find_element_by_id('email').send_keys('lizka.nvrsk@gmail.com')
   pytest.driver.find_element_by_id('pass').send_keys('1234Liza')


   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element_by_xpath('//button[@type="submit"]').click()
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends" #проверяем, что находимся на главной странице

   #поиск на странице фото, имен, породы
   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0   #проверка, что эти поля не пустые

#
def test_show_my_pets():

   pytest.driver.find_element_by_id('email').send_keys('lizka.nvrsk@gmail.com')
   pytest.driver.find_element_by_id('pass').send_keys('1234Liza')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   #явное ожидание:
   wait = WebDriverWait(pytest.driver, 5)

   # Проверяем, что мы оказались на главной странице сайта.
   # Ожидаем в течение 5с, что на странице есть тег h1 с текстом "PetFriends"
   assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME,'h1'), "PetFriends"))

   # страница с моими питомцами.
   pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()

   # проверяем, что мы оказались на  странице с моими питомцами.
   # ожидаем в течение 5с, что на странице есть тег h2 с текстом "All" -именем пользователя
   assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), "All"))

   # данные питомцев:
   css_locator = 'tbody>tr'
   data_my_pets = pytest.driver.find_elements_by_css_selector(css_locator)

   # ожидаем, что данные всех питомцев видны на странице:
   for i in range(len(data_my_pets)):
      assert wait.until(EC.visibility_of(data_my_pets[i]))

   # ищем фото питомцев и ожидаем, что все загруженные фото, видны на странице:
   image_my_pets = pytest.driver.find_elements_by_css_selector('img[style="max-width: 100px; max-height: 100px;"]')
   for i in range(len(image_my_pets)):
      if image_my_pets[i].get_attribute('src') != '':
         assert wait.until(EC.visibility_of(image_my_pets[i]))

   # ищем все имена питомцев и ожидаем увидеть их на странице:
   name_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[1]')
   for i in range(len(name_my_pets)):
      assert wait.until(EC.visibility_of(name_my_pets[i]))

   # ищем все породы питомцев и ожидаем увидеть их на странице:
   type_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[2]')
   for i in range(len(type_my_pets)):
      assert wait.until(EC.visibility_of(type_my_pets[i]))

   # ищем все данные возраста питомцев и ожидаем увидеть их на странице:
   age_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[3]')
   for i in range(len(age_my_pets)):
      assert wait.until(EC.visibility_of(age_my_pets[i]))

   # количество питомцев пользователя:
   all_statistics = pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text.split("\n")
   statistics_pets = all_statistics[1].split(" ")
   all_my_pets = int(statistics_pets[-1])

   assert len(data_my_pets) == all_my_pets

   # у половины питомцев есть фото:
   m = 0
   for i in range(len(image_my_pets)):
      if image_my_pets[i].get_attribute('src') != '':
         m += 1
   assert m >= all_my_pets/2

   # у всех питомцев есть имя:
   for i in range(len(name_my_pets)):
      assert name_my_pets[i].text != ''

   # у всех питомцев есть порода:
   for i in range(len(type_my_pets)):
      assert type_my_pets[i].text != ''

   # что у всех питомцев есть возраст:
   for i in range(len(age_my_pets)):
      assert age_my_pets[i].text != ''

   # у всех питомцев разные имена:
   list_name_my_pets = []
   for i in range(len(name_my_pets)):
      list_name_my_pets.append(name_my_pets[i].text)
   set_name_my_pets = set(list_name_my_pets) # преобразовываем список в множество
   assert len(list_name_my_pets) == len(set_name_my_pets) # сравниваем длину списка и множества: без повторов должны совпасть

   #нет повторяющихся питомцев:
   list_data_my_pets = []
   for i in range(len(data_my_pets)):
      list_data = data_my_pets[i].text.split("\n")
      list_data_my_pets.append(list_data[0])
   set_data_my_pets = set(list_data_my_pets)
   assert len(list_data_my_pets) == len(set_data_my_pets)