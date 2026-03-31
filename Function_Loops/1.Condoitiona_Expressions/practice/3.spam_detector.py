"""
3. A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.

"""

spam_mail1 = '''If you are looking for the ultimate shortcut to financial freedom, our new masterclass is designed to help you make a lot of money through automated trading systems. We have limited spots available for this exclusive session, so you should buy now to secure the early bird discount. Don't forget to subscribe this weekly newsletter for more tips, and make sure to click this link to finish your registration immediately'''

spam_mail2 = '''Many young entrepreneurs are driven by the ambition to make a lot of money in the tech industry, often focusing on scalable software solutions to reach their financial goals.'''

spam_mail3 = '''The flash sale ends in exactly two hours, urging customers to buy now if they want to save 50% on premium winter apparel.'''

clean_mail = '''The morning sun rose slowly over the quiet valley, casting long shadows across the dew-covered grass. A gentle breeze moved through the trees, carrying the scent of pine and damp earth. It was a perfect day for a long hike, providing a rare opportunity to disconnect from the digital world and focus entirely on the natural beauty of the surrounding mountains.'''

spam_check = spam_mail1

# if((spam_check.find("Make a lot of money") or spam_check.find("buy now") or spam_check.find("subscribe this") or spam_check.find("click this")) != -1):
#    print("Spam Detected !")
# else:
#    print("Safe")

# This is failing all time returning the same thing spam detected
# In Python, your or statement returned -1 (which is truthy) and immediately compared it to -1, making the condition True regardless of whether spam was actually found.

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

if(p1 in spam_check or p2 in spam_check or p3 in spam_check or p4 in spam_check):
  print("Spam Detected !")
else:
  print("Safe .")
