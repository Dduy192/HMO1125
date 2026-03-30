import os
from ecmwf.opendata import Client
import xarray as xr
import matplotlib.pyplot as plt

# 1. Download data
client = Client(source="ecmwf")
client.retrieve(
    time=0,
    step=24,
    type="fc",
    param="2t",
    target="data.grib2"
)

# 2. Load and subset data (Region: Southeast Asia)
ds = xr.open_dataset("data.grib2", engine="cfgrib")
ds_sub = ds.sel(latitude=slice(25, 5), longitude=slice(100, 115))

# 3. Plot data
plt.figure(figsize=(10, 8))
ds_sub.t2m.plot(cmap="RdYlBu_r")
plt.title("ECMWF 2m Temperature Forecast (+24h)")

# 4. Save to PNG
os.makedirs("output", exist_ok=True)
plt.savefig("output/latest_plot.png")
plt.close()
