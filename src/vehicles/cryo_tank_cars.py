from train import CryoTankCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = CryoTankCarConsist(roster='pony',
                             base_numeric_id=20,
                             gen=4,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_sparse_16px')

    consist = CryoTankCarConsist(roster='pony',
                             base_numeric_id=50,
                             gen=4,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_sparse_24px')

    consist = CryoTankCarConsist(roster='pony',
                             base_numeric_id=60,
                             gen=4,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_sparse_32px')

    consist = CryoTankCarConsist(roster='pony',
                             base_numeric_id=80,
                             gen=5,
                             subtype='A',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_sparse_16px')

    consist = CryoTankCarConsist(roster='pony',
                             base_numeric_id=90,
                             gen=5,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_sparse_24px')

    consist = CryoTankCarConsist(roster='pony',
                             base_numeric_id=150,
                             gen=5,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_sparse_32px')

    # gen 6A not included - could add?

    """
    consist = CryoTankCarConsist(roster='pony',
                             base_numeric_id=180,
                             gen=6,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     vehicle_length=4,
                     chassis='2_axle_sparse_16px')
    """

    consist = CryoTankCarConsist(roster='pony',
                             base_numeric_id=190,
                             gen=6,
                             subtype='B',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     vehicle_length=6,
                     chassis='4_axle_sparse_24px')

    consist = CryoTankCarConsist(roster='pony',
                             base_numeric_id=200,
                             gen=6,
                             subtype='C',
                             sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     vehicle_length=8,
                     chassis='4_axle_sparse_32px')
