from py_near.account import Account
import asyncio
from py_near.dapps.core import NEAR

ACCOUNT_ID = "max-test.testnet"
PRIVATE_KEY = "ed25519:5kkWYBFK2Qy44gLwk2i7ZiAXSgWxoxCjBzaUbZXTERx5uKDZD7w9zau36tfLub2c6TnnSjJP6aubtHFRb1W5S7Js"

from py_near.providers import JsonProvider

provider = JsonProvider(["https://test.rpc.fastnear.com", "https://rpc.testnet.pagoda.co"])

async def main():
    account = Account(account_id=ACCOUNT_ID, private_key=PRIVATE_KEY, rpc_addr="https://rpc.testnet.pagoda.co")
    await account.startup()
    print(await account.get_balance() / NEAR)
    print(await account.fetch_state())
    raise

    # ref_contract = "v2.ref-finance.near"
    # usdc_contract = "17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1"
    # bridged_usdc_contract = "a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.factory.bridge.near"
    # near_and_briged_usdc_pool_id = 3
    ref_contract = "ref-finance-101.testnet"
    usdc_contract = "usdc.fakes.testnet"

    amount_in = 1 * 10 ** 24   # 1 NEAR

    actions = [
        {
            "pool_id": 6,  # NEAR<>wNEAR pool (check current pool ID on Ref Finance)
            # "token_in": "wrap.near",  # technically we're swapping NEAR which gets wrapped
            "token_in": "wrap.testnet",
            "token_out": usdc_contract,
            "amount_in": str(amount_in),
            "min_amount_out": "0", # You might want to set a minimum to prevent slippage
        }
    ]

    result = await account.function_call(
        contract_id=ref_contract,
        method_name="swap",
        args={
            "actions": actions
        },
    )

    print("Swap successful!")
    print("Transaction result:", result)

asyncio.run(main())



"max-test"
"bird royal ghost memory dumb gather tackle endorse trick copy moment claw"
"ed25519:5kkWYBFK2Qy44gLwk2i7ZiAXSgWxoxCjBzaUbZXTERx5uKDZD7w9zau36tfLub2c6TnnSjJP6aubtHFRb1W5S7Js"



# # Define the parameters for the swap
# token_in = "wNEAR"  # Token you are swapping from
# token_out = "nDAI"  # Token you are swapping to
# amount_in = 1_000_000_000_000_000_000  # Amount in yoctoNEAR (1 NEAR = 10^24 yoctoNEAR)
#
# # Create the swap transaction
# swap_transaction = {
#     "receiver_id": "dclv2.ref-labs.near",
#     "actions": [
#         {
#             "type": "swap",
#             "params": {
#                 "token_in": token_in,
#                 "token_out": token_out,
#                 "amount_in": amount_in,
#                 "min_amount_out": 0,  # Set minimum amount to receive
#             }
#         }
#     ]
# }
#
# # Send the transaction
# response = account.function_call(
#     contract_id="dclv2.ref-labs.near",
#     method_name="swap",
#     args=swap_transaction,
#     gas=200_000_000_000_000,  # Adjust gas limit as needed
#     attached_deposit=0  # No deposit needed for the swap
# )
#
# print("Swap transaction response:", response)



### ОКРУЖЕНИЕ
# export function getConfig(
#   env: string | undefined = ENV ||
#     process.env.NEAR_ENV ||
#     process.env.REACT_APP_REF_SDK_ENV
# ) {
#   ENV = env;
#   switch (env) {
#     case 'mainnet':
#       return {
#         networkId: 'mainnet',
#         nodeUrl: 'https://rpc.mainnet.near.org',
#         walletUrl: 'https://wallet.near.org',
#         WRAP_NEAR_CONTRACT_ID: 'wrap.near',
#         REF_FI_CONTRACT_ID: 'v2.ref-finance.near',
#         REF_TOKEN_ID: 'token.v2.ref-finance.near',
#         indexerUrl: 'https://indexer.ref.finance',
#         explorerUrl: 'https://testnet.nearblocks.io',
#         REF_DCL_SWAP_CONTRACT_ID: 'dclv2.ref-labs.near',
#       };
#     case 'testnet':
#       return {
#         networkId: 'testnet',
#         nodeUrl: 'https://rpc.testnet.near.org',
#         walletUrl: 'https://wallet.testnet.near.org',
#         indexerUrl: 'https://testnet-indexer.ref-finance.com',
#         WRAP_NEAR_CONTRACT_ID: 'wrap.testnet',
#         REF_FI_CONTRACT_ID: 'ref-finance-101.testnet',
#         REF_TOKEN_ID: 'ref.fakes.testnet',
#         explorerUrl: 'https://testnet.nearblocks.io',
#         REF_DCL_SWAP_CONTRACT_ID: 'dclv2.ref-dev.testnet',
#       };
#     default:
#       return {
#         networkId: 'mainnet',
#         nodeUrl: 'https://rpc.mainnet.near.org',
#         walletUrl: 'https://wallet.near.org',
#         REF_FI_CONTRACT_ID: 'v2.ref-finance.near',
#         WRAP_NEAR_CONTRACT_ID: 'wrap.near',
#         REF_TOKEN_ID: 'token.v2.ref-finance.near',
#         indexerUrl: 'https://indexer.ref.finance',
#         explorerUrl: 'https://nearblocks.io',
#         REF_DCL_SWAP_CONTRACT_ID: 'dclv2.ref-labs.near',
#       };
#   }
# }