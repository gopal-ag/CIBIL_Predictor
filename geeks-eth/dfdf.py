# import random
# import keys
# import datetime
# from twilio.rest import Client
# from done import *
# ID = 0
# BLK_ID=90
# def send_sms(commodity, price, amount, phone_number, trans_id, c_score,f_Id,blk_id):
#     now = datetime.datetime.now()
#     today_date = now.strftime("%Y-%m-%d %H:%M")  # Format the date and time
#
#     sms_text = (
#         f"Farmer ID is: {f_Id},\n"
#         f"Block ID is: {blk_id},\n"
#         f"Today's date: {today_date},\n"
#         f"The price is: {price}₹,\n"
#         f"Amount is: {amount} kgs,\n"
#         f"Phone number is: {phone_number},\n"
#         f"Transaction ID is: {trans_id},\n"
#         f"Credit score is: {c_score}"
#
#     )
#     add_info(sms_text)
#
#     client = Client(keys.account_sid, keys.auth_token)
#
#     message = client.messages.create(
#         body=sms_text,
#         from_=keys.twilio_number,
#         to='+91' + str(phone_number)
#     )
#
#     print(message.body)
#
#
# # Initialize a global ID variable
# def get_random_10_digit_number():
#     """Generate a random 10 digit number."""
#     return random.randint(1000000000, 9999999999)
#
#
# def calculate_new_credit_score(previous_score, weight, quality):
#     """Calculate a new credit score based on weighted inputs."""
#
#     # Set the contributions for each component
#     previous_score_weight = 0.6
#     weight_weight = 0.2
#     quality_weight = 0.2
#
#     # Calculate the new score
#     new_score = (previous_score * previous_score_weight) + \
#                 (weight * weight_weight) + \
#                 (quality * quality_weight)
#
#     # Ensure the new score is within bounds
#     new_score = max(0.0, min(1000.0, new_score))
#
#     # Return the rounded new score
#     return round(new_score)
#
#
# class Transaction:
#     """A class to represent a transaction."""
#     def __init__(self, price, weight, quality, date):
#         global BLK_ID
#         self.Price = price
#         self.T_id = get_random_10_digit_number()
#         self.Blk_Id = BLK_ID
#         # BLK_ID increment is removed from here
#         self.date = date
#         self.Weight = weight
#         self.Quality = quality
#
#
# class Farmer:
#     """A class to represent a farmer."""
#     def __init__(self, phone_num):
#         global ID
#         ID += 1
#         self.Farmer_Id = ID
#         self.Phone_num = phone_num
#         self.Credit_Score = 0  # Starting with a base score of 0 for each farmer
#         self.transactions = []
#
#     def add_transaction(self, transaction):
#         """Add a transaction to the farmer's record and update credit score."""
#         self.transactions.append(transaction)
#
#     def update_credit_score(self):
#         """Update the farmer's credit score based on transactions."""
#         global BLK_ID
#         for transaction in self.transactions:
#             self.Credit_Score = calculate_new_credit_score(self.Credit_Score, transaction.Weight, transaction.Quality)
#             # Print details after each transaction
#             print(f"Transaction ID: {transaction.T_id}")
#             # print(f"Block ID: {transaction.Blk_Id}")
#             print(f"Price: {transaction.Price}")
#             print(f"Date: {transaction.date}")
#             print(f"Weight: {transaction.Weight} kg")
#             print(f"Quality: {transaction.Quality}")
#             print(f"Updated Credit Score: {self.Credit_Score}")
#             print("-------------------")
#             send_sms("wheat",transaction.Price,int(transaction.Weight),9811199650,transaction.T_id,self.Credit_Score,self.Farmer_Id,transaction.Blk_Id)
#             BLK_ID += 1  # Increment the BLK_ID here after the SMS is sent
#
# def main():
#     """Main function to create farmers and transactions, then print their details."""
#     num_farmers = 10
#     num_transactions_per_farmer = 5
#     farmers = []
#
#     for i in range(num_farmers):
#         farmer = Farmer(get_random_10_digit_number())
#         for j in range(num_transactions_per_farmer):
#             transaction = Transaction(random.randint(0, 999), 100.0 + random.uniform(0, 500), 0.5 + random.random(), "2023-11-23")
#             farmer.add_transaction(transaction)
#         print(f"Farmer ID: {farmer.Farmer_Id}")
#         print(f"Phone Number: {farmer.Phone_num}")
#         farmer.update_credit_score()
#         print(f"Final Credit Score: {farmer.Credit_Score}")
#         print("-------------------")
#         farmers.append(farmer)
#
#     return farmers
#
# # Run the main function if this file is executed as a script
# if __name__ == "__main__":
#     main()
import random
import datetime
from twilio.rest import Client
# Assume keys and done modules are available and provide necessary functionality
import keys
from blockchain import *

