from train import PassengerVeryHighSpeedCabEngineConsist, ElectricHighSpeedPaxUnit


def main(roster_id):
    consist = PassengerVeryHighSpeedCabEngineConsist(roster_id=roster_id,
                                                     id='helm_wind_cab',
                                                     base_numeric_id=3060,
                                                     name='Helm Wind Cab',
                                                     role='very_high_speed',
                                                     power=1700,
                                                     dual_headed=True,
                                                     pantograph_type='z-shaped-single',
                                                     gen=5,
                                                     intro_date_offset=-3,  # introduce earlier than gen epoch by design
                                                     sprites_complete=True)

    consist.add_unit(type=ElectricHighSpeedPaxUnit,
                     weight=76,
                     # no pax capacity on Helm Wind cabs
                     capacity=0,
                     spriterow_num=0,
                     chassis='4_axle_solid_express_32px',
                     tail_light='very_high_speed_32px_1')

    return consist
