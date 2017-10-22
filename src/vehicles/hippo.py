from train import EngineConsist, DieselLoco

consist = EngineConsist(id='hippo',
                        base_numeric_id=1870,
                        title='Hippo [Diesel]',
                        power=3600,
                        track_type='NG',
                        speed=55,
                        intro_date=1975)

consist.add_unit(type=DieselLoco,
                 weight=130,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
