# Minilang - Language overview

Minlang combines documentation, code, and tests into a single file format. Minilang programs are valid Markdown files. Code is embedded as indented blocks.

## Literals

There are literals for the basic types *bool*, *number*, *text*, *list*, and *map*. 

Variables are declared by assigning a value to them. Identifiers names may consist if letters, digits, and underscores. They must begin with a letter.

  a_bool: true
  a_text: "Hallo schöne Welt ☺"
  the_number_zero: 0.0
  a_negative_number: -1
  a_list: ( 2 4 "six" ( "a nested list" 42 ) )
  a_map: ( first: "What?" second: "Cool" "third with spaces": 42 )
  a_rect: ( x: 10 y: 20 w: 13 h: 8 )

Commas in lists are optional.

  a_list: (1, 2, "hallo")

Strings may contain code, enclosed in **.().**.

  a_text: "There are .(n). kitten.("s" if n != 1). in the basket."

## Functions

Functions consist of a variable and a value that is not constant, but computed. Computed values may take parameters and can incorporate ("close over") their scope.

  t: 1
  tick: t + 1

  plus1 a:
    a + 1

  add a b:
    a + b

Functions return the value of the last expression. Return statements may also be used.

  max a b:
    if a > b:
      return a
    else:
      return b

Parameters can be named:

  check x: x y: y:
    print x y

Parameters may be separated by commas:

  check x: x, y: y:
    print x, y


By now you will have notices: Similar to Python, indentation is important.

## Conditions

  if a = 5:
    print "A is five"
  else if a = 7:
    print "A is seven"
  else:
    print "All other cases"

Multiple conditions may be checked at once.

  if a
    < 10:
      print "A is below ten"
      continue
    = 5: 
      print "A is five"
    = 7: 
      print "A is seven"
    else:
      print "All other cases"

In this construct, the branches don't fall through as they do in "C". Instead, if you want to have a branch fall through, you **continue** to the next branch.

Conditions may also be used as expression.

  b: 5 if a = 5 else 7

## Loops

There are two types of loops. All of them use the **while** keyword.

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

  a_list: element[0..1] while element in ("Olav" "Lena" "Birgit")

a_list will contain ("Ol" "Le" "Bi")

## Tests

Example invocations may be included after a leading **>**.with the expected result after a **->**.

> add 3 5 -> 8
> add 2.5 -3 -> -1.5
> add "hallo" " schöne welt!" -> "hallo schöne welt!"

