# Посмотреть список пулов
# near view --network-id mainnet v2.ref-finance.near get_pools "{\"from_index\": 0, \"limit\": 10}"
# near contract call-function as-read-only v2.ref-finance.near get_return json-args '{"pool_id": 3, "token_in": "a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.factory.bridge.near", "token_out": "wrap.near", "amount_in": "1000"}' network-config mainnet now

# Посмотреть сколько будет return
# near view --network-id mainnet v2.ref-finance.near get_return "{\"pool_id\": 4512, \"token_in\": \"wrap.near\", \"token_out\": \"17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1\", \"amount_in\": \"100000000000000000000000\"}"

# Посмотреть информацию об аккаунте
# near account view-account-summary voreficna.near network-config mainnet now

# Цены токенов
"https://api.ref.finance/list-token-price"
# Пулы
"https://api.ref.finance/pool/search?type=dcl&sort=tvl&limit=20&labels=&offset=0&hide_low_pool=true&order_by=desc&token_type=&token_list=&pool_id_list="

{"pool_kind": "SIMPLE_POOL", "token_account_ids": ["17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1", "wrap.near"], "amounts": ["1759998522974", "721183232483433975898851571588"], "total_fee": 30, "shares_total_supply": "247516181471439320570858934221", "amp": 0, "farming": false, "token_symbols": ["USDC", "wNEAR"], "update_time": 1743787322, "id": "4512", "tvl": "3519530.730363557", "token0_ref_price": "0.9998230477410316"}
{"pool_kind": "SIMPLE_POOL", "token_account_ids": ["3.contract.portalbridge.near", "wrap.near"], "amounts": ["11495", "4364380249003637045371"], "total_fee": 60, "shares_total_supply": "6170421030682185665453", "amp": 0, "farming": false, "token_symbols": ["USDC", "wNEAR"], "update_time": 1743787322, "id": "4491", "tvl": "0.022143076247568873", "token0_ref_price": "0.9264104225810244"}
{"pool_kind": "DEGEN_SWAP", "token_account_ids": ["aurora", "17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1"], "amounts": ["2310848648144704", "4345021"], "total_fee": 30, "shares_total_supply": "12208284476362615597365816", "amp": 10, "farming": false, "token_symbols": ["ETH", "USDC"], "update_time": 1743787322, "id": "5747", "tvl": "8.485979825951569"}

# DCL Pool

{
                "id": "17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1|wrap.near|100",
                "amp": 0,
                "rates": null,
                "c_amounts": null,
                "shares_total_supply": "",
                "pool_kind": "DCL",
                "token_account_ids": [
                    "17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1",
                    "wrap.near"
                ],
                "amounts": [
                    "501643295301",
                    "678041293894616043315339368028"
                ],
                "token_symbols": [
                    "USDC",
                    "wNEAR"
                ],
                "tvl": "2156025.8283137212707378996877672",
                "volume_24h": "3297633.6205344903500825960172175",
                "fee_volume_24h": "263.8106896427592280066076813774",
                "apy": "0",
                "total_fee": "0.0001",
                "farm_apy": "0",
                "is_farm": false,
                "is_new": false,
                "is_meme": false,
                "farm_is_multi_currency": false,
                "top": false,
                "degens": null
            },

# DEGEN
{
                "id": "5515",
                "amp": 60,
                "rates": null,
                "c_amounts": [
                    "98671965047521641231049385396",
                    "233684451802477818125467306663"
                ],
                "shares_total_supply": "612548357867877731181947517667",
                "pool_kind": "DEGEN_SWAP",
                "token_account_ids": [
                    "wrap.near",
                    "17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1"
                ],
                "amounts": [
                    "98671965047521641231049385396",
                    "233684451802"
                ],
                "token_symbols": [
                    "wNEAR",
                    "USDC"
                ],
                "tvl": "474426.52018406765460376050036624",
                "volume_24h": "173794.27074406452762262829545485",
                "fee_volume_24h": "417.10624978575486629430790909164",
                "apy": "32.0900655201005827485704647288293858805041364023411630507764829",
                "total_fee": "0.003",
                "farm_apy": "0",
                "is_farm": false,
                "is_new": false,
                "is_meme": false,
                "farm_is_multi_currency": false,
                "top": false,
                "degens": [
                    "2448900000000000000000000",
                    "999900000000000000000000"
                ]
            },

# Classic
{
                "id": "4512",
                "amp": 0,
                "rates": null,
                "c_amounts": null,
                "shares_total_supply": "247516220822216331860435108740",
                "pool_kind": "SIMPLE_POOL",
                "token_account_ids": [
                    "17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1",
                    "wrap.near"
                ],
                "amounts": [
                    "1760931597854",
                    "720802240955625056595090419799"
                ],
                "token_symbols": [
                    "USDC",
                    "wNEAR"
                ],
                "tvl": "3519552.06019992101275097702742272",
                "volume_24h": "449879.08354204927792269319997405",
                "fee_volume_24h": "1079.70980050091826701446367993772",
                "apy": "11.19727938220778734890522093626333129402913759360161793893641676",
                "total_fee": "0.003",
                "farm_apy": "0",
                "is_farm": false,
                "is_new": false,
                "is_meme": false,
                "farm_is_multi_currency": false,
                "top": false,
                "degens": null
            },