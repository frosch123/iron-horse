from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailcarConsist(roster_id=roster_id,
                                            id='tin_rocket',
                                            base_numeric_id=530,
                                            name='Tin Rocket',
                                            role='pax_railcar_1',
                                            power=400,
                                            gen=5,
                                            sprites_complete=True,
                                            intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarPaxUnit,
                     weight=40,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_3')

    return consist
