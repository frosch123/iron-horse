from train import EngineConsist, ElectricLoco

consist = EngineConsist(id='electrico',
                        base_numeric_id=180,
                        title='Electrico 2-B+B-2 [Electric]',
                        power=2400,
                        speed=75,
                        type_base_buy_cost_points=35,  # dibble buy cost for game balance
                        type_base_running_cost_points=-10,  # dibble running costs for game balance
                        intro_date=1920)

consist.add_unit(type=ElectricLoco,
                 weight=140,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
