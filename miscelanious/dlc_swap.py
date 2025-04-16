#get-pool
# near view --network-id mainnet dclv2.ref-labs.near get_pool "{\"pool_id\": \"17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1|wrap.near|100\"}"
# near view --network-id mainnet v2.ref-finance.near get_return "{\"pool_id\": 4512, \"token_in\": \"wrap.near\", \"token_out\": \"17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1\", \"amount_in\": \"100000000000000000000000\"}"
x = 1.0001 ** -405733 * 1000000000000000000
print(x)
y = (1/x)
print(y)
raise

# near view --network-id mainnet v2.ref-finance.near get_return "{\"pool_id\": 3, \"token_in\": \"a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.factory.bridge.near\", \"token_out\": \"wrap.near\", \"amount_in\": \"100000\"}"

# 1 NEAR = 100000000000000000000000 # 1 * 10
# "ft_transfer_call"
{
  "receiver_id": "dclv2.ref-labs.near",
  "amount": "100000000000000000000000",
  "msg": "{\"Swap\":{\"pool_ids\":[\"17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1|wrap.near|100\"],\"output_token\":\"17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1\",\"min_output_amount\":\"239299\"}}"
}
