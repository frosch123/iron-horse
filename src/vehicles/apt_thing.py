from train import PassengerEngineVeryHighSpeedConsist, ElectricPaxUnit

consist = PassengerEngineVeryHighSpeedConsist(id='apt_thing',
                                              base_numeric_id=3060,
                                              name='Helm Wind',
                                              role='pax_high_speed',
                                              power=1200,
                                              gen=4,
                                              intro_date_offset=20)  # introduce later than gen epoch by design

# 4 units (2-tiles) because building these is annoying if the units are too small?
# or 2 units (1-tile) to make any integer length?

consist.add_unit(type=ElectricPaxUnit,
                 weight=31,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=0,
                 chassis='4_axle_solid_express_32px',
                 repeat=2)
