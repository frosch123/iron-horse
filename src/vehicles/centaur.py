from train import EngineConsist, DieselEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='centaur',
                            base_numeric_id=3150,
                            name='Centaur',
                            role='heavy_express_1',
                            power=3700,
                            random_reverse=True,
                            gen=6,
                            intro_date_offset=5,  # introduce much earlier than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=95,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist