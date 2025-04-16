from enum import Enum

class NodeURL(Enum):
    TESTNET: str = "https://rpc.testnet.near.org" # ["https://test.rpc.fastnear.com", "https://rpc.testnet.pagoda.co"]
    MAINNET: str = "https://rpc.mainnet.near.org"

class NetworkID(Enum):
    TESTNET: str = "testnet"
    MAINNET: str = "mainnet"

class DLCContract(Enum):
    TESTNET: str = "dclv2.ref-dev.testnet"
    MAINNET: str = "dclv2.ref-labs.near"

class WrapNEARContract(Enum):
    TESTNET: str = "wrap.testnet"
    MAINNET: str = "wrap.near"

class USDCContract(Enum):
    TESTNET: str = "usdc.fakes.testnet"
    MAINNET: str = "17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1"

class WnearUsdcPoolID(Enum):
    TESTNET: str = "usdc.fakes.testnet|wrap.testnet|100"
    MAINNET: str = "17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1|wrap.near|100"
