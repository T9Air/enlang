# Language Syntax Documentation

## Variables

- Declared implicitly.
- Example: `x is now 10`

## Comments

- Start comments with `Comment:`
- Comments must not be on a line with other code
- Do not put comments on the last line of a file
- Examples:

  ```enlang
  Comment: This is a comment
  ```

## Printing

- Use the `output` keyword followed by a string, number, or variable.
- Example: `output "Hello"` or `output x`

## Input

- Use `input` to read user input into a variable.
- Example: `x is now input`

## Operators

- Supported: `plus`, `minus`, `times`, `divide`
- Translates to standard +, -, *, /

## Comparisons

- `==`, `!=`, `>`, `<`, `>=`, `<=`
- Used in conditionals and loops

## Conditionals

- Begins with `if <condition>`
- Optional `otherwise` block
- Example:

  ```enlang
  if 1 == 2
      output "Impossible"
  otherwise
      output "Always runs"
  ```

## Nested Conditionals

- It's possible to place an `if` inside another `if` or inside an `otherwise` block.
- Example:

  ```enlang
  if x == 10
      if x == 10
          output "Nested condition met"
  otherwise
      output "Outer condition not met"
  ```

## Loops

- For loop: `repeat <number> times`
  
  ```enlang
  repeat 5 times
      output "Hi"
  ```

- While loop: `repeat until <condition>`

  ```enlang
  repeat until x == 0
      output "In loop"
  ```

## Nested Loops

- For loops and while loops can be nested.
- Example:

  ```enlang
  repeat 2 times
      repeat until y == 5
          output "Nested loops example"
  ```

## Random Numbers

- Generate random numbers using `number between <min> and <max>`
- Can use variables or numbers as the minimum and maximum
- Can be used in assignments and output statements
- Examples:

  ```enlang
  x is now number between 1 and 10
  output number between 1 and total
  ```

## Functions

- Create with `create <functionName>`
- Run with `run <functionName>`
- Example:

  ```enlang
  create greet
      output "Hello"
  run greet
  ```

## Function Details

- Currently no function arguments or return values are supported.
- Example:

  ```enlang
  create sample
      output "Sample function"
  run sample
  ```

## Edge Cases

- Variables can be assigned any data type.
- Division by zero raises a runtime error.
