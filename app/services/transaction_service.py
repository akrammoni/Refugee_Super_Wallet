from app.models.transaction import Transaction


class TransactionService:

    def create_transaction(self, transaction_id, wallet_id, amount, transaction_type, description):

        transaction = Transaction(
            transaction_id,
            wallet_id,
            amount,
            transaction_type,
            description
        )

        return transaction
