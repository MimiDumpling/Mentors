import collections
"""
Implement a class that tracks
transactions between peers.

- aggregate
- summary of who owes what
- collect transactions
- save state so you can see balance
"""

class BillTracker(object):
    "Collects and reports transactions."

    def __init__(self):
        self.people = collections.defaultdict(lambda: collections.defaultdict(int))
        
    def log_transaction(self, payer, payee, amount):
        # check if payee/payer are in the dict
        # add/edit their data based on amount owed
        # self.people[payee] = collections.defaultdict(int)
        self.people[payee][payer] += amount
        
    def get_balance(self, payer, payee):
        # check the dict for who owes what
        if self.people[payee][payer]:
            amount = self.people[payee][payer]
            print "{} owes {} {}".format(payer, payee, str(amount))
        else:
            print "{} doesn't owe {} money.".format(payer, payee)

    def summary(self):
        # go thru whole dict.
        # maybe only print the negative numbers
        for payee, payer_dict in self.people.iteritems():
            for payer, amount in payer_dict.iteritems():
                if amount < 0:
                    self.get_balance(payer, payee)


bt = BillTracker()
bt.log_transaction('Jill', 'Bob', -50)
bt.get_balance("Jill", "Bob")
bt.summary()

        # bob : {
        #     jill: -50,
        #     stan: -20,
        # } 

        # mary : {
        #     bob: -70,
        # }

        # jill : {
        #     bob: 50,
        # }
