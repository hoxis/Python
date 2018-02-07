def cheese_andcrackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "we can just give the function numbers directly: "
cheese_andcrackers(20, 30)

print "or, we can use variables from our script: "
amount_of_cheese = 10
amount_of_crackers = 50

cheese_andcrackers(amount_of_cheese, amount_of_crackers)

print "we can even do math inside too:"
cheese_andcrackers(10+20, 3+9)

print "And we can combine the two, variables and math:"
cheese_andcrackers(amount_of_cheese + 100, amount_of_cheese+111)