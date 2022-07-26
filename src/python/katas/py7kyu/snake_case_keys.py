"""Kata url: https://www.codewars.com/kata/610c8308ed5ee4003279d112."""

from typing import Dict


def snake_case(string) -> str:
    return "".join(char if char.islower() else f"_{char.lower()}" for char in string)


def snake_casify(dictionary) -> Dict[str, str]:
    return {snake_case(k): v for k, v in dictionary.items()}


def test_snake_case():
    assert snake_casify(
        {"firstName": "Bob", "lastName": "Johnson", "dateOfBirth": "8/8/2010"}
    ) == {"first_name": "Bob", "last_name": "Johnson", "date_of_birth": "8/8/2010"}
    assert snake_casify(
        {"firstName": "Geraldine", "lastName": "Smores", "dateOfBirth": "23/5/2040"}
    ) == {
        "first_name": "Geraldine",
        "last_name": "Smores",
        "date_of_birth": "23/5/2040",
    }
    assert snake_casify(
        {"firstName": "Hilbert", "lastName": "Simmons", "dateOfBirth": "11/8/2038"}
    ) == {"first_name": "Hilbert", "last_name": "Simmons", "date_of_birth": "11/8/2038"}
    assert snake_casify(
        {"firstName": "Bill", "lastName": "Musk", "dateOfBirth": "19/7/2015"}
    ) == {"first_name": "Bill", "last_name": "Musk", "date_of_birth": "19/7/2015"}
    assert snake_casify(
        {"firstName": "Paul", "lastName": "Thomas", "dateOfBirth": "23/5/2040"}
    ) == {"first_name": "Paul", "last_name": "Thomas", "date_of_birth": "23/5/2040"}
    assert snake_casify(
        {"firstName": "Qazi", "lastName": "Davidson", "dateOfBirth": "8/8/2010"}
    ) == {"first_name": "Qazi", "last_name": "Davidson", "date_of_birth": "8/8/2010"}
    assert snake_casify(
        {"firstName": "Robert", "lastName": "Findish", "dateOfBirth": "9/11/2030"}
    ) == {"first_name": "Robert", "last_name": "Findish", "date_of_birth": "9/11/2030"}
    assert snake_casify(
        {"firstName": "Alice", "lastName": "Kivy", "dateOfBirth": "4/4/2041"}
    ) == {"first_name": "Alice", "last_name": "Kivy", "date_of_birth": "4/4/2041"}
    assert snake_casify(
        {"firstName": "Lucy", "lastName": "Johnson", "dateOfBirth": "10/12/1996"}
    ) == {"first_name": "Lucy", "last_name": "Johnson", "date_of_birth": "10/12/1996"}
    assert snake_casify(
        {"firstName": "Jeff", "lastName": "Bendedict", "dateOfBirth": "27/12/2044"}
    ) == {"first_name": "Jeff", "last_name": "Bendedict", "date_of_birth": "27/12/2044"}
    assert snake_casify(
        {"firstName": "Geraldine", "lastName": "Simmons", "dateOfBirth": "18/7/2007"}
    ) == {
        "first_name": "Geraldine",
        "last_name": "Simmons",
        "date_of_birth": "18/7/2007",
    }
    assert snake_casify(
        {"firstName": "Steve", "lastName": "Musk", "dateOfBirth": "10/8/2021"}
    ) == {"first_name": "Steve", "last_name": "Musk", "date_of_birth": "10/8/2021"}
    assert snake_casify(
        {"firstName": "Geraldine", "lastName": "Kivy", "dateOfBirth": "6/5/1981"}
    ) == {"first_name": "Geraldine", "last_name": "Kivy", "date_of_birth": "6/5/1981"}
    assert snake_casify(
        {"firstName": "Jeff", "lastName": "Musk", "dateOfBirth": "28/5/2019"}
    ) == {"first_name": "Jeff", "last_name": "Musk", "date_of_birth": "28/5/2019"}
    assert snake_casify(
        {"firstName": "Bill", "lastName": "Simmons", "dateOfBirth": "18/2/2004"}
    ) == {"first_name": "Bill", "last_name": "Simmons", "date_of_birth": "18/2/2004"}
    assert snake_casify(
        {"firstName": "Samantha", "lastName": "Thomas", "dateOfBirth": "25/7/2014"}
    ) == {"first_name": "Samantha", "last_name": "Thomas", "date_of_birth": "25/7/2014"}
    assert snake_casify(
        {"firstName": "Bob", "lastName": "Larry", "dateOfBirth": "3/7/2004"}
    ) == {"first_name": "Bob", "last_name": "Larry", "date_of_birth": "3/7/2004"}
    assert snake_casify(
        {"firstName": "Timothy", "lastName": "Pulapakura", "dateOfBirth": "20/7/2011"}
    ) == {
        "first_name": "Timothy",
        "last_name": "Pulapakura",
        "date_of_birth": "20/7/2011",
    }
    assert snake_casify(
        {"firstName": "Remming", "lastName": "Bendedict", "dateOfBirth": "15/10/2030"}
    ) == {
        "first_name": "Remming",
        "last_name": "Bendedict",
        "date_of_birth": "15/10/2030",
    }
    assert snake_casify(
        {"firstName": "Henry", "lastName": "Musk", "dateOfBirth": "14/2/1995"}
    ) == {"first_name": "Henry", "last_name": "Musk", "date_of_birth": "14/2/1995"}
    assert snake_casify(
        {"firstName": "Susan", "lastName": "Simmons", "dateOfBirth": "11/1/2043"}
    ) == {"first_name": "Susan", "last_name": "Simmons", "date_of_birth": "11/1/2043"}
    assert snake_casify(
        {"firstName": "Steve", "lastName": "Davidson", "dateOfBirth": "28/9/2033"}
    ) == {"first_name": "Steve", "last_name": "Davidson", "date_of_birth": "28/9/2033"}
    assert snake_casify(
        {"firstName": "Bob", "lastName": "Washington", "dateOfBirth": "1/4/2019"}
    ) == {"first_name": "Bob", "last_name": "Washington", "date_of_birth": "1/4/2019"}
    assert snake_casify(
        {"firstName": "Timothy", "lastName": "Teret", "dateOfBirth": "26/3/2034"}
    ) == {"first_name": "Timothy", "last_name": "Teret", "date_of_birth": "26/3/2034"}
    assert snake_casify(
        {"firstName": "Paul", "lastName": "Johnson", "dateOfBirth": "5/1/1989"}
    ) == {"first_name": "Paul", "last_name": "Johnson", "date_of_birth": "5/1/1989"}
    assert snake_casify(
        {"firstName": "Jeff", "lastName": "Pulapakura", "dateOfBirth": "1/4/1993"}
    ) == {"first_name": "Jeff", "last_name": "Pulapakura", "date_of_birth": "1/4/1993"}
    assert snake_casify(
        {"firstName": "George", "lastName": "Wholesome", "dateOfBirth": "1/4/1993"}
    ) == {"first_name": "George", "last_name": "Wholesome", "date_of_birth": "1/4/1993"}
    assert snake_casify(
        {"firstName": "George", "lastName": "Robertson", "dateOfBirth": "7/4/1980"}
    ) == {"first_name": "George", "last_name": "Robertson", "date_of_birth": "7/4/1980"}
    assert snake_casify(
        {"firstName": "George", "lastName": "Simmons", "dateOfBirth": "5/7/1985"}
    ) == {"first_name": "George", "last_name": "Simmons", "date_of_birth": "5/7/1985"}
    assert snake_casify(
        {"firstName": "Alice", "lastName": "Williamson", "dateOfBirth": "8/8/2010"}
    ) == {"first_name": "Alice", "last_name": "Williamson", "date_of_birth": "8/8/2010"}
    assert snake_casify(
        {"firstName": "Max", "lastName": "Musk", "dateOfBirth": "16/4/2021"}
    ) == {"first_name": "Max", "last_name": "Musk", "date_of_birth": "16/4/2021"}
    assert snake_casify(
        {"firstName": "Steve", "lastName": "Bezos", "dateOfBirth": "9/11/2030"}
    ) == {"first_name": "Steve", "last_name": "Bezos", "date_of_birth": "9/11/2030"}
    assert snake_casify(
        {"firstName": "Gerald", "lastName": "Wholesome", "dateOfBirth": "1/7/2038"}
    ) == {"first_name": "Gerald", "last_name": "Wholesome", "date_of_birth": "1/7/2038"}
    assert snake_casify(
        {"firstName": "Raj", "lastName": "Smores", "dateOfBirth": "25/10/1989"}
    ) == {"first_name": "Raj", "last_name": "Smores", "date_of_birth": "25/10/1989"}
    assert snake_casify(
        {"firstName": "Bob", "lastName": "Findish", "dateOfBirth": "15/1/2027"}
    ) == {"first_name": "Bob", "last_name": "Findish", "date_of_birth": "15/1/2027"}
    assert snake_casify(
        {"firstName": "Tony", "lastName": "Wholesome", "dateOfBirth": "21/6/2020"}
    ) == {"first_name": "Tony", "last_name": "Wholesome", "date_of_birth": "21/6/2020"}
    assert snake_casify(
        {"firstName": "Geraldine", "lastName": "Bezos", "dateOfBirth": "9/6/2029"}
    ) == {"first_name": "Geraldine", "last_name": "Bezos", "date_of_birth": "9/6/2029"}
    assert snake_casify(
        {"firstName": "Derek", "lastName": "Robertson", "dateOfBirth": "22/11/1987"}
    ) == {
        "first_name": "Derek",
        "last_name": "Robertson",
        "date_of_birth": "22/11/1987",
    }
    assert snake_casify(
        {"firstName": "Jeff", "lastName": "Smores", "dateOfBirth": "4/4/2041"}
    ) == {"first_name": "Jeff", "last_name": "Smores", "date_of_birth": "4/4/2041"}
    assert snake_casify(
        {"firstName": "Remming", "lastName": "Gregory", "dateOfBirth": "28/7/2028"}
    ) == {"first_name": "Remming", "last_name": "Gregory", "date_of_birth": "28/7/2028"}
    assert snake_casify(
        {"firstName": "Geraldine", "lastName": "Bezos", "dateOfBirth": "14/2/1995"}
    ) == {"first_name": "Geraldine", "last_name": "Bezos", "date_of_birth": "14/2/1995"}
    assert snake_casify(
        {"firstName": "Remming", "lastName": "Smores", "dateOfBirth": "11/8/2038"}
    ) == {"first_name": "Remming", "last_name": "Smores", "date_of_birth": "11/8/2038"}
    assert snake_casify(
        {"firstName": "Elon", "lastName": "Bezos", "dateOfBirth": "27/3/2019"}
    ) == {"first_name": "Elon", "last_name": "Bezos", "date_of_birth": "27/3/2019"}
    assert snake_casify(
        {"firstName": "James", "lastName": "Charles", "dateOfBirth": "26/3/2034"}
    ) == {"first_name": "James", "last_name": "Charles", "date_of_birth": "26/3/2034"}
    assert snake_casify(
        {"firstName": "Elon", "lastName": "Teret", "dateOfBirth": "13/1/2006"}
    ) == {"first_name": "Elon", "last_name": "Teret", "date_of_birth": "13/1/2006"}
    assert snake_casify(
        {"firstName": "Derek", "lastName": "Thomas", "dateOfBirth": "1/6/1999"}
    ) == {"first_name": "Derek", "last_name": "Thomas", "date_of_birth": "1/6/1999"}
    assert snake_casify(
        {"firstName": "Tony", "lastName": "Pulapakura", "dateOfBirth": "2/5/1986"}
    ) == {"first_name": "Tony", "last_name": "Pulapakura", "date_of_birth": "2/5/1986"}
    assert snake_casify(
        {
            "purchaserName": "Geraldine",
            "purchaseProduct": "Phone",
            "dateOfTransaction": "28/12/2003",
        }
    ) == {
        "purchaser_name": "Geraldine",
        "purchase_product": "Phone",
        "date_of_transaction": "28/12/2003",
    }
    assert snake_casify(
        {
            "purchaserName": "Geraldine",
            "purchaseProduct": "Guitar",
            "dateOfTransaction": "11/3/2017",
        }
    ) == {
        "purchaser_name": "Geraldine",
        "purchase_product": "Guitar",
        "date_of_transaction": "11/3/2017",
    }
    assert snake_casify(
        {
            "purchaserName": "Tony",
            "purchaseProduct": "Desktop",
            "dateOfTransaction": "3/4/2042",
        }
    ) == {
        "purchaser_name": "Tony",
        "purchase_product": "Desktop",
        "date_of_transaction": "3/4/2042",
    }
