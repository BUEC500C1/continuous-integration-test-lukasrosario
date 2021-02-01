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
    m = re.findall(r"\d+(?:\.\d+)?", string)
    return m[0]


distances = [
    ("12 feet to meters", 3.6576),
    ("3 meters to feet", 9.84252),
    ("5000 meters to miles", 3.106856),
    ("what is 56 feet in inches", 672),
    ("what is 2 miles in meters", 3218.69),
    ("?/&&  2 feet to inches \\  ??", 24),
]


@pytest.mark.parametrize("question,expected_answer", distances)
def test_ask_distances(client, question, expected_answer):
    rv = ask_question(client, question).data.decode()
    value = float(parseint(rv))
    print(value)
    assert 0.99 * expected_answer <= value <= 1.01 * expected_answer
