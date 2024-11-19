"""Kata url: https://www.codewars.com/kata/56f3f6a82010832b02000f38."""
describe_age=lambda a:"You're a(n) "+{1:"elderly",a<65:"adult",a<18:"teenager",a<13:"kid"}[1]