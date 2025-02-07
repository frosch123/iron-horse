# intermodal containers are sandboxed into their own module to avoid them spawning tentacles into gestalt graphics, global constants, train.py etc

from gestalt_graphics.pipelines import GenerateCompositedIntermodalContainers
from gestalt_graphics.gestalt_graphics import GestaltGraphicsIntermodal

class IntermodalContainerGestalt(object):
    """ Sparse class to hold container gestalts """
    # a gestalt is a set of containers of specific length and appearance
    # each set corresponds to a spritesheet which will be generated by the graphics processor
    # each set is used for a specific group of cargo labels or classes
    # - multiple container types exist, e.g. box, tank, flat, bulk etc
    # - unknown and generic cargos default to box containers)
    # ====== #
    # each container set may have one or more spriterows
    # spriterows are chosen randomly when vehicles load new cargo
    # rows are composed by the graphics processor, and may include variations for
    # - combinations of container lengths
    # - combinations of container types
    # - container colours
    # !!! containers are going to need 'base sets' to allow double stack, cropped for well cars etc
    # !!! the consist needs to encode the set type to fetch the right spritesets
    # !!! base sets will also have to be encoded in gestalts here, unless they're done by (sets * gestalts) combinatorially?
    def __init__(self, container_subtype):
        self.pipeline = GenerateCompositedIntermodalContainers()
        self.container_subtype = container_subtype

    @property
    def floor_height_variants(self):
        # used to handle, e.g. low floor, narrow gauge etc by putting a yoffset in the generated container sprites
        # extend to accomodate double stack later (only one floor height probably)?
        # format is (label, yoffset for floor-height) - leave floor height as 0 for default floor heights
        if self.stack_type == 'single':
            return (('default', 0), ('low_floor', 1))
        else:
            # other values not implemented yet
            raise ValueError()

    @property
    def id(self):
        return "intermodal_" + self.container_subtype + "_" + str(self.length) + "px"


class IntermodalBox16px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 16
        self.stack_type = 'single'
        self.variants = [['box_30_foot_1CC'],
                         ['box_30_foot_2CC'],
                         ['box_30_foot_red']]


class IntermodalBox24px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 24
        self.stack_type = 'single'
        self.variants = [['box_20_foot_1CC', 'box_20_foot_1CC'],
                         ['box_20_foot_1CC', 'box_20_foot_red'],
                         ['box_20_foot_red', 'box_20_foot_1CC'],
                         ['box_40_foot_1CC'],
                         ['box_40_foot_2CC'],
                         ['box_40_foot_red']]


class IntermodalBox32px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 32
        self.stack_type = 'single'
        self.variants = [['box_20_foot_1CC', 'box_20_foot_1CC', 'box_20_foot_1CC'],
                         ['box_20_foot_1CC', 'box_20_foot_1CC', 'box_20_foot_red'],
                         ['box_20_foot_red', 'box_20_foot_red', 'box_20_foot_red'],
                         ['box_20_foot_2CC', 'box_20_foot_2CC', 'box_20_foot_2CC'],
                         ['box_20_foot_1CC', 'box_20_foot_1CC', 'box_20_foot_1CC'],
                         ['box_20_foot_1CC', 'box_40_foot_1CC'],
                         ['box_20_foot_2CC', 'box_40_foot_1CC'],
                         ['box_20_foot_red', 'box_40_foot_red'],
                         ['box_40_foot_1CC', 'box_20_foot_1CC'],
                         ['box_40_foot_2CC', 'box_20_foot_2CC'],
                         ['box_40_foot_2CC', 'box_20_foot_1CC'],
                         ['box_30_foot_1CC', 'box_30_foot_1CC']]


class IntermodalChemicalsTank16px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 16
        self.stack_type = 'single'
        chemicals_tank_30_foot = container_subtype + '_30_foot'
        self.variants = [[chemicals_tank_30_foot]]


class IntermodalChemicalsTank24px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 24
        self.stack_type = 'single'
        chemicals_tank_20_foot = container_subtype + '_20_foot'
        chemicals_tank_40_foot = container_subtype + '_40_foot'
        self.variants = [[chemicals_tank_20_foot, chemicals_tank_20_foot],
                         [chemicals_tank_40_foot]]


class IntermodalChemicalsTank32px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 32
        self.stack_type = 'single'
        chemicals_tank_20_foot = container_subtype + '_20_foot'
        chemicals_tank_30_foot = container_subtype + '_30_foot'
        chemicals_tank_40_foot = container_subtype + '_40_foot'
        self.variants = [[chemicals_tank_20_foot, chemicals_tank_20_foot, chemicals_tank_20_foot],
                         [chemicals_tank_30_foot, chemicals_tank_30_foot],
                         [chemicals_tank_40_foot, chemicals_tank_20_foot],
                         [chemicals_tank_20_foot, chemicals_tank_40_foot]]


