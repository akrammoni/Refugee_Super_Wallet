# API Tests

## Create Wallet

POST /wallet

Example:

{
"wallet_id":"RW001",
"refugee_id":"REF001"
}


## Create Aid Transaction

POST /transaction

Example:

{
"transaction_id":"TX001",
"wallet_id":"RW001",
"amount":100,
"transaction_type":"AID",
"description":"Food Assistance"
}

