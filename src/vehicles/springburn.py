from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='springburn',
                            base_numeric_id=1790,
                            name='Springburn',
                            power=1200,
                            intro_date=1950)

    consist.add_unit(type=DieselEngineUnit,
                     weight=80,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
