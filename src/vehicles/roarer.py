from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='roarer',
                            base_numeric_id=2230,
                            name='Roarer',
                            role='heavy_express_2',
                            power=3200,
                            random_reverse=True,
                            gen=4,
                            pantograph_type='z-shaped-double',
                            intro_date_offset=3,  # introduce later than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=80,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