ID = 0
BLK_ID = 90

def send_sms(commodity, price, amount, phone_number, trans_id, c_score, f_Id, blk_id):
    now = datetime.datetime.now()
    today_date = now.strftime("%Y-%m-%d %H:%M")  # Format the date and time
    sms_text = (f"Farmer ID is: {f_Id},\n"
                f"Block ID is: {blk_id},\n"
                f"Today's date: {today_date},\n"
                f"The price is: {price}₹,\n"
                f"Amount is: {amount} kgs,\n"
                f"Phone number is: {phone_number},\n"
                f"Transaction ID is: {trans_id},\n"
                f"Credit score is: {c_score}")
    add_info(sms_text)  # Assume add_info function is defined in the done module
    client = Client(keys.account_sid, keys.auth_token)
    message = client.messages.create(
        body=sms_text,
        from_=keys.twilio_number,
        to='+91' + str(phone_number)
    )
    print(message.body)

def get_random_10_digit_number():
    return random.randint(1000000000, 9999999999)

def calculate_new_credit_score(previous_score, weight, quality):
    previous_score_weight = 0.6
    weight_weight = 0.2
    quality_weight = 0.2
    new_score = (previous_score * previous_score_weight) + \
                (weight * weight_weight) + \
                (quality * quality_weight)
    new_score = max(0.0, min(1000.0, new_score))
    return round(new_score)

class Transaction:
    def __init__(self, price, weight, quality, date):
        global BLK_ID
        self.Price = price
        self.T_id = get_random_10_digit_number()
        self.Blk_Id = BLK_ID
        self.date = date
        self.Weight = weight
        self.Quality = quality

class Farmer:
    def __init__(self, phone_num):
        global ID
        ID += 1
        self.Farmer_Id = ID
        self.Phone_num = phone_num
        self.Credit_Score = 0
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def update_credit_score(self):
        global BLK_ID
        for transaction in self.transactions:
            self.Credit_Score = calculate_new_credit_score(self.Credit_Score, transaction.Weight, transaction.Quality)
            print(f"Transaction ID: {transaction.T_id}")
            print(f"Price: {transaction.Price}")
            print(f"Date: {transaction.date}")
            print(f"Weight: {transaction.Weight} kg")
            print(f"Quality: {transaction.Quality}")
            print(f"Updated Credit Score: {self.Credit_Score}")
            print("-------------------")
            send_sms("wheat", transaction.Price, int(transaction.Weight), self.Phone_num, transaction.T_id, self.Credit_Score, self.Farmer_Id, BLK_ID)
            BLK_ID += 1

def main():
    num_farmers = 10
    num_transactions_per_farmer = 5
    farmers = []

    for i in range(num_farmers):
        farmer = Farmer(get_random_10_digit_number())
        for j in range(num_transactions_per_farmer):
            transaction = Transaction(random.randint(0, 999), 100.0 + random.uniform(0, 500), 0.5 + random.random(), "2023-11-23")
            farmer.add_transaction(transaction)
        print(f"Farmer ID: {farmer.Farmer_Id}")
        print(f"Phone Number: {farmer.Phone_num}")
        farmer.update_credit_score()
        print(f"Final Credit Score: {farmer.Credit_Score}")
        print("-------------------")
        farmers.append(farmer)

    return farmers

if __name__ == "__main__":
    main()
