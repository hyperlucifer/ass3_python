# define a class date (Day,Month,Year) with function to accept and display it
# Accept date from user.throw a user define exception "invalid date exception" 
# if the date is invalid
class date:
    def __init__(self) -> None:
        self.day=None
        self.Month=None
        self.year=None

    def accept_date(self,d,m,y):
        if(d>0 and d<=31):
            self.day=d
        else:
            raise Exception("invalid date Exception")
        if(m>1 and m<=12):
            self.Month=m
        else:
            raise Exception("invalid date Exception")
        if(y<2024):
            self.year=y
        else:
            raise Exception("invalid date Exception")
    def display(self):
        print(f"the date is {self.day}/{self.Month}/{self.year}")

d=date()
d.accept_date(23,6,1789)
d.display()