from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='flindermouse',
                            base_numeric_id=790,
                            name='Flindermouse',
                            role='heavy_freight_2',
                            power=2500,
                            gen=3,
                            pantograph_type='diamond-double',
                            intro_date_offset=-23,  # introduce earlier than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=65,
                     vehicle_length=6,
                     spriterow_num=0,
                     repeat=2)

    return consist
