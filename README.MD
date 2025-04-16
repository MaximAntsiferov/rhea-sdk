СВАП в тестнете с помощью EXPLORERa
1) метод storage_deposit для wrap.testnet
2) метод storage_deposit для usdc.fakes.testnet
3) метод storage_deposit для dclv2.ref-dev.testnet
4) метод ft_transfer_call для обмениваемого токена с агрументами:
receiver_id = dclv2.ref-dev.testnet
amount = 100000000000000000000000 (0.1 NEAR)
msg = "{\"Swap\": {\"pool_ids\": [\"usdc.fakes.testnet|wrap.testnet|100\"], \"output_token\": \"usdc.fakes.testnet\", \"min_output_amount\":\"239299\"}}"

Attached deposit = 1 (1 yNEAR)
GAS * 10 - для тестнета

CВАП через cmd
1) вводим команду
near contract call-function as-transaction wrap.testnet ft_transfer_call json-args
2) вводим аргументы
{"receiver_id": "dclv2.ref-dev.testnet", "amount": "100000000000000000000000", "msg": "{\"Swap\": {\"pool_ids\": [\"usdc.fakes.testnet^|wrap.testnet^|100\"], \"output_token\": \"usdc.fakes.testnet\", \"min_output_amount\": \"239299\"}}"}
3) затем вводим там остальное

СВАП через bash:
near --quiet contract call-function as-transaction wrap.testnet ft_transfer_call json-args '{"receiver_id": "dclv2.ref-dev.testnet", "amount": "100000000000000000000000", "msg": "{\"Swap\": {\"pool_ids\": [\"usdc.fakes.testnet^|wrap.testnet^|100\"], \"output_token\": \"usdc.fakes.testnet\", \"min_output_amount\": \"239299\"}}"}' prepaid-gas '100.0 Tgas' attached-deposit '1 yoctoNEAR' sign-as max-test.testnet network-config testnet sign-with-legacy-keychain send

Получить инфо о пуле:

# TESTNET
near view --quiet --network-id testnet dclv2.ref-dev.testnet get_pool "{\"pool_id\": \"usdc.fakes.testnet|wrap.testnet|100\"}"

# MAINNET
near view --network-id mainnet dclv2.ref-labs.near get_pool "{\"pool_id\": \"17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1|wrap.near|100\"}"


near call $CONTRACT_ID storage_deposit '' --accountId $USER_ID --amount 0.1

export ACCOUNT_ID=bob.testnet
near account create-account sponsor-by-faucet-service $ACCOUNT_ID autogenerate-new-keypair save-to-keychain network-config testnet create
near account view-account-summary max-test.testnet network-config testnet now
near account list-keys max-test.testnet network-config testnet now