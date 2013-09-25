# list of explicit vehicle ids for locos
buy_menu_sort_order_locos = [# brit locos
                           'standard',
                           'raven',
                           'goods',
                           'metro',
                           'collier',
                           'wordsell',
                           'gresley',
                           'hellenic',
                           'suburban',
                           'chopper',
                           'slammer',
                           'whistler',
                           'zebedee',
                           'gridiron',
                           'screamer',
                           'pendolino',
                            # nagn locos
                           #'dmc_sd40',
                           #'geep'
                           ]

# wagon ids are generic and are composed to specific vehicle ids elsewhere
# order is significant
# format is base_id: num_generations
from ordered_dict_backport import OrderedDict
buy_menu_sort_order_wagons = OrderedDict([('passenger_car', 3),
                                          ('mail_car', 3),
                                          ('box_car', 2),
                                          ('open_car', 2),
                                          ('tank_car', 3),
                                          ('hopper_car', 2),
                                          ('flat_car', 2),
                                          ('livestock_car', 2),
                                          ('reefer_car', 2),
                                          ('covered_hopper_car', 2)])

# shared lists of allowed classes, shared across multiple ship types
base_refits_by_class = {'empty': [],
                       'all_freight': ['CC_BULK', 'CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_LIQUID', 'CC_ARMOURED', 'CC_REFRIGERATED', 'CC_COVERED', 'CC_NON_POURABLE'],
                       'pax': ['CC_PASSENGERS'],
                       'mail': ['CC_MAIL'],
                       'liquids': ['CC_LIQUID'],
                       'packaged_freight': ['CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_ARMOURED', 'CC_LIQUID'],
                       'flatcar_freight': ['CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_ARMOURED', 'CC_LIQUID'],
                       'hopper_freight': [],
                       'covered_hopper_freight': [],
                       'refrigerated_freight': [],
                       'express_freight': ['CC_EXPRESS','CC_ARMOURED']}

# speed for wagons in mph (some generations may optionally have no speed set)
standard_wagon_speed = 75
speedy_wagon_speed = 100

# set <-> numeric id mapping
#vehicle_set_id_mapping = {'univ': 0, 'brit': 1 ,'nagn': 2, 'soam': 3, 'euro': 4}
vehicle_set_id_mapping = {'brit': 1}

# capacity multipliers for capacity parameter
capacity_multipliers = [0.67, 1, 1.33]

# used to construct the cargo table automatically
# ! order is significant ! - openttd will cascade through default cargos in the order specified by the cargo table
cargo_labels = ['PASS', # pax first
                           'TOUR',
                           # "the mail must get through"
                           'MAIL',
                           # bulk-ish cargos
                           'COAL',
                           'IORE',
                           'GRVL',
                           'SAND',
                           'AORE',
                           'CORE',
                           'CLAY',
                           'SCMT',
                           'WOOD',
                           'LIME',
                           # common express-ish / processed cargos
                           'GOOD',
                           'FOOD',
                           'STEL',
                           'FMSP',
                           'ENSP',
                           'BEER',
                           'BDMT',
                           'MNSP',
                           'PAPR',
                           'WDPR',
                           'VEHI',
                           'COPR',
                           'DYES',
                           # liquid-ish cargos
                           'OIL_',
                           'RFPR',
                           'PETR',
                           'PLAS',
                           'WATR',
                           # fish and farm cargos
                           'FISH',
                           'CERE',
                           'FICR',
                           'FRVG',
                           'FRUT',
                           'GRAI',
                           'LVST',
                           'MAIZ',
                           'MILK',
                           'RUBR',
                           'SGBT',
                           'SGCN',
                           'WHEA',
                           'WOOL']

# this is for nml, don't need to use python path module here
graphics_path = 'src/graphics/'

# chameleon templating goes faster if a cache dir is used; this specifies which dir is cache dir
chameleon_cache_dir = 'chameleon_cache'

# cost constants
FIXED_RUN_COST = 500.0
FUEL_RUN_COST = 10.0

# OpenTTD's max date
max_game_date = 5000001

# standard offsets for trains
default_train_offsets = {'1': [[-3, -12], [-14, -14], [-16, -11], [-8, -15], [-3, -12], [-14, -14], [-16, -11], [-8, -15]], # needs fix
                         '2': [[-3, -12], [-14, -14], [-16, -11], [-8, -15], [-3, -12], [-14, -14], [-16, -11], [-8, -15]], # needs fix
                         '3': [[-3, -12], [-14, -14], [-16, -11], [-8, -15], [-3, -12], [-14, -14], [-16, -11], [-8, -15]], # needs fix
                         '4': [[-3, -20], [-6, -18], [0, -11], [-8, -15], [-3, -12], [-14, -14], [-17, -11], [-8, -19]],
                         '5': [[-3, -18], [-8, -17], [-4, -11], [-8, -15], [-3, -12], [-14, -14], [-17, -11], [-8, -18]],
                         '6': [[-3, -16], [-10, -16], [-8, -11], [-8, -15], [-3, -12], [-14, -14], [-17, -11], [-8, -17]],
                         '7': [[-3, -14], [-12, -15], [-12, -11], [-8, -15], [-3, -12], [-14, -14], [-17, -11], [-8, -15]],
                         '8': [[-3, -12], [-14, -14], [-16, -11], [-8, -15], [-3, -12], [-14, -14], [-16, -11], [-8, -15]]}
