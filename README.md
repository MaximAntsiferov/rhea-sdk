# rhea-sdk

[![PyPi Package Version](https://img.shields.io/pypi/v/rhea-sdk?style=flat-square)](https://pypi.org/project/rhea-sdk)
[![Supported python versions](https://img.shields.io/pypi/pyversions/rhea-sdk)](https://pypi.python.org/pypi/rhea-sdk)
[![Twitter](https://img.shields.io/twitter/follow/p_volnov?label=Follow)](https://twitter.com/MaksimA30)

[//]: # ([![downloads]&#40;https://img.shields.io/github/downloads/MaximAntsiferov/rhea-sdk/total?style=flat-square&#41;]&#40;https://pypi.org/project/rhea-sdk&#41;)


**rhea-sdk** is an asynchronous SDK for interacting with Rhea Finance DEX

## Examples
<details>
  <summary>📚 Click to see some basic examples</summary>


**Few steps before getting started...**
- Install near-cli-rs
- Install the latest stable version of rhea-sdk, simply running `pip install rhea-sdk`
- Create NEAR account and get your private key [wallet](https://wallet.near.org/create)

### Usage examples

```python
import asyncio
from rhea_sdk import Rhea

wnear_contract = "wrap.near"
usdc_contract = "17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1"

async def main():
    rhea = Rhea(account_id="example.near", network_id="mainnet", private_key="ed25519:...")
    
    # Get account tokens balance
    near_balance = await rhea.account.get_near_balance()
    usdc_balance = await rhea.account.get_token_balance(usdc_contract)
    wnear_balance = await rhea.account.get_token_balance(wnear_contract)
    
    # Wrap or Unwrap some NEAR
    await rhea.account.wrap_near(0.15)
    await rhea.account.unwrap_near(0.05)
    
    # List all DLC pools
    pools = await rhea.dlc_pool.get_pools()
    
    # Get DLC pool_id by tokens and commission
    pool_id = rhea.dlc_pool.get_pool_id(wnear_contract, usdc_contract, 100)
    
    # Get pool extended info by pool_id
    pool = await rhea.dlc_pool.get_pool(pool_id)
    
    # Get current tokens price in the pool
    prices = await rhea.dlc_pool.get_tokens_price(pool_id)
    
    # Calculate expected output
    amount_to_swap = 0.1
    min_output_amount = amount_to_swap * prices[wnear_contract]
    
    # Swap
    await rhea.dlc_pool.swap(wnear_contract, usdc_contract, pool_id, amount_to_swap, min_output_amount)
```

</details>


## Official rhea-sdk resources:
 - Social media:
   - 🇺🇸 [Telegram](https://t.me/maksim30)
   - 🇺🇸 [Twitter](https://twitter.com/MaksimA30)
 - PyPI: [rhea-sdk](https://pypi.python.org/pypi/rhea-sdk)
 - Documentation: [Github repo](https://github.com/MaximAntsiferov/rhea-sdk)
 - Source: [Github repo](https://github.com/MaximAntsiferov/rhea-sdk)
 - Issues/Bug tracker: [Github issues tracker](https://github.com/MaximAntsiferov/rhea-sdk/issues)

## Contributors

### Code Contributors

This project exists thanks to all the people who contribute.
<a href="https://github.com/MaximAntsiferov/rhea-sdk/graphs/contributors"><img src="https://opencollective.com/rhea-sdk/contributors.svg?width=890&button=false" /></a>
