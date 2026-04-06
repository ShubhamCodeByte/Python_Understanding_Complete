"""
5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
"""

class TicketBook():                   # this is the wrong method we need to use the  __init__ to get the attribute
  # noOfSeat = 0                           this is running in every call the seat is not increasing
  # noOfSeat: int                            this is giving the error : AttributeError: 'TicketBook' object has no attribute 'noOfSeat'
  
  def __init__(self,seat):
    self.noOfSeat = seat
  name = ""
  date = ""
  def book(self):
    self.name = input("please enter the name: ")
    self.date = input("please enter the date of treavel: ")
    print(f"{self.name} your ticket is booked on {self.date}.")
    self.noOfSeat = 1             # this will make the noOfseat = 1 only as it is running in the class from starting
    return self.noOfSeat

  def getStatus(self):
    print(f"You have {self.noOfSeat} no of seat.")


def main():
  seat = 0
  s = TicketBook(seat)

  # booking\
  seat = s.book()           # i have passed the seat in this which should be in the initantiation time
  seat += 1


  # status checking
  s.getStatus()

while(1):
  main()
  exit = input("press enter to rebook and type exit to come out")
  if (exit == "exit"):
    break

