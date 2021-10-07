import sys

sys.path.insert(1, "../src")
from softdes import lambda_handler
import pytest


event_test = {
    "ndes": "1",
    "code": "",
    "args": [[1], [2], [3]],
    "resp": [0, 0, 0],
    "diag": ["a", "b", "c"]
}


# content of test_class.py
def test_correct_submission():
    with open('./desafios/desafio1_Correto.py','r') as des:
        event_test["code"] = des.read()
    assert len(lambda_handler(event_test)) == 0

def test_wrong_function():
    with open('./desafios/desafio1_SemFunc.py','r') as des:
        event_test["code"] = des.read()
    answer = lambda_handler(event_test)
    assert (answer == "Nome da função inválido. Usar 'def desafio{0}(...)'".format(event_test["ndes"]))

def test_incorrect_submission():
    with open('./desafios/desafio1_Incorreto.py','r') as des:
        event_test["code"] = des.read()
    answer = lambda_handler(event_test)
    assert (answer == " ".join(event_test["diag"]))
