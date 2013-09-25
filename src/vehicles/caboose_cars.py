import global_constants
from train import Train, CabooseCar

vehicle = CabooseCar(title = 'Caboose [Car]',
                vehicle_set = 'brit',
                wagon_generation = 1,
                replacement_id = '-none',
                buy_cost = 22,
                fixed_run_cost_factor = 3.5,
                fuel_run_cost_factor = 1.0,
                weight = 25,
                vehicle_length = 5,
                buy_menu_width = 32,
                intro_date = 1860,
                str_type_info = 'COASTER',
                vehicle_life = 40,
                graphics_status = '',)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