class IntermodalCryoTank16px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 16
        self.stack_type = 'single'
        cryo_tank_30_foot = container_subtype + '_30_foot'
        self.variants = [[cryo_tank_30_foot]]


class IntermodalCryoTank24px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 24
        self.stack_type = 'single'
        cryo_tank_20_foot = container_subtype + '_20_foot'
        cryo_tank_40_foot = container_subtype + '_40_foot'
        self.variants = [[cryo_tank_20_foot, cryo_tank_20_foot],
                         [cryo_tank_40_foot]]


class IntermodalCryoTank32px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 32
        self.stack_type = 'single'
        cryo_tank_20_foot = container_subtype + '_20_foot'
        cryo_tank_30_foot = container_subtype + '_30_foot'
        cryo_tank_40_foot = container_subtype + '_40_foot'
        self.variants = [[cryo_tank_20_foot, cryo_tank_20_foot, cryo_tank_20_foot],
                         [cryo_tank_30_foot, cryo_tank_30_foot],
                         [cryo_tank_40_foot, cryo_tank_20_foot],
                         [cryo_tank_20_foot, cryo_tank_40_foot]]


class IntermodalCurtainSide16px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 16
        self.stack_type = 'single'
        curtain_side_30_foot = container_subtype + '_30_foot'
        self.variants = [[curtain_side_30_foot]]


class IntermodalCurtainSide24px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 24
        self.stack_type = 'single'
        curtain_side_40_foot = container_subtype + '_40_foot'
        self.variants = [[curtain_side_40_foot]]


class IntermodalCurtainSide32px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 32
        self.stack_type = 'single'
        curtain_side_30_foot = container_subtype + '_30_foot'
        self.variants = [[curtain_side_30_foot, curtain_side_30_foot]]


class IntermodalEdiblesTank16px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 16
        self.stack_type = 'single'
        self.variants = [['edibles_tank_30_foot']]


class IntermodalEdiblesTank24px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 24
        self.stack_type = 'single'
        self.variants = [['edibles_tank_20_foot', 'edibles_tank_20_foot'],
                         ['edibles_tank_40_foot']]


class IntermodalEdiblesTank32px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 32
        self.stack_type = 'single'
        self.variants = [['edibles_tank_20_foot', 'edibles_tank_20_foot', 'edibles_tank_20_foot'],
                         ['edibles_tank_30_foot', 'edibles_tank_30_foot'],
                         ['edibles_tank_20_foot', 'edibles_tank_40_foot']]


class IntermodalFlat16px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 16
        self.stack_type = 'single'
        self.variants = [['box_30_foot_1CC'],
                         ['box_30_foot_2CC']]


class IntermodalFlat24px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 24
        self.stack_type = 'single'
        self.variants = [['box_20_foot_red', 'empty_20_foot',]]


class IntermodalFlat32px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 32
        self.stack_type = 'single'
        self.variants = [['box_20_foot_red', 'empty_20_foot', 'empty_20_foot']]


class IntermodalLivestock16px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 16
        self.stack_type = 'single'
        self.variants = [['livestock_30_foot']]


class IntermodalLivestock24px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 24
        self.stack_type = 'single'
        self.variants = [['livestock_20_foot', 'livestock_20_foot'],
                         ['livestock_40_foot']]


class IntermodalLivestock32px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 32
        self.stack_type = 'single'
        self.variants = [['livestock_20_foot', 'livestock_20_foot', 'livestock_20_foot'],
                         ['livestock_20_foot', 'livestock_40_foot'],
                         ['livestock_40_foot', 'livestock_20_foot']]


class IntermodalOpenBulk16px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 16
        self.stack_type = 'single'
        bulk_30_foot = container_subtype + '_30_foot'
        self.variants = [[bulk_30_foot]]


class IntermodalOpenBulk24px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 24
        self.stack_type = 'single'
        bulk_20_foot = container_subtype + '_20_foot'
        bulk_40_foot = container_subtype + '_40_foot'
        self.variants = [[bulk_20_foot, bulk_20_foot],
                         [bulk_40_foot]]


class IntermodalOpenBulk32px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 32
        self.stack_type = 'single'
        bulk_20_foot = container_subtype + '_20_foot'
        bulk_30_foot = container_subtype + '_30_foot'
        self.variants = [[bulk_20_foot, bulk_20_foot, bulk_20_foot],
                         [bulk_30_foot, bulk_30_foot]]


class IntermodalReefer16px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 16
        self.stack_type = 'single'
        self.variants = [['reefer_30_foot']]


class IntermodalReefer24px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 24
        self.stack_type = 'single'
        self.variants = [['reefer_20_foot', 'reefer_20_foot'],
                         ['reefer_40_foot']]


