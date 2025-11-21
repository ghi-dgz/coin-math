# coin flip math

basically answering the question
how long would it take to get 10 heads in a row?
11 heads?
12????
ok yeah you get the point

# conclusions

f(x) = 2^(x+1)-2
using calc (calcium)
f'(x) = ln(2) * 2^(x+1)
F(x) = 2^(x+1)/ln(2) - 2x + C

| heads | flips |
| - | -   |
| 1 | 2   |
| 2 | 6   |
| 3 | 14  |
| 4 | 30  |
| 5 | 62  |
| 6 | 126 |
| 7 | 254 |
| 8 | 510 |
| 9 | 1022|
| 10| 2046|
| 11| 4094|
| 12| 8190|