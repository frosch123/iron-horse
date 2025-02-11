from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='wyvern',
                            base_numeric_id=2950,
                            name='Wyvern',
                            role='heavy_express_3',
                            power=2000,
                            random_reverse=True,
                            gen=4,
                            intro_date_offset=-5,  # let's not have everything turn up in 1960
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=110,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
