╔══════════════════════════════════╗
║         📒 PySum Notes                 ║
║    Module 1 : Fundamentals             ║
║       L-01  →  L-13                    ║
╚══════════════════════════════════╝

🧱  L-01 : Variables & Data Types
──────────────────────────────────
  name = "Emperor"    # str
  age  = 18           # int
  pi   = 3.14         # float
  → Numbers no quotes
  → Text must be " " or ' '


🔁  L-02 : Typecasting
──────────────────────────────────
  int("42")   → 42
  float("5")  → 5.0
  str(1507)   → "1507"
  int(3.9)    → 3  (chops,no round)
  → input() returns str → cast!


⌨️  L-03 : User Input
──────────────────────────────────
  name = input("Name: ")
  age  = int(input("Age: "))
  → Always returns string
  → Convert early for math


✍️  L-04,05 : Comments & Escapes
──────────────────────────────────
  # this is a comment (ignored)
  \n   newline
  \t   tab
  \\   backslash
  \"   double quote
  \'   single quote


➗  L-06 : Arithmetic Operators
──────────────────────────────────
  7+3  = 10     7-3  = 4
  7*3  = 21     7/3  = 2.33..
  7//3 = 2      7%3  = 1
  2**3 = 8

  //  floor division (chop)
  %   remainder
  **  power


⚖️  L-07 : Comparison Operators
──────────────────────────────────
   ==  equal       !=  not equal
   >   greater     <   less
   >=  gtr/equal   <=  less/equal
   → Result: True or False
   e.g.  age >= 18


🧠  L-08 : Logical Operators
──────────────────────────────────
  and  → both True   → True
  or   → at least one → True
  not  → flip True↔False
  e.g. (age>18 and hasID)


✂️  L-09,10 : Assignment Operators
──────────────────────────────────
  =   assign      +=  add then assign
  -=  subtract    *=  multiply
  /=  divide      //= floor div
  %=  remainder   **= power
  → x += 5   ≡   x = x + 5


🔢  L-11,12,13 : Bitwise Operators
──────────────────────────────────
  &   AND    1 if both bits 1
  |   OR     1 if any bit 1
  ^   XOR    1 if bits differ
  ~   NOT    ~x = -x -1
  <<  shift left   ( ×2ⁿ )
  >>  shift right  ( ÷2ⁿ floor )

  5 & 3  = 1     5 | 3  = 7
  5 ^ 3  = 6     ~5     = -6
  3 << 1 = 6     8 >> 1 = 4