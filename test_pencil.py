from pencil import *

def test_pencil_writes_simple_string():
    length = 10
    durability = 1000
    eraser = 1000
    paper = ""

    newPencil = Pencil(length, durability, eraser)
    text = newPencil.write("simple string", paper)
    assert text == "simple string"


def test_pencil_writes_lower_case_letters_when_durability_goes_to_0():
    newPencil = Pencil(1,1,1)
    text = newPencil.write("t", "")
    assert text == "t"

def test_pencil_writes_capital_letters_when_durability_goes_to_0():
    newPencil = Pencil(2,2,2)
    text = newPencil.write("T", "")
    assert text == "T"

def test_pencil_only_writes_capital_letters_when_enough_durability():
    newPencil = Pencil(1, 1, 1)
    text = newPencil.write("T", "")
    assert text == " "


def test_text_appended_to_existing_text():
    length = 10
    durability= 1000
    eraser = 1000
    paper = ""
    newPencil = Pencil(length, durability, eraser)
    paper= newPencil.write("simple string", paper)
    paper = newPencil.write("is complex", paper)
    assert paper == "simple stringis complex"

def test_durability_reduction():

    length = 10
    durability = 100
    eraser = 1000
    paper = ""
    newPencil = Pencil(length, durability, eraser)
    newPencil.write("Simple String", paper)
    assert newPencil.current_durability == 86

def test_text_after_durability_is_zero_and_pencil_is_dull():
    length = 10
    durability = 10
    eraser = 1000
    paper = ""
    newPencil = Pencil(length, durability, eraser)
    text = newPencil.write("Simple String", paper)
    assert text == "Simple St    "

def test_durability_regains_after_sharpening():
    length = 10
    durability = 10
    eraser = 1000
    paper = ""
    newPencil = Pencil(length, durability, eraser)
    text = newPencil.write("Simple String", paper)
    newPencil.sharpen()
    text = newPencil.write("Simple String", text)
    assert text == "Simple St    Simple St    "

def test_dullness_after_sharpening_length_zero_pencil():
    length = 3
    durability = 10
    eraser = 100
    paper = ""
    newPencil = Pencil(length, durability, eraser)
    newPencil.sharpen()
    newPencil.sharpen()
    newPencil.sharpen()
    text = newPencil.write("Simple String", paper)
    newPencil.sharpen()
    text = newPencil.write("simple", text)
    assert text == "Simple Str          "