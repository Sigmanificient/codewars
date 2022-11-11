"""Kata url: https://www.codewars.com/kata/588a00ad70720f2cd9000005."""


class Router:

    def __init__(self):
        self.__routes = {}
        self._404 = lambda: "Error 404: Not Found"

    def bind(self, uri, method, function):
        self.__routes[uri + method] = function

    def runRequest(self, uri, method):
        return self.__routes.get(uri + method, self._404)()
