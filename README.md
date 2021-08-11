# PL/0 (1976) Compiler

## Grammar

### Diagram

![Diagram](docs/PL_0%20-%20Flow.png)

### ENF

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
> Notes.
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

