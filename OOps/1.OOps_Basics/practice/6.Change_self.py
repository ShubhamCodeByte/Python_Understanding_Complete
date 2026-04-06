"""
	6. Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects.

"""


class Change():
  def greet(slf):
    print("i have changed the self to other name no impact")



c = Change()

c.greet()
