from train import EngineConsist, DieselEngineUnit


def main():    # roughly an SAR 91-000 class
    consist = EngineConsist(id='bigfoot',
                            base_numeric_id=1620,
                            name='Bigfoot',
                            power=900,
                            base_track_type='NG',
                            intro_date=1970)

    consist.add_unit(type=DieselEngineUnit,
                     weight=50,
                     vehicle_length=5,
                     spriterow_num=0)

    return consist
