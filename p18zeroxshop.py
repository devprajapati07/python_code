typexerox_price=15
pagexerox_price=5

# xerorx_type

print("   sir select your zerox type   ")


xerox_type = (int(input("enter number of pages to type print ")))
xerox_pages=(int(input("enter number of pages to print")))

total_priceof_typexerox = xerox_type  * typexerox_price
total_priceof_pagexerox = xerox_pages * pagexerox_price

total_bill = total_priceof_typexerox + total_priceof_pagexerox

print("sir your total bill ==> ",total_bill)

print("   thank you for visiting us   ")