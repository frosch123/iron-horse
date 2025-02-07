from train import PassengerEngineRailcarConsist, ElectroDieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailcarConsist(roster_id=roster_id,
                                            id='zeus',
                                            base_numeric_id=3210,
                                            name='Zeus',
                                            role='pax_railcar_2',
                                            power=850,  # RL EMU HP is much lower, but eh
                                            power_by_railtype={'RAIL': 360, 'ELRL': 850}, # bit nerfed on diesel, by design
                                            pantograph_type='z-shaped-single-with-base',
                                            easter_egg_haulage_speed_bonus=True,
                                            gen=6,
                                            sprites_complete=True,
                                            intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectroDieselRailcarPaxUnit,
                     weight=45,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_2')

    return consist
