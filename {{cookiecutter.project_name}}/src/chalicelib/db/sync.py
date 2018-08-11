from .models import SampleModel


if not SampleModel.exists():
    SampleModel.create_table(
        read_capacity_units=1, 
        write_capacity_units=1, 
        wait=True,
    )
