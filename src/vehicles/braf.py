from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='braf',
                            base_numeric_id=0,
                            name='2-6-0 Braf',
                            role='freight_1',
                            power=1250,
                            tractive_effort_coefficient=0.24,
                            gen=2,
                            sprites_complete=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=68,
                     vehicle_length=5,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=30,
                     vehicle_length=3,
                     spriterow_num=1)

    return consist
