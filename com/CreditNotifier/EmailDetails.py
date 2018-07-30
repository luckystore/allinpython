class EmailDetails(object):
    def __init__(self, fi=None,account_no=None,customer_name=None,due_amount=None,due_date=None,email=None):
        self.fi = fi
        self.account_no = account_no
        self.customer_name = customer_name
        self.due_amount = due_amount
        self.due_date = due_date
        self.email = email

