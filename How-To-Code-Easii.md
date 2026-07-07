# How to code Easii:

### Creating and running a `.es` file:

- To create a `.es` file, into the terminal type, `easii create (filename)`
- To run a file, into the terminal type, `easii ./(filename).es`

### Defining a variable using `var`:

- Separated by spaces, the first component after `var`, is the variable name, and the third is the variable value.
- e.g. `var name = Bob`
- Variables can also be redefined later using the same syntax.

### The `write` instructions:

- Writing anything after the `write` instruction with a space, will write it in the console.
- e.g. `write Hello, World!`, would output, `Hello, World!`
- They can also use variables like this!
- e.g. `write My name is {name}!`, would output, `My name is Bob!`