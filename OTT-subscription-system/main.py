from User import User

user1 = User("user1",{"Netflix":20,"AmazonPrime":10,"HotStar":50})
total_bill = user1.get_subscription()
print("total bill to be paid by user1 is {}".format(total_bill))

user2 = User("user2",{"Netflix":10,"AmazonPrime":0,"HotStar":100})
total_bill = user2.get_subscription()
print("total bill to be paid by user1 is {}".format(total_bill))


user1 = User("user1",{"Netflix":10,"AmazonPrime":2})
total_bill = user1.get_subscription()
print(total_bill)