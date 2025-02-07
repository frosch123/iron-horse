from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='bush_elephant',
                            base_numeric_id=2000,
                            name='2-6-6-2 Bush Elephant',
                            power=2200,
                            base_track_type='NG',
                            intro_date=1915)

    consist.add_unit(type=SteamEngineUnit,
                     weight=128,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=52,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist
