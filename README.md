# Pencil Durability Kata

The purpose of the Pencil Durability Kata is to write code to simulate, first coarsely and then more faithfully, an ordinary graphite pencil. It includes writing and editing text, point degradation, using the eraser, and sharpening the pencil. The point of this kata is to provide a larger-than-trivial exercise that can be used to practice TDD. A significant portion of the effort will be in determining which tests should be written and, more importantly, written next.

The pencil object has several major functions that the user can use it for. It can write text, edit text, erase text, and be sharpened. All of these functions effect various state variables of the pencil: length, durability, and eraser [durability].

The text functions take two variables, one which is the change to be made (text to be added or deleted), and then the paper to which the change is occuring on. The paper may already contain text.

The code was developed in a test-driven development style, writing tests based off of the specification here: https://github.com/PillarTechnology/kata-pencil-durability#point-degradation and then writing more code until the tests pass. You can see this in my git commit history here: https://github.com/bschwyn/pencilKata/commits/master

### Download and installation

To download the pencil kata use:

```git clone https://github.com/bschwyn/pencilKata```

and use pip to install pytest:

```pip3 install pytest```

The tests can then be run by typing

```pytest```, ```py.test``` or ```pytest pencilKata``` in the pencilKata directory.

### Future work

As the specification becomes more complete, here are some changes I could imagine being added to the pencilKata code.
- more strictly defining the results of edit collisions
- separation of the 'paper' into it's own separate class, with different characteristics. Perhaps different paper degrades pencils differently or has different effects on the text. Rather than string concatenation, paper objects would probably need an 'add text' method that pencil functions would access. Pencil methods would take a paper object, modify it, and then return the modified paper object.
- You could a Writing-Instrument interface which is implemented by different objects such as Pen, Pencil.

### Acknowlegements

This kata was written to follow the spec described here: https://github.com/PillarTechnology/kata-pencil-durability#point-degradation, by Pillar Technologies. All of the code is my own.
