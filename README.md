# lazy-calculator
Demonstration of lazy evaluation

This a simple calculator that can add, subtract and multiply values in a set of registers.
* Any name consisting of alphanumeric characters is be allowed as register names.
* All input is case insensitive.
* The program either take its input from the standard input stream, or from a file. When the
program is launched with one command line argument, input is read from the file specified in
the argument. When accepting input from file, it is not necessary to include quit to exit the
program.
* Invalid commands are ignored, but are logged to the console

The syntax is quite simple:

 `<register> <operation> <value> `
 
 `print <register> `
 
 `quit `
 
Allowed operations are add, subtract and multiply. Here is a simple example:

 `A add 2 `
 
 `A add 3 `

 `print A `

 `B add 5 `

 `B subtract 2 `

 `print B `
 
 `A add 1 `
 
 `print A `

 `quit `

The output will be:

 `5 `

 `3 `

 `6 `

The calculator also supports using registers as values, with lazy evaluation (evaluated at print), e.g.
A multiply B. Here is one example:

 `a add 10 `

 `b add a `

 `b add 1 `
 
 `print b `

 `QUIT `

The output should be:

 `11 `

Another example:

 `result add revenue `

 `result subtract costs `
 
 `revenue add 200 `
 
 `costs add salaries `

 `salaries add 20 `
 
 `salaries multiply 5 `
 
 `costs add 10 `
 
 `print result `
 
 `QUIT `

The output should be:

 `90 `
