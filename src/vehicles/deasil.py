from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailcarConsist(roster_id=roster_id,
                                            id='deasil',
                                            base_numeric_id=1770,
                                            name='Deasil',
                                            role='pax_railcar_1',
                                            power=200,
                                            gen=3,
                                            sprites_complete=True,
                                            intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarPaxUnit,
                     weight=30,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_1')

    return consist
