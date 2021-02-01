import pytest
import json
import re


def test_index(client):
    rv = client.get("/")
    assert b"Enter a conversion question below" in rv.data


def ask_question(client, question):
    return client.post(
        "/",
        data=json.dumps({"question": question}),
        headers={"Content-Type": "application/json"},
    )


def parseint(string):
    m = re.findall(r"-?\d+(?:\.\d+)?", string)
    return m[0]


distances = [
    ("12 feet to meters", 3.6576),
    ("convert 3 meters to feet", 9.84252),
    ("5000 meters to miles", 3.106856),
    ("what is 56 feet in inches", 672),
    ("what is 2 miles in meters", 3218.69),
    ("?/&&  2feet to inches \\  ??", 24),
]

weights = [
    ("25 oz to grams", 708.738),
    ("convert 45 lbs to kg", 20.4117),
    ("10 grams to lb", 0.0220462),
    ("5329 oz to kilograms", 151.0746),
    ("what is 100 kilograms in oz", 3527.4),
    ("/&\\  29kg in g \\  \\??", 29000),
]

temperatures = [
    ("25 c to f", 77),
    ("convert 54 kelvin to c", -219.15),
    ("1000 celsius to fahrenheit", 1832),
    ("-64 fahrenheit to kelvin", 219.817),
    ("what is 32 f in c", 0),
    ("  \\//  290f in c \\  \\?&&  ", 143.333),
]


@pytest.mark.parametrize("question,expected_answer", distances)
def test_ask_distances(client, question, expected_answer):
    rv = ask_question(client, question).data.decode()
    value = float(parseint(rv))
    assert 0.995 * abs(expected_answer) <= abs(value) <= 1.005 * abs(
        expected_answer
    ) and (
        all(item > 0 for item in [value, expected_answer])
        or all(item < 0 for item in [value, expected_answer])
        or all(item == 0 for item in [value, expected_answer])
    )


@pytest.mark.parametrize("question,expected_answer", weights)
def test_ask_weights(client, question, expected_answer):
    rv = ask_question(client, question).data.decode()
    value = float(parseint(rv))
    assert 0.995 * abs(expected_answer) <= abs(value) <= 1.005 * abs(
        expected_answer
    ) and (
        all(item > 0 for item in [value, expected_answer])
        or all(item < 0 for item in [value, expected_answer])
        or all(item == 0 for item in [value, expected_answer])
    )


@pytest.mark.parametrize("question,expected_answer", temperatures)
def test_ask_temperatures(client, question, expected_answer):
    rv = ask_question(client, question).data.decode()
    value = float(parseint(rv))
    assert 0.995 * abs(expected_answer) <= abs(value) <= 1.005 * abs(
        expected_answer
    ) and (
        all(item > 0 for item in [value, expected_answer])
        or all(item < 0 for item in [value, expected_answer])
        or all(item == 0 for item in [value, expected_answer])
    )
