from train import EngineConsist, ElectricLoco

consist = EngineConsist(id='electra',
                        base_numeric_id=170,
                        title='Electra [Electric]',
                        power=2400,
                        tractive_effort_coefficient=0.32,
                        speed=90,
                        type_base_buy_cost_points=10,  # dibble buy cost for game balance
                        intro_date=1935)  # explicit intro date by design

consist.add_unit(type=ElectricLoco,
                 weight=105,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
