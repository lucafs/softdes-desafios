from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import pytest

driver = webdriver.Firefox()

# Testa o login admin admin no get e ve se funcion
def test_login_success():
    try:
        driver.get("admin:admin@localhost:8080")
        assert True
    except:
        assert False


# Testa errar a senha e ve se não funciona
def test_login_fail():
    try:
        driver.get("admin:adaim@localhost:8080")
        assert False
    except:
        assert True


def test_desafio_correto():
    try:
        driver.get("admin:admin@localhost:8080")
        filesend = driver.find_element_by_id("resposta")
        filesend.send_keys(os.getcwd() + "/desafios/desafio1_Correto.py")
        driver.find_element_by_class_name("btn-primary").click()
        headline = driver.find_element_by_class_name("table-responsive")
        text = (
            headline.find_element_by_xpath(".//table/tbody/tr/td[3]")
            .get_attribute("innerHTML")
            .strip()
        )
        assert text == "OK!"
    except:
        assert False


def test_desafio_incorreto():
    try:
        driver.get("admin:admin@localhost:8080")
        filesend = driver.find_element_by_id("resposta")
        filesend.send_keys(os.getcwd() + "/desafios/desafio1_Incorreto.py")
        driver.find_element_by_class_name("btn-primary").click()
        table = driver.find_element_by_class_name("table-responsive")
        text = (
            table.find_element_by_xpath(".//table/tbody/tr/td[3]")
            .get_attribute("innerHTML")
            .strip()
        )
        assert text == "Erro"
    except:
        assert False

@pytest.fixture(autouse=True, scope='session')
def my_fixture_teardown():
    yield
    driver.quit()
    os.remove("geckodriver.log")

