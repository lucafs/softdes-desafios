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


def test_incorrect_submission():
    with open('./desafios/desafio1_Incorreto.py','r') as des:
        event_test["code"] = des.read()
    

# def test_three():
#     with open('./desafios/desafioSemFunc.py','r') as des3:
#         desafio3 = des3.read()