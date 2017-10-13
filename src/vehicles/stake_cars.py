import global_constants
from train import StakeConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = StakeConsist(roster='pony',
                         base_numeric_id=2740,
                         gen=2,
                         subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = StakeConsist(roster='pony',
                         base_numeric_id=2730,
                         gen=3,
                         subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = StakeConsist(roster='pony',
                         base_numeric_id=2750,
                         gen=3,
                         subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = StakeConsist(roster='pony',
                         base_numeric_id=1710,
                         gen=4,
                         subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = StakeConsist(roster='pony',
                         base_numeric_id=2760,
                         gen=4,
                         subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = StakeConsist(roster='pony',
                         base_numeric_id=930,
                         gen=5,
                         subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = StakeConsist(roster='pony',
                         base_numeric_id=2770,
                         gen=5,
                         subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = StakeConsist(roster='pony',
                         base_numeric_id=2780,
                         gen=6,
                         subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)

    consist = StakeConsist(roster='pony',
                         base_numeric_id=2790,
                         gen=6,
                         subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0)
    # --------------- antelope ----------------------------------------------------------------------

    #--------------- llama ----------------------------------------------------------------------