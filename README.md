# PL/0 Compiler (Modified)

## Grammar

### BNF

```bnf
<program> ::= <block> .

<block> ::= <const-decl> <var-decl> <proc-decl> <statement>

<const-decl> ::= const <const-assignment-list> ; | e

<const-assignment-list> ::= <ident> = <number>
            | <const-assignment-list> , <ident> = <number>

<var-decl> ::= var <ident-list> ; | e

<ident-list> ::= <ident> | <ident-list> , <ident>

<proc-decl> ::= <proc-decl> procedure <ident> ; <block> ; | e

<statement> ::= <ident> := <expression>
            | call <ident>
            | begin <statement-list> end
            | if <condition> then <statement>
            | while <condition> do <statement>
            | e

<statement-list> ::= <statement> | <statement-list> ; <statement>

<condition> ::= odd <expression> | <expression> <relation> <expression>

<relation> ::= = | <> | < | > | <= | >=

<expression> ::= <term> | <adding-operator> <term>
            | <expression> <adding-operator> <term>

<adding-operator> ::= + | -

<term> ::= <factor> | <term> <multiplying-operator> <factor>

<multiplying-operator> ::= * | /

<factor> ::= <ident> | <number> | ( <expression> )
```
> **Notes**
>
> 1. `e` denotes the empty string.
> 2. `<ident>` and `<number>`  are  tokens  representing  identifiers  and  numbers, respectively.

### EBNF

```bnf
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

<condition> ::= odd <expression> | <expression> <relation> <expression>

<relation> ::= = | <> | < | > | <= | >=

<expression> ::= [<adding-operator>] <term> {<adding-operator> <term>}

<adding-operator> ::= + | -

<term> ::= <factor> {<multiplying-operator> <factor>}

<multiplying-operator> ::= * | /

<factor> ::= <ident> | <number> | ( <expression> )
```
> Notes.
>
> 1. Optional constructions are enclosed in square brackets `[]`.
> 2. Constructs repeated zero or more times are enclosed in curly brackets `{}`.

## Code examples

```pl
var x, y;
begin
   x:=1;
   y:=2;
   y:=x+y;
end.
```
```pl
const i = 10; var x, y;
procedure p;
   var i, j;
   begin
      i := 5;
      x := 4 * i
   end;
begin
   x := i;
   call p;
   y := x * i
end.
```

```pl
const m=7,n=85;
var x,y,z,q,r;
procedure multiply;
   var a,b;
   begin a:=x; b:=y; z:=0;
      while b>0 do
      begin
         if odd b then z:=z+a;
          a:=2*a; b:=b/2;
      end
   end;
procedure divide;
   var w;
   begin r:=x; q:=0; w:=y;
      while w <= r do w:=2*w;
      while w > y do
      begin
         q:=2*q; w:=w/2;
         if w <= r then
         begin
            r:=r-w; q:=q+1
         end
      end
   end;
procedure gcd;
   var f,g;
   begin f:=x; g:=y;
   while f<>g do
      begin
         if f<g then g:=g-f;
         if g<f then f:=f-g;
      end;
   z:=f
   end;

begin
   x:=m; y:=n; call multiply;
   x:=25; y:=3; call divide;
   x:=84; y:=36; call gcd
end.
```

