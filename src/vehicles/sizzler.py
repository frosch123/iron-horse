from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='sizzler',
                        base_numeric_id=2180,
                        name='Sizzler',
                        role='express_2',
                        power=7400,
                        type_base_buy_cost_points=63,  # dibble buy cost for game balance
                        random_reverse=True,
                        intro_date=2025)  # explicit intro date by design

consist.add_unit(type=ElectricEngineUnit,
                 weight=82,
                 vehicle_length=8,
                 spriterow_num=0)

