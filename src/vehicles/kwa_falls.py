from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id='kwa_falls',
                        base_numeric_id=1970,
                        title='2-8-2 Kwa Falls [Steam]',
                        power=1800,
                        tractive_effort_coefficient=0.19,
                        track_type='NG',
                        speed=75,
                        intro_date=1945)

consist.add_unit(type=SteamLoco,
                 weight=100,
                 vehicle_length=7,
                 spriterow_num=0)

consist.add_unit(type=SteamLocoTender,
                 weight=40,
                 vehicle_length=5,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
