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