# #!/usr/bin/env python3

# from functions import greet_programmer, greet, greet_with_default, \
#                         add, halve

# import io
# import sys



# class TestGreetProgrammer:
#     '''function greet_programmer()'''

#     def test_greet_programmer(self):
#         '''prints "Hello, programmer!"'''
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         greet_programmer()
#         sys.stdout = sys.__stdout__
#         assert(captured_out.getvalue() == "Hello, programmer!\n")

# class TestGreet:
#     '''function greet()'''

#     def test_greet_programmer(self):
#         '''prints "Hello, {name}!"'''
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         greet("Guido")
#         sys.stdout = sys.__stdout__
#         assert(captured_out.getvalue() == "Hello, Guido!\n")

# class TestGreetWithDefault:
#     '''function greet_with_default()'''

#     def test_greet_with_default(self):
#         '''prints "Hello, programmer!"'''
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         greet_with_default()
#         sys.stdout = sys.__stdout__
#         assert(captured_out.getvalue() == "Hello, programmer!\n")

#     def test_greet_with_default_with_param(self):
#         '''prints "Hello, {name}!"'''
#         captured_out = io.StringIO()
#         sys.stdout = captured_out
#         greet_with_default("Guido")
#         sys.stdout = sys.__stdout__
#         assert(captured_out.getvalue() == "Hello, Guido!\n")

# class TestAdd:
#     '''function add()'''

#     def test_add(self):
#         '''calculates 45 + 55 = 100'''
#         assert(add(45, 55) == 100)

# class TestHalve:
#     '''function halve()'''

#     def test_halve_int(self):
#         '''halves integer input'''
#         assert(halve(100) == 50)

#     def test_halve_float(self):
#         '''halves float input'''
#         # assert(halve(99.0) == 49.5)
#lib/testing/lib_test.py
import pytest
from lib.functions import greet_programmer, greet, greet_with_default, add, halve

def test_greet_programmer(capsys):
    greet_programmer()
    captured = capsys.readouterr()
    assert captured.out == "Hello, programmer!\n"

def test_greet(capsys):
    greet("Alice")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"

def test_greet_with_default(capsys):
    greet_with_default()
    captured = capsys.readouterr()
    assert captured.out == "Hello, programmer!\n"

    greet_with_default("Bob")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Bob!\n"


def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_halve():
    assert halve(10) == 5.0
    assert halve(1) == 0.5
    assert halve(0) == 0.0
