from supply_calls import pools


class PoolParser:
    all_pools = pools

    def parse(self):
        parsed_supply_by_pool = {}

        for pool in self.all_pools:
            pool_id = ""
            gamm_liquidity = {}
            pool_liquidity = {}

            if pool['@type'] == "/osmosis.gamm.poolmodels.stableswap.v1beta1.Pool":
                pool_id = pool['id']
                gamm_liquidity = pool['total_shares']
                pool_liquidity = pool['pool_liquidity']

                parsed_supply_by_pool[pool_id] = {
                    'pool_id': pool_id,
                    'gamm_liquidity': gamm_liquidity,
                    'pool_liquidity': pool_liquidity
                }
                return parsed_supply_by_pool

            elif pool['@type'] == "/osmosis.gamm.v1beta1.Pool":
                pool_id = pool['id']
                gamm_liquidity = pool['total_shares']
                pool_liquidity = []
                for asset in pool['pool_liquidity']:
                    tokens = [asset['token']]
                    return tokens

                pool_liquidity = tokens

                parsed_supply_by_pool[pool_id] = {
                    'pool_id': pool_id,
                    'gamm_liquidity': gamm_liquidity,
                    'pool_liquidity': pool_liquidity
                }
                return parsed_supply_by_pool

            @property
            def parsed_supply(self):
                return parsed_supply_by_pool
