<p align="center">
    <h1 align="center">PL/0 compiler</h1>
    <p align="center"> PL/0 is a programming language, intended as an educational programming language, that is similar to but much simpler than Pascal.</p>
    <p align="center">It was originally introduced in the book <em>Algorithms + Data Structures = Programs</em> by Niklaus Wirth in 1976.</p>
</p>
<p align="center">
    <a href="#"><img src="https://img.shields.io/badge/licence-WTFPL-yellowgreen?style=for-the-badge" alt="WTFPL License" /></a>
    <a href="https://www.python.org/downloads/release/python-396/"><img src="https://img.shields.io/badge/python-3.9.6-blue?style=for-the-badge&logo=python" alt="Python" /></a>
    <a href="https://docs.conda.io/en/latest/miniconda.html"><img src="https://img.shields.io/badge/miniconda-4.10.3-blue?style=for-the-badge&logo=anaconda" alt="Miniconda" /></a>
    <a href="https://ply.readthedocs.io/en/latest/index.html"><img src="https://img.shields.io/badge/ply-3.11-blue?style=for-the-badge" alt="PLY" /></a>
</p>

<h2>Table of contents</h2>

- [Features](#features)
- [To do](#to-do)
- [Grammar](#grammar)
  - [Diagram](#diagram)
  - [BNF](#bnf)
  - [EBNF](#ebnf)
- [Code examples](#code-examples)
- [Development enviroment](#development-enviroment)
  - [Commands](#commands)
- [References](#references)

## Features

- [x] Lexer.
- [x] Parser (Grammar rules).
- [x] AST generation (Nodes)
- [x] Variable declaration detection.

## To do

- [ ] Generation of symbol and address table.
- [ ] Generation of error table.
- [ ] Value assignments to variables.
- [ ] CALL procedures
- [ ] ODD operation
- [ ] IF statements
- [ ] WHILE staments

## Grammar

### Diagram

![Diagram](docs/PL_0%20-%20Flow.png)

### BNF

```
<program> ::= <block> .

<block> ::= <const-decl> <var-decl> <proc-decl> <statement>

<const-decl> ::= CONST <const-assignment-list> ;
              | e

<const-assignment-list> ::= <ident> = <number>
                         | <const-assignment-list> , <ident> = <number>

<var-decl> ::= var <ident-list> ;
            | e

<ident-list> ::= <ident>
              | <ident-list> , <ident>

<proc-decl> ::= <proc-decl> PROCEDURE <ident> ; <block> ;
             | e

<statement> ::= <ident> := <expression>
            | CALL <ident>
            | BEGIN <statement-list> END
            | IF <condition> THEN <statement>
            | WHILE <condition> DO <statement>
            | e

<statement-list> ::= <statement>
                  | <statement-list> ; <statement>

<condition> ::= odd <expression>
             | <expression> <relation> <expression>

<relation> ::= =
            | <>
            | <
            | >
            | <=
            | >=

<expression> ::= <term>
              | <adding-operator> <term>
              | <expression> <adding-operator> <term>

<adding-operator> ::= +
                   | -

<term> ::= <factor>
        | <term> <multiplying-operator> <factor>

<multiplying-operator> ::= *
                        | /

<factor> ::= <ident>
          | <number>
          | ( <expression> )
```

> :pushpin: Notes
>
> 1. `e` denotes the empty string.
> 2. `<ident>` and `<number>`  are  tokens  representing  identifiers  and  numbers, respectively.

### EBNF

```
<program> ::= <block> .

<block> ::= <const-decl> <var-decl> <proc-decl> <statement>

<const-decl> ::= [const <ident> = <number> {, <ident> = <number>} ;]

<var-decl> ::= [var <ident> {, <ident>} ;]

<proc-decl> ::= {procedure <ident> ; <block> ;}

<statement> ::= <ident> := <expression>
             | call <ident>
             | begin <statement> {; <statement>} end
             | if <condition> then <statement>
             | while <condition> do <statement>
             | e

<condition> ::= odd <expression>
             | <expression> <relation> <expression>

<relation> ::= =
            | <>
            | <
            | >
            | <=
            | >=

<expression> ::= [<adding-operator>] <term> {<adding-operator> <term>}

<adding-operator> ::= +
                   | -

<term> ::= <factor> {<multiplying-operator> <factor>}

<multiplying-operator> ::= *
                        | /

<factor> ::= <ident>
          | <number>
          | ( <expression> )
```

> :pushpin: Notes
>
> 1. `e` denotes the empty string.
> 2. `<ident>` and `<number>`  are  tokens  representing  identifiers  and  numbers, respectively.
> 3. Optional constructions are enclosed in square brackets `[]`.
> 4. Constructs repeated zero or more times are enclosed in curly brackets `{}`.

## Code examples

```
VAR x, y;
BEGIN
   x:=1;
   y:=2;
   y:=x+y
END.
```

```
CONST m = 7, n = 85;
VAR x, y, z, q, r;

PROCEDURE multiply;
    VAR a, b;
BEGIN a := x; b := y; z := 0;
    WHILE b > 0 DO
    BEGIN
        IF ODD b THEN z := z + a;
        a := 2 * a; b := b / 2;
    END
END;

PROCEDURE divide;
    VAR w;
BEGIN r := x; q := 0; w := y;
    WHILE w <= r DO  w := 2 * w;
    WHILE w > y DO
        BEGIN  q := 2 * q; w := w / 2;
            IF w <= r THEN
            BEGIN r := r - w; q := q + 1
            END
        END
END;

PROCEDURE gcd;
    VAR f, g;
BEGIN f := x; g := y;
    WHILE f <> g DO
        BEGIN IF f < g THEN g := g - f;
            IF g < f THEN f := f - g;
        END;
    z := f
END;

BEGIN
    x :=  m; y :=  n; CALL multiply;
    x := 25; y :=  3; CALL divide;
    x := 84; y := 36; CALL gcd
END.
```

## Development enviroment

### Commands

1. Create a new conda enviroment from a list of specified packages

    ```bash
    # Command estructure
    conda create --name {env_name} python=3.9.6 ply=3.11
    
    # After creating the enviroment you can install autopep8 for     your IDE
    conda install --name {env_name} autopep8 -y
    ```
    > :pushpin: Notes
    > 
    > Replace `{env_name}` for whatever name you want.

2. Activate the enviroment

    ```bash
    # In the terminal for MacOS / Linux
    # In Anaconda Prompt for Windows
    conda activate {env_name}
    ```
    > :pushpin: Notes
    > 
    > Replace `{env_name}` for whatever name you want.

    Or choose the conda enviroment from your favorite IDE


## References

- [CS485 Project - PL/0 Compiler](https://cs.wmich.edu/~yang/teach/cs485/pl0/)
- [Github repository](https://github.com/dila93/Compilador_PL0)
- [Presentation](https://www.slideserve.com/moke/pl-0-parser-powerpoint-ppt-presentation)
- [Node implementation](https://web.archive.org/web/20200125143809/http://www.cs.columbia.edu:80/~aho/cs4115/Lectures/MineTimeFinalReport.pdf)
