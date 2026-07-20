from flask import Flask, jsonify, request, render_template

from app.services.wallet_service import WalletService
from app.services.transaction_service import TransactionService


app = Flask(__name__)


wallet_service = WalletService()
transaction_service = TransactionService()


@app.route("/")
def home():

    return render_template("dashboard.html")


@app.route("/wallet", methods=["POST"])
def create_wallet():

    data = request.get_json()

    wallet = wallet_service.create_wallet(
        data["wallet_id"],
        data["refugee_id"]
    )

    return jsonify({
        "wallet_id": wallet.wallet_id,
        "refugee_id": wallet.refugee_id,
        "balance": wallet.balance,
        "currency": wallet.currency
    })


@app.route("/transaction", methods=["POST"])
def create_transaction():

    data = request.get_json()

    transaction = transaction_service.create_transaction(
        data["transaction_id"],
        data["wallet_id"],
        data["amount"],
        data["transaction_type"],
        data["description"]
    )

    return jsonify({
        "transaction_id": transaction.transaction_id,
        "amount": transaction.amount,
        "description": transaction.description
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT", 8080)), debug=False)
