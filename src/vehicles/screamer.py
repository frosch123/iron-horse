import global_constants
from train import Train, DieselMultipleUnit

vehicle = DieselMultipleUnit(id = 'screamer',
            numeric_id = 1370,
            title = 'Screamer [Diesel]',
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            speed = 80,
            power = 3300,
            weight = 125,
            vehicle_length = 8,
            buy_menu_width = 32,
            loading_speed = 20,
            intro_date = 1980,
            str_type_info = 'COASTER',
            vehicle_life = 40,
            graphics_status = '',)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