class IntermodalReefer32px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 32
        self.stack_type = 'single'
        self.variants = [['reefer_20_foot', 'reefer_20_foot', 'reefer_20_foot'],
                         ['reefer_30_foot', 'reefer_30_foot'],
                         ['reefer_20_foot', 'reefer_40_foot'],
                         ['reefer_40_foot', 'reefer_20_foot']]


class IntermodalTank16px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 16
        self.stack_type = 'single'
        tank_30_foot = container_subtype + '_30_foot'
        self.variants = [[tank_30_foot]]


class IntermodalTank24px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 24
        self.stack_type = 'single'
        tank_20_foot = container_subtype + '_20_foot'
        tank_40_foot = container_subtype + '_40_foot'
        self.variants = [[tank_20_foot, tank_20_foot],
                         [tank_40_foot]]


class IntermodalTank32px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 32
        self.stack_type = 'single'
        tank_20_foot = container_subtype + '_20_foot'
        tank_30_foot = container_subtype + '_30_foot'
        tank_40_foot = container_subtype + '_40_foot'
        self.variants = [[tank_20_foot, tank_20_foot, tank_20_foot],
                         [tank_30_foot, tank_30_foot],
                         [tank_40_foot, tank_20_foot],
                         [tank_20_foot, tank_40_foot]]


class IntermodalWood16px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 16
        self.stack_type = 'single'
        self.variants = [['wood_30_foot']]


class IntermodalWood24px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 24
        self.stack_type = 'single'
        self.variants = [['wood_40_foot']]


class IntermodalWood32px(IntermodalContainerGestalt):
    def __init__(self, container_subtype):
        super().__init__(container_subtype)
        self.length = 32
        self.stack_type = 'single'
        self.variants = [['wood_30_foot', 'wood_30_foot']]


def get_container_gestalts_by_length(vehicle_length):
    result = []
    for container_gestalt in registered_container_gestalts:
        if container_gestalt.length == 4 * vehicle_length:
            result.append(container_gestalt)
    return result

registered_container_gestalts = []

container_type_gestalt_mapping = {'box': [IntermodalBox16px, IntermodalBox24px, IntermodalBox32px],
                                  'bulk': [IntermodalOpenBulk16px, IntermodalOpenBulk24px, IntermodalOpenBulk32px],
                                  'chemicals_tank': [IntermodalChemicalsTank16px, IntermodalChemicalsTank24px, IntermodalChemicalsTank32px],
                                  'cryo_tank': [IntermodalCryoTank16px, IntermodalCryoTank24px, IntermodalCryoTank32px],
                                  'curtain_side': [IntermodalCurtainSide16px, IntermodalCurtainSide24px, IntermodalCurtainSide32px],
                                  'edibles_tank': [IntermodalEdiblesTank16px, IntermodalEdiblesTank24px, IntermodalEdiblesTank32px],
                                  #'flat': [IntermodalFlat16px, IntermodalFlat24px, IntermodalFlat32px], # unused currently
                                  'livestock': [IntermodalLivestock16px, IntermodalLivestock24px, IntermodalLivestock32px],
                                  'reefer': [IntermodalReefer16px, IntermodalReefer24px, IntermodalReefer32px],
                                  'tank': [IntermodalTank16px, IntermodalTank24px, IntermodalTank32px],
                                  'wood': [IntermodalWood16px, IntermodalWood24px, IntermodalWood32px]}

def register_container_gestalt(container_type, container_subtype):
    for gestalt in container_type_gestalt_mapping[container_type]:
        registered_container_gestalts.append(gestalt(container_subtype))

def main():
    # yeah this is fiddly
    # we need to generate both cargo-specific sprites (visible cargo or specific recolour
    # and semi-generic fallback sprites, with specific type of container - tank, box, etc (and generic cargo and/or default recolour)

    # first do the defaults, which will be named xxxxxx_DFLT
    for container_type in container_type_gestalt_mapping.keys():
        if container_type not in ['bulk']: # exclude some types which have no meaningful default (and will fall back to box)
            container_subtype = container_type + '_DFLT'
            register_container_gestalt(container_type, container_subtype)

    # then do the ones with cargo-specific graphics, e.g. bulk_COAL, tank_PETR etc
    for container_subtype in set(GestaltGraphicsIntermodal().cargo_label_mapping.values()):
        if 'DFLT' not in container_subtype: # exclude DFLT, handled explicitly elsewhere
            container_type = container_subtype[0:-5]
            register_container_gestalt(container_type, container_subtype)

    """
    # for knowing how many containers combinations we have in total
    total = 0
    for gestalt in registered_container_gestalts:
        total += len(gestalt.variants)
    print('total variants', total)
    """
