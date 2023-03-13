import requests
import json


def bankSupply() -> dict:
    bank_supply = requests.get(
        "https://api.osl.zone/cosmos/bank/v1beta1/supply?pagination.limit=2000")
    supply = bank_supply.json()["supply"]
    return (supply)


def pools() -> dict:
    num_pools_call = requests.get(
        "https://api.osl.zone/osmosis/gamm/v1beta1/num_pools")
    num_pools = num_pools_call.json()["num_pools"]
    gamm_pools = requests.get(
        f'https://api.osl.zone/osmosis/gamm/v1beta1/pools?pagination.limit={num_pools}')
    pools = gamm_pools.json()["pools"]
    return (pools)
