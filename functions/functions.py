from typing import Any, Dict, List, Optional, Tuple, Union

import h5py as h5
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from numpy.typing import NDArray
#from plotid.publish import publish
#from plotid.tagplot import tagplot


def generate_group_name(
    controller: Union[str, List[str]],
    topology: Union[str, List[str]],
    disruption: Union[str, List[str]],
) -> List[str]:
    # if variable is String, convert to List
    if isinstance(controller, str):
        controller = [controller]
    if isinstance(topology, str):
        topology = [topology]
    if isinstance(disruption, str):
        disruption = [disruption]

    group_name = []

    for C in controller:
        for T in topology:
            for D in disruption:
                group_name.append(f"{controller}_{topology}_{disruption}")
    return group_name


def read_metadata(file: str, path: str, attr_key: str) -> Any:
        try:
            with h5.File(file, "r") as h5file:
                if path not in h5file:
                    print(f"Warning: Path '{path} not found in HDF5 file.")
                    return None
                
                obj = h5file[path]

                if attr_key not in obj.attrs:
                    print(f"Warning: Attribute '{attr_key}' not found at path '{path}'.")
                    return None
                
                return obj.attrs[attr_key]
            

        except (OSError, FileNotFoundError):
            print(f"Warning: Could not open HDF5 file '{file}'.")
            return None
    


def read_data(file: str, path: str) -> Optional[NDArray]:
    try:
        with h5.File(file, "r") as h5file:
            
            if path not in h5file:
                print(f"Warning: Path '{path}' not found in HDF5 file.")
                return None

            obj = h5file[path]

            
            if not isinstance(obj, h5.Dataset):
                print(f"Warning: Path '{path}' does not point to a dataset.")
                return None

            data = np.asarray(obj[()])

            
            if data.ndim == 0:
                data = data.reshape(1)
            elif data.ndim != 1:
                data = data.ravel()

            return data

    except (OSError, FileNotFoundError):
        print(f"Warning: Could not open HDF5 file '{file}'.")
        return None
    pass


def cap_service_data(service_data: NDArray, setpoint: float) -> NDArray:
    pass


def check_negative_values(array: NDArray) -> bool:
    pass


def integral_with_time_step(data: NDArray, time_steps: NDArray) -> float:
    pass


def calculate_service_loss(service_fill: float, service_target: float) -> float:
    pass


def convert_Ws_to_Wh(energy_in_Ws: float) -> float:
    pass


def calculate_mean_and_std(data: List[float]) -> Tuple[float, float]:
    pass


def save_dataframe_in_hdf5_with_metadata(
    df: pd.DataFrame,
    hdf5_path: str,
    group_name: str,
    metadata: Dict[str, Any],
) -> None:
    pass


def read_plot_data(
    file_path: str, group_path: str
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    pass


def plot_service_loss_vs_power(
    processed_data: pd.DataFrame, plot_format_data: Dict[str, str]
) -> Figure:
    pass


def publish_plot(
    fig: Figure, source_paths: Union[str, List[str]], destination_path: str
) -> None:
    pass
