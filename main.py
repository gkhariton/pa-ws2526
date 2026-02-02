import numpy as np
import pandas as pd

from functions import functions as fn
from functions import generate_group_name

def main():
    file_path = "data\data_GdD_WiSe2526.h5"
    controllers = ["ARIMA", "DTW", "PID"]
    topologies = ["Coupled", "Decentral", "Central"]
    disruptions = ["BlockageConstant", "BlockageCosine", "PumpOutage", "NoDisruption"]

    group_names = generate_group_name(controllers, topologies, disruptions)
    considered_groups = ["DTW_Coupled_NoDisruption"]

    processed_data = pd.DataFrame(columns=["power_mean", "power_std", "service_loss_mean", "service_loss_std"])
    pass


if __name__ == "__main__":
    main()
