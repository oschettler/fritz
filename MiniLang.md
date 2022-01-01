# Example #1

Minlang programs are valid Markdown files. Code is embedded as indended blocks

## Literals

There are literals for the basic types *bool*, *number*, *text*, *list*, and *map*. 

Variables are declared by assigning to them. Identifiers names may consist if letters, digits, and underscores. They must begin with a letter.

  var a_bool: true
  vat a_text: "Hallo Welt"
  var the_number_zero: 0.0
  var a_negative_number: -1
  var a_list: ( 2 4 "six" ( "a nested list" 42 ) )
  var a_map: ( first: "What?" second: "Cool" "third with spaces": 42 )

Commas in lists are optional.

  var a_list: (1, 2, "hallo")

## Functions

Functions are defined similar to variables.

  to add a b:
    a + b

Parameters can be named:

  to check x: x y: y:
    print x y

Parameters may be separated by commas:

  to check x: x, y: y:
    print x, y


Similar to Python, indentation is important.

## Conditions

  if a = 5:
    print "A is five"
  else if a = 7:
    print "A is seven"
  else:
    print "All other cases"

Multiple conditions may be checked at once.

  if a in
    5: print "A is five"
    7: print "A is seven"
    else:
      print "All other cases"

Conditions may also be used as expression.

  var b: 5 if a = 5 else 7

## Loops

There are two types of loops:

  a: false
  while a = false:
    read a

  while element in ( 2 4 "six" ):
    print element

  while key value in (a: 42 b: 43 c: 44):
    print "key: " key ", value: " value

  while n in 2 .. 5:
    print n

In the last loop, the ".." creates a range. The Numbers 2, 3, 4 are printed. If you want an inclusive range, use three dots "...".

## Iterators

Iterators may be invoked separate from loops, like list comprehensions in Python

  var a_list: element[0..1] while element in ("Olav" "Lena" "Birgit")

a_list will contain ("Ol" "Le" "Bi")

## Tests

Example invocations may be included after a leading **>**.with the expected result after a **->**.

> add 3 5 -> 8
> add 2.5 -3 -> -1.5
> add "hallo" " schöne welt!" -> "hallo schöne welt!"

