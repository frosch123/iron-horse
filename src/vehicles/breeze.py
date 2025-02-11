from train import PassengerEngineRailcarConsist, ElectricRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailcarConsist(roster_id=roster_id,
                                            id='breeze',
                                            base_numeric_id=3200,
                                            name='Breeze',
                                            role='pax_railcar_2',
                                            power=650,  # RL EMU HP is much lower, but eh
                                            pantograph_type='z-shaped-single-with-base',
                                            easter_egg_haulage_speed_bonus=True,
                                            gen=5,
                                            sprites_complete=True,
                                            intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarPaxUnit,
                     weight=42,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_3')

    return consist
