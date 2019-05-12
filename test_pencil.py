from pencil import *

def test_pencil_writes_simple_string():
    newPencil = Pencil(length=10, durability=1000, eraser=1000)
    text = newPencil.write(text="simple string", paper="")
    assert text == "simple string"


def test_pencil_writes_lower_case_letters_when_durability_goes_to_0():
    newPencil = Pencil(length=1,durability=1,eraser=1)
    text = newPencil.write("t", "")
    assert text == "t"

def test_pencil_writes_capital_letters_when_durability_goes_to_0():
    newPencil = Pencil(length=2,durability=2,eraser=2)
    text = newPencil.write("T", "")
    assert text == "T"

def test_pencil_does_not_write_letters_when_lacking_durability():
    newPencil = Pencil(length=1,durability= 1,eraser= 1)
    text = newPencil.write("T", "")
    assert text == " "


def test_write_appends_new_text_to_existing_text():
    newPencil = Pencil(length=10, durability=100, eraser=10)
    paper= newPencil.write("simple string", paper="")
    paper = newPencil.write("is complex", paper)
    assert paper == "simple stringis complex"

def test_durability_reduction():
    newPencil = Pencil(length=10, durability=100, eraser=100)
    newPencil.write("Simple String", "")
    assert newPencil.current_durability == 86

def test_text_after_durability_is_zero_and_pencil_is_dull():
    newPencil = Pencil(length=10, durability=10, eraser=10)
    text = newPencil.write("Simple String", "")
    assert text == "Simple St    "

def test_durability_restored_after_sharpening():
    newPencil = Pencil(length=10, durability=10, eraser=10)
    text = newPencil.write("Simple String", "")
    newPencil.sharpen()
    text = newPencil.write("Simple String", text)
    assert text == "Simple St    Simple St    "


def test_length_decreased_after_sharpening():
    newPencil = Pencil(length=3, durability=10, eraser=10)
    newPencil.sharpen()
    assert newPencil.length == 2

def test_length_zero_pencil_does_not_write():
    newPencil = Pencil(length=3, durability=10, eraser=10)
    newPencil.sharpen()
    newPencil.sharpen()
    newPencil.sharpen()
    text = newPencil.write("Simple String", paper="")
    newPencil.sharpen()
    text = newPencil.write("abc", text)
    assert text == "Simple St       "

def test_erase_last_instance_of_text():
    newPencil = Pencil(10,10,1000)
    paper = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
    text = newPencil.erase("chuck", paper)
    text = newPencil.erase("chuck", text)
    assert text == "How much wood would a woodchuck chuck if a wood      could       wood"

def test_eraser_stops_erasing_after_degraded_to_zero():
    newPencil = Pencil(10,10,3)
    paper = "Buffalo Bill"
    text = newPencil.erase("Bill", paper)
    assert text == "Buffalo B   "

def test_eraser_does_not_erase_mismatched_text():
    newPencil = Pencil(10,10,10)
    text = "When a pencil is created"
    erased_text = newPencil.erase("Pen", text)
    assert erased_text == "When a pencil is created"

def test_edit_inserts_space():
    newPencil = Pencil(10,10,10)
    text = "An       a day keeps the doctor away"
    edited_text = newPencil.edit("onion", text)
    assert edited_text == "An onion a day keeps the doctor away"

def test_edits_inserts_in_first_space():
    newPencil = Pencil(10,10,10)
    text = "An       a day    keeps the doctor away"
    edited_text = newPencil.edit("onion", text)
    assert edited_text == "An onion a day    keeps the doctor away"

def test_edit_collisions_are_at_signs():
    newPencil = Pencil(10,100,100)
    text = "An       a day keeps the doctor away"
    edited_text = newPencil.edit("artichoke", text)
    assert edited_text == "An artich@k@ay keeps the doctor away"
"""
def test_edit_collisions_of_same_characters():
    newPencil=Pencil(10,10,10)
    text = "hello     universe"
    edited_text = newPencil.edit("Neptune", text)
    assert edited_text == "hello Neptun@verse"
"""