
class MenuItem():

    def __init__(self,name,price,cook_time):
        self.name = name
        self.price = price
        self.cook_time = cook_time


class Burger (MenuItem):

    def __init__(self,name,price,patty,patty_q,cook_time,bread="참깨빵"):
        self.estimate = (cook_time * patty_q) + 60
   
        super().__init__(name, price,cook_time)
   
        self.patty = patty
        self.patty_q = patty_q
        self.bread = bread
        self.basic = ["양파", "양상추", "토마토", "피클"]
        self.sold_out = False

class SpecialBurger (Burger):

    def __init__(self,name,price,patty,patty_q,cook_time,special):
        super().__init__(name, price,patty,patty_q,cook_time,bread = "브리오슈번")
        self.special = special

b1 = Burger("치즈버거",5000,"쇠고기+치즈",1,120)

print(b1.name)




class Side(MenuItem):

    def __init__ (self,name,price,cook_time):
        super.__init__(name, price, cook_time)


class Drink(MenuItem):

    def __init__(self,name,price,cook_time=30):
        super.__init__(name, price, cook_time)

class SetMenu ():

    def __init__(self,burgers,sides,drinks):
        self.burgers = burgers
        self.sides = sides
        self.drinks = drinks
        self.name = burgers.name + " 세트"   
        total_price = burgers.price + sides.price + drinks.price
        self.discount = int(total_price * 0.8)


   
 #   계산: self.조리시간 = 최대값(버거_객체.조리시간, 사이드_객체.조리시간, 음료_객체.조리시간)

b1 = Burger("양고기버거",8500,"양고기 패티",1,1200)
b2 = Burger("치즈버거",6500,"체다 치즈 패티",5,120)
b3 = Burger("고기x버거",6500,"x",0,0)

sb1 = SpecialBurger("라면버거",7500,"신라면 패티",1,900,"짜파게티스프")
sb2 = SpecialBurger("고단백버거",8000,"번데기 패티",4,300,"단백질보충제")

s1 = Side("돼지고기튀김",5000,1200)
s2 = Side("육포",4500,60)
s3 = Side("야채샐러드",3500,120)


