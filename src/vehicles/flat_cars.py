from train import FlatCarConsist, FreightCar


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=1170,
                             gen=1,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')

    # no gen 2 for NG, straight to gen 3

    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=1130,
                             gen=3,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')


    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=1370,
                             gen=4,
                             subtype='U',
                             base_track_type='NG',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_ng_16px')

    #--------------- pony ----------------------------------------------------------------------
    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=1140,
                             gen=1,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')

    # no gen 2A, gen 1A continues in pony

    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=1150,
                             gen=2,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=1350,
                             gen=3,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=1160,
                             gen=3,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=2550,
                             gen=3,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')


    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=1560,
                             gen=4,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=2540,
                             gen=4,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_24px')


    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=2530,
                             gen=4,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_32px')


    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=2520,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_greebled_24px')


    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=2510,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_filled_greebled_32px')


    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=1630,
                             gen=6,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_1cc_filled_24px')


    consist = FlatCarConsist(roster_id='pony',
                             base_numeric_id=1640,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')
