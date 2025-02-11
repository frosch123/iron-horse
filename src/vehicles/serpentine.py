from train import PassengerEngineMetroConsist, MetroUnit


def main(roster_id):
    consist = PassengerEngineMetroConsist(roster_id=roster_id,
                                          id='serpentine',
                                          base_numeric_id=460,
                                          name='Serpentine',
                                          role='pax_metro',
                                          power=600,
                                          gen=1,
                                          sprites_complete=True)

    # should be 4 units not 2, would look nicer short, but eh, painting
    consist.add_unit(type=MetroUnit,
                     weight=36,
                     capacity=120,
                     chassis='railcar_32px',
                     tail_light='metro_32px_1',
                     repeat=2)

    return consist
