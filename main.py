class myclass:
    def __init__(self):
        self.my_fav = {'Paris': 500, 'NYC': 600}
    
    def get_extra_cost(self, dist):
        return self.my_fav.get(dist, 0)
    
    def valid_this(self, dist):
        return isinstance(dist, str)  

class passanger:
    def __init__(self, num):
        self.num = num
    
    def valid_number(self):
        print("this working here")
        return isinstance(self.num, int) and self.num > 0

    def for_here_discount(self):
        if 4 < self.num < 10:
            return 0.1
        elif self.num <= 10:
            return 0.2
        else:
            return 0.0

class Plane:
    def __init__(self, dist, num, dur):
        self.myclass = myclass()
        self.passanger = passanger(num)  
        self.total_time = total_time(dur)
        self.dist = dist
        self.seats = 200

    def sum(self):
        if not self.myclass.valid_this(self.dist) or not self.passanger.valid_number() or not self.total_time.is_valid_total_time():
            return -1

        _numbertotal_ = Vacation._costbas  
        _numbertotal_ += self.myclass.get_extra_cost(self.dist)
        _numbertotal_ += self.total_time.get_fee()
        _numbertotal_ -= self.total_time.get_the_best_promo_ever()

        discount = self.passanger.for_here_discount()
        _numbertotal_ = _numbertotal_ - (_numbertotal_ * discount)
        
        return max(int(_numbertotal_), 0)

class total_time:
    def __init__(self, dur):
        self.dur = dur

    def is_valid_total_time(self):
        return isinstance(self.dur, int) and self.dur > 0

    def get_fee(self):
        return 200 if self.dur < 7 else 0

    def get_the_best_promo_ever(self):
        return 200 if self.dur > 30 else 0

class Vacation:
    _costbas_ = 1000

    def __init__(self, dist, num, dur):
        self.myclass = myclass()
        self.passanger = passanger(num)  
        self.total_time = total_time(dur)
        self.dist = dist

    def sum(self):
        if not self.myclass.valid_this(self.dist) or not self.passanger.valid_number() or not self.total_time.is_valid_total_time():
            return -1
        
        _numbertotal_ = Vacation._costbas_  
        _numbertotal_ += self.myclass.get_extra_cost(self.dist)
        _numbertotal_ += self.total_time.get_fee()
        _numbertotal_ -= self.total_time.get_the_best_promo_ever()

        discount = self.passanger.for_here_discount()
        _numbertotal_ = _numbertotal_ - (_numbertotal_ * discount)
        
        return max(int(_numbertotal_), 0)

#main function
def main():
    #inputs
    dist = "Paris"
    num = 5
    dur = 10

    #outputs
    calculator = Vacation(dist, num, dur)
    cost = calculator.sum()

    #printing
    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")

#main event function
if __name__ == "__main__":
    main()
