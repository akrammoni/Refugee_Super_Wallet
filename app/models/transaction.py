class Transaction:

    def __init__(self, transaction_id, wallet_id, amount, transaction_type, description):

        self.transaction_id = transaction_id
        self.wallet_id = wallet_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
