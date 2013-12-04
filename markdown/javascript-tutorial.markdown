SWE 430 Tutorial 1:  JavaScript Tutorial
========================================================================


You can interact with the code from the following JavaScript tutorial at jsbin.com:

- [jsbin JavaScript Tutorial](http://jsbin.com/swe430_javascript_tutorial/latest/edit?javascript,console,live)


All our examples and assignments are in JavaScript.  A quick overview of JavaScript is available at <a href="http://coffeescript.org">coffeescript.org</a>.  The overview provides several code snippets.  You can test a code snippet by clicking the 'load' button and then run it using the 'run' button.  You can also modify any snippet you load.  Make sure you understand the topics listed below.  If the overview is not enough, complete books are also available: 
<a href="http://autotelicum.github.com/Smooth-CoffeeScript/">Smooth CoffeeScript</a>
(if link is blocked, here's the pdf of  
<a href="SmoothCoffeeScript.pdf">Smooth CoffeeScript</a>) and
<a href="http://arcturo.github.io/library/coffeescript/02_syntax.html">The Little Book on CoffeeScript</a> (if link is blocked, you can also read it on Safari Online.)  If you have any questions or run into any problems, please don't hesitate to ask me for help!

Note:  **Everything you need to run CoffeeScript and qUnit is contained within the environment for each example and exercise.  You do not need to install anything.**

whitespace

Most programmers use whitespace to give a visual layout to their code.  In CoffeeScript, this idea is taken a step further.  Whitespace is used to define both the visual layout and the syntax of the program.  It makes the code more readable by enforcing consistent layout while eliminating needless syntax tokens  (semicolons, braces, parentheses) already expressed by the layout.

From coffeescript.org:

"First, the basics: CoffeeScript uses significant whitespace to delimit blocks of code."

    f = (x) -> x * x            # Function defined in-line, compiles ok

    f = (x) ->                  # Function defined with body as sub-block
        x = 2                   # Proper indentation
        x + 5                   # Every statement in body lines up

    f = (x) ->                  # Improper indentation
        x = 2                   # Statements in body must line up
          x + 5                 # Should be 2 spaces &lt;-

    if good                     # Proper indentation of blocks
        do_a()                  # if and else line up
    else
        do_b()

    if bad
        do_a()
        else                    # Improper indentation, will not compile
        do_b()

From wikipedia:
"Coffeescript is very sensitive to whitespace, counting a tab as a single space."

When writing CoffeeScript, it's best not to use tabs and instead just stick with spaces.  Most text editors and IDEs have a setting to change tabs to spaces.  For example, when I type Tab, my editor inserts 4 spaces instead.

functions

    square = (x) -> x * x       # -> defines a function
    square 3                    # Returns 9

    alias = square              # Both square and alias refer to the 
                                # same function
    alias 3                     # Also returns 9

    call_with_3 = (f) -> f 3    # A function that takes a function as a
                                # parameter and calls it
    call_with_3 square          # Also return 9

Functions are defined with `->`.  Functions are first-class objects, can create closures, be assigned to variables, passed into functions as parameters and returned from functions as a return value.

String interpolation

    obj = {x: 7}                # An object with x = 7
    "3 + 4 = #{obj.x}"          # content inside #{} is executed
                                # returns "3 + 4 = 7"

The @ symbol

    @x                          # means this.x (replace @ with this.)
                                # 'this' is dynamically scoped

Classes and Constructors

    class A                 
        constructor: (@x) ->    # Class A has a property named x

        f: -> @x                # The method f() returns the value of x

Inheritance and polymorphism with the "extends" and "super" keywords

    class B extends A           # Inherits from class A
        constructor: ->
            super 5             # Call's class A constructor

        f: -> super()           # Call's class A's f() method

Accessing an object's property using a string

    b = new B                   # the x property is set to x
    b["x"]                      # returns 5

Regular Expressions

    re = /\d\d/                 # matches 2 digits

