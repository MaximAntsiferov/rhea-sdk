ACCOUNT_ID = "max-test.testnet"
PRIVATE_KEY = "ed25519:5kkWYBFK2Qy44gLwk2i7ZiAXSgWxoxCjBzaUbZXTERx5uKDZD7w9zau36tfLub2c6TnnSjJP6aubtHFRb1W5S7Js"
POOL_ID = "usdc.fakes.testnet|wrap.testnet|100"

near account view-account-summary max-test.testnet network-config testnet now
near view --network-id testnet dclv2.ref-dev.testnet get_pool "{\"pool_id\": \"usdc.fakes.testnet|wrap.testnet|100\"}"

near view --network-id testnet wrap.testnet ft_transfer_call "{\"receiver_id\": \"dclv2.ref-dev.testnet\", \"amount\": \"100000000000000000000000\", \"msg\": \"{\"Swap\": \"{\"pool_ids\": [\"usdc.fakes.testnet|wrap.testnet|100\"], \"output_token\": \"usdc.fakes.testnet\", \"min_output_amount\":\"239299\"}\"}"


near call --use-account "max-test.testnet" "wrap.testnet" ft_transfer_call "{\"receiver_id\": \"dclv2.ref-dev.testnet\", \"amount\": \"100000000000000000000000\", \"msg\": \"{\"Swap\": \"{\"pool_ids\": [\"usdc.fakes.testnet|wrap.tesnet|100\"], \"output_token\": \"usdc.fakes.testnet\", \"min_output_amount\":\"239299\"}\"}"


{
  "receiver_id": "dclv2.ref-labs.near",
  "amount": "100000000000000000000000",
  "msg": "{\"Swap\":{\"pool_ids\":[\"17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1|wrap.near|100\"],\"output_token\":\"17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1\",\"min_output_amount\":\"239299\"}"
         "}"
}

near call --use-account max-test.testnet --deposit-yocto 1 --gas 300000000000000 --network-id testnet wrap.testnet ft_transfer_call "{\"receiver_id\": \"dclv2.ref-dev.testnet\", \"amount\": \"100000000000000000000000\", \"msg\": \"{\"Swap\": {\"pool_ids\": [\"usdc.fakes.testnet^|wrap.testnet^|100\"], \"output_token\": \"usdc.fakes.testnet\", \"min_output_amount\": \"239299\"}}\"}"

near call --use-account max-test.testnet dclv2.ref-dev.testnet storage_deposit '' --accountId $USER_ID --amount 0.1

--deposit-yocto=1 --private-key="ed25519:5kkWYBFK2Qy44gLwk2i7ZiAXSgWxoxCjBzaUbZXTERx5uKDZD7w9zau36tfLub2c6TnnSjJP6aubtHFRb1W5S7Js"
{"index":0,"kind":{"ExecutionError":"Smart contract panicked: E102: insufficient storage"}}


{"Swap": {"pool_ids": ["usdc.fakes.testnet^|wrap.testnet^|100"], "output_token": "usdc.fakes.testnet", "min_output_amount": "239299"}}
z = {"receiver_id": "dclv2.ref-dev.testnet", "amount": "100000000000000000000000", "msg": {"Swap": "{\"pool_ids\": [\"usdc.fakes.testnet^|wrap.testnet^|100\"], \"output_token\": \"usdc.fakes.testnet\", \"min_output_amount\": \"239299\"}\"}}
print(z)

near contract call-function as-transaction wrap.testnet ft_transfer_call json-args {"receiver_id": "dclv2.ref-dev.testnet", "amount": "100000000000000000000000", "msg": {"Swap": "{\"pool_ids\": [\"usdc.fakes.testnet^|wrap.testnet^|100\"], \"output_token\": \"usdc.fakes.testnet\", \"min_output_amount\": \"239299\"}\"}}