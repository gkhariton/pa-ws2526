import numpy as np
import pandas as pd


from functions.functions import generate_group_name, read_metadata, read_data, cap_service_data, check_negative_values


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

            start_time_index = read_metadata(file=file_path, path=run_path, attr_key="analyse_start_time_index")
            tank_1_pressure = read_data(
                file=file_path,
                path=f"{run_path}/tank_1_pressure"
            )

            pump_1_power = read_data(
                file=file_path,
                path=f"{run_path}/pump_1_power"
            )

            pump_2_power = read_data(
                file=file_path,
                path=f"{run_path}/pump_2_power"
            )

            time = read_data(
                file=file_path,
                path=f"{run_path}/time"
            )

            service_fill = cap_service_data(
                service_data=tank_1_pressure,
                setpoint=setpoint
            )

            if not check_negative_values(pump_1_power):
                print(
                    f"Warning: Negative values in pump_1_power "
                    f"for group {group}, {run_name}"
                )

            if not check_negative_values(pump_2_power):
                print(
                    f"Warning: Negative values in pump_2_power "
                    f"for group {group}, {run_name}"
                )


if __name__ == "__main__":
    main()
