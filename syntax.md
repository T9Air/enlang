# Language Syntax Documentation

## Variables

- Declared implicitly.
- Variables can be:
  - Strings: `x is now "String"`
  - Numbers: `x is now 90`
  - Boolean: `x is now <true/false>`
  - Other variables:

    ```enlang
    x is now 90
    y is now x
    ```

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
- Supported inputs:
  - Strings: `"String"`
  - Numbers: `90`
  - Boolean: `<true/false>`
  - Variables: `var1`

## Conditionals

- Begins with `if <condition>`
- Optional `however if <condition>`
  - Unlimited amount
- Optional `otherwise` block
- Example:

  ```enlang
  if 1 == 2
      output "Impossible"
  however if 1 == 3
      output "Oops"
  hovewer if 1 == 4
      output "Come on!"
  otherwise
      output "Always runs"
  ```

## Nested Conditionals

- It's possible to place an `if` inside another `if`, `however if`, or `otherwise` block.
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
