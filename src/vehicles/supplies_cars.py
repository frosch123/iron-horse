import global_constants
from train import SuppliesConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = SuppliesConsist(roster='pony',
                              base_numeric_id=710,
                              gen=2,
                              subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = SuppliesConsist(roster='pony',
                              base_numeric_id=700,
                              gen=3,
                              subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=4)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = SuppliesConsist(roster='pony',
                              base_numeric_id=2850,
                              gen=3,
                              subtype='B')

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = SuppliesConsist(roster='pony',
                              base_numeric_id=2860,
                              gen=4,
                              subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = SuppliesConsist(roster='pony',
                              base_numeric_id=2870,
                              gen=4,
                              subtype='B')

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = SuppliesConsist(roster='pony',
                              base_numeric_id=2880,
                              gen=5,
                              subtype='A')

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = SuppliesConsist(roster='pony',
                              base_numeric_id=2890,
                              gen=5,
                              subtype='B')

    consist.add_unit(type=FreightCar,
                     capacity=45,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])


    #--------------- antelope ----------------------------------------------------------------------


    #--------------- llama ----------------------------------------------------------------------
