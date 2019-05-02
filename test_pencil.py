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
    text = newPencil.write("abc", text)
    assert text == "Simple St       "

def test_erase_last_instance_of_text():
    newPencil = Pencil(10,10,1000)
    paper = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
    text = newPencil.erase("chuck", paper)
    text = newPencil.erase("chuck", text)
    assert text == "How much wood would a woodchuck chuck if a wood      could       wood"

def test_eraser_degredation():
    newPencil = Pencil(10,10,3)
    paper = "Buffalo BilL"
    text = newPencil.erase("Bill")
    assert text == "Buffalo B   "

def test_eraser_text_mismatch():
    newPencil = Pencil(10,10,10)
    text = "When a pencil is created"
    erased_text = newPencil.erase("Pen", text)
    assert erased_text == "When a pencil is created"

def test_editing():
    newPencil = Pencil(10,10,10)
    text = "An       a day keeps the doctor away"
    edited_text = newPencil.edit("onion", text)
    assert edited_text == "An onion a day keeps the doctor away"

def test_edits_use_left_white_spaces_first():
    newPencil = Pencil(10,10,10)
    text = "An      a day    keeps the doctor away"
    edited_text = newPencil.edit("onion", text)
    assert edited_text == "An onion a day    keeps the doctor away"

def test_edit_collisions():
    newPencil = Pencil(10,100,100)
    text = "An      a day keeps the doctor away"
    edited_text = newPencil.edit("artichoke", text)
    assert edited_text == "An artich@k@ay keeps the doctor away"

def test_edit_collisions_of_same_characters():
    newPencil=Pencil(10,10,10)
    text = "hello     universe"
    edited_text = newPencil.edit("Neptune", text)
    assert edited_text == "hello Neptun@verse"
