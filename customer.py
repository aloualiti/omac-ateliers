class Customer():
    customers=[]
    def __init__(self, customer_name):
        for elem in Customer.customers:
            if elem == customer_name:
                raise ValueError("this customer already exists in the list")
        self.customer_name = customer_name
        Customer.customers.append(customer_name)

        