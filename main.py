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


if __name__ == "__main__":
    main()
