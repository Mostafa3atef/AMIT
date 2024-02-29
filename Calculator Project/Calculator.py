class Calculator():
  def __init__(self,first,second):
    self.num1=first
    self.num2=second
  def addition (self):
    return f'{self.num1} + {self.num2} = {self.num1 + self.num2}'
  def subtraction (self,a,b):
    return f'{self.num1} - {self.num2} = {self.num1 - self.num2}'
  def multiplication (self,a,b):
    return f'{self.num1} * {self.num2} = {self.num1 * self.num2}'
  def division (self,a,b):
    return f'{self.num1} / {self.num2} = {self.num1 / self.num2}'
  def tr (self,a,b):
    return f'The area of triangle is = {0.5 * self.num1 * self.num2}'


