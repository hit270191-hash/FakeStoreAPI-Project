import random
import datetime
from faker import Faker
from datamodels.Product import Product
from datamodels.User import User
from datamodels.Address import Address
from datamodels.Name import Name
from datamodels.Geolocation import Geolocation
from datamodels.CartProduct import CartProduct
from datamodels.Carts import Carts

class Payloads:
    faker = Faker()
    categories= ['electronics', 'furniture', 'clothing', 'books', 'beauty']

    def product_payload(self) ->Product:

        title = self.faker.sentence(nb_words= 5)
        price = float(self.faker.pricetag().replace("$","").replace(",",""))
        description = self.faker.sentence(nb_words= 6)
        category= random.choice(self.categories)
        image = "https://i.pravatar.cc/100"

        return Product(title,price,description,category,image)


    def user_payload(self) ->User:

        firstname= self.faker.first_name()
        lastname= self.faker.last_name()
        name= Name(firstname,lastname)

        lat= self.faker.latitude()
        lng= self.faker.longitude()
        geolocation = Geolocation(str(lat),str(lng))

        city= self.faker.city()
        street= self.faker.street_name()
        number= random.randint(1,100)
        zipcode= self.faker.zipcode()
        address= Address(city, street, number, zipcode, geolocation)

        #user
        email= self.faker.email()
        username= self.faker.user_name()
        password= self.faker.password()
        phone= self.faker.phone_number()

        return User(email,username,password,name,address,phone)

    def cart_payload(self,userId: int) -> Carts:
        # userId= self.faker.userId()
        date= str(datetime.date.today())
        product_id= self.faker.random_int(1,100)
        quantity= self.faker.random_int(1,10)
        cart_product= CartProduct(productId=product_id,quantity=quantity)

        return Carts(userId= userId, date= date, products= [cart_product])





# from dataclasses import dataclass
#
# @dataclass
# class GeoLocation:
#     lat: str
#     long: str
#
#
# @dataclass
# class Address:
#     city: str
#     street: str
#     number: int
#     zipcode: str
#     geolocation: GeoLocation
#
#
# @dataclass
# class Name:
#     firstname: str
#     lastname: str
#
#
# @dataclass
# class User:
#     id: int
#     email: str
#     username: str
#     password: str
#     name: Name
#     address: Address
#     phone: str