from app.models.wallet import Wallet


class WalletService:

    def create_wallet(self, wallet_id, refugee_id):

        wallet = Wallet(
            wallet_id=wallet_id,
            refugee_id=refugee_id,
            balance=0,
            currency="USD"
        )

        return wallet
