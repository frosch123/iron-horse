from train import PassengerEngineRailcarConsist, DieselRailcarUnit

consist = PassengerEngineRailcarConsist(id='tin_rocket',
                                        base_numeric_id=530,
                                        name='Tin Rocket',
                                        role='pax_railcar',
                                        power=400,
                                        gen=5,
                                        sprites_complete=True,
                                        intro_date_offset=-5)  # introduce early by design

consist.add_unit(type=DieselRailcarUnit,
                 weight=40,
                 vehicle_length=8,
                 capacity=75,
                 chassis='railcar')
