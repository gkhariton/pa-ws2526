import numpy as np
import pandas as pd


from functions.functions import generate_group_name
from functions.functions import read_metadata

def main():
    file_path = "data/data_GdD_WiSe2526.h5"
    controllers = ["ARIMA", "DTW", "PID"]
    topologies = ["Coupled", "Decentral", "Central"]
    disruptions = ["BlockageConstant", "BlockageCosine", "PumpOutage", "NoDisruption"]

    group_names = generate_group_name(controllers, topologies, disruptions)
    considered_groups = ["DTW_Coupled_NoDisruption"]

    processed_data = pd.DataFrame(columns=["power_mean", "power_std", "service_loss_mean", "service_loss_std"])

    for group in group_names:
        if group not in considered_groups:
            continue

        setpoint = read_metadata(file=file_path, path=group, attr_key="setpoint")

        groups_service_loss = []
        groups_power = []

        for run_id in range(1, 11):
            run_name = f"run_{run_id:02d}"         
            run_path = f"{group}/{run_name}"       

            start_time_index = read_metadata(
                file=file_path,
                path=run_path,
                attr_key="analyse_start_time_index"
        )


if __name__ == "__main__":
    main()
