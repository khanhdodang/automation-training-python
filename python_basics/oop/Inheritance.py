# parent class
class Bird:
    
  def __init__(self):
    print("Bird is ready")

  def whoisThis(self):
    print("Bird")

  def swim(self):
    print("Swim faster")

# child class
class Penguin(Bird):

  def __init__(self):
    # call super() function
    super().__init__()
    print("Penguin is ready")

  def whoisThis(self):
    print("Penguin")

  def run(self):
    print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

'''
In the above program, we created two classes i.e. Bird (parent class) and Penguin (child class).
The child class inherits the functions of parent class.
We can see this from the swim() method.

Again, the child class modified the behavior of the parent class.
We can see this from the whoisThis() method.
Furthermore, we extend the functions of the parent class, by creating a new run() method.

Additionally, we use the super() function inside the __init__() method.
This allows us to run the __init__() method of the parent class inside the child class.
'''
