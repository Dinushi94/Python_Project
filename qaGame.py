print("HI! There What's Up")

ans = input("Are you ready to play (yes/no):")

score = 0
totalQ = 5

if ans.lower() == 'yes':
    ans = input('1. What is the most basic language Microsoft made?')

    if ans.lower() == ".NET namespace":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

        ans = input('2. What does PHP stand for')

        if ans.lower() == " Personal Home Page ":
            score += 1
            print("Correct")
        else:
            print("Incorrect")

        ans = input('3.  var value = Math.pow(0, 10); document.write("<br />Fourth Test Value : " + value ); Type question here?')

        if ans.lower() == "Fourth Test value:0":
            score += 1
            print("Correct")
        else:
            print("Incorrect")

        ans = input('4. Which HTML attribute is used to define inline styles?')

        if ans.lower() == "style":
            score += 1
            print("Correct")
        else:
            print("Incorrect")

        ans = input('5. Who is making the Web standards?')

        if ans.lower() == " The World Wide Web Consortium":
            score += 1
            print("Correct")
        else:
            print("Incorrect")

        #else:
 #   print("Come next Time")


#if ans.lower() == "yes":

        print("Thank you for playing ")
        print("you got ", score, " question correct.")

        mark = (score/totalQ)*100

        print("Mark:", str(mark) + '%')

print("GoodBye!")
print("Have a Nice Day")



