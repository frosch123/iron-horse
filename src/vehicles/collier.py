import global_constants
from train import Train, SteamTenderLoco

vehicle = SteamTenderLoco(id = 'collier',
            numeric_id = 1240,
            title = 'Collier [Steam]',
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            speed = 45,
            power = 1300,
            weight = 95,
            vehicle_length = 7,
            buy_menu_width = 32,
            loading_speed = 20,
            intro_date = 1900,
            str_type_info = 'COASTER',
            vehicle_life = 40,
            trailing_part_lengths = [4],
            graphics_status = '',)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
