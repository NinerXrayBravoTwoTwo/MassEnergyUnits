### List of errors

* Readme is unfinished
* Book referances need to be corrected to standard format, include ISDN's if possible.


### List of possible projects

* Missing a simple explanation of Spacetime.  A spacetime diagram might help or confuse ...
* Pictures?  If so which ones would help.  Should be referenced from a public Wiki I believe.
* A tool that draw's good spacetime diagrams with hyperbolic graph lines that can be used to
create diagrams for powerpoints and other presentations.  Could this use povray for some diagrams?
* A seperate file for this that includes all the shot designations, type, estimated yeild, aliases.
* Should all shot designations be resolved to Peta Joules instead of tons_tnt?
* I have a simple programs that displays a time countdown expressd in ly, au, miles instead of hours min sec which is kind of neat (and simple)
```
var ly = interval.TotalDays / 365.25;
var au = interval.TotalDays * 173.14463;
var mi = interval.TotalDays * 16.094799;

Console.WriteLine($"{interval.TotalDays:N5} days");
Console.WriteLine("");

Console.WriteLine($"{ly:N8} ly");
Console.WriteLine($"{au:N3} au");
Console.WriteLine(mi > 100 ? $"{mi:N4} billion miles" : $"{mi * 1000:N1} million miles");
```
