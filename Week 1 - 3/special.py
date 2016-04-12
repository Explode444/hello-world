words = {
0: "",
1: "one",
2: "two",
3: "three",
4: "four",
5: "five",
6: "six",
7: "seven",
8: "eight",
9: "nine",
10: "ten",
11: "eleven",
12: "twelve",
13: "thirteen",
14: "fourteen",
15: "fifteen",
16: "sixteen",
17: "seventeen",
18: "eighteen",
19: "nineteen",
20: "twenty",
30: "thirty",
40: "forty",
50: "fifty",
60: "sixty",
70: "seventy",
80: "eighty",
90: "ninety",
100: "one"}

total = ""
for num in range(1, 1000):
    
    
    ones = num % 10
    rest = num - ones
    huns = rest / 100 
    tens = rest - huns * 100

 #   print "huns", huns, "tens", tens, "ones", ones
    if huns > 0:
        hundred = "hundred"
        if ones > 0 or tens > 0:
            hundred += "and"
    else:
        hundred = ""

    if tens >= 10 and tens < 20:

        tens = 0
        ones += 10
    
    print words[huns] + hundred  + words[tens] + words[ones] 
    total += words[huns] + hundred  + words[tens] + words[ones] 
    
total += "onethousand"
print "length:", len(total)