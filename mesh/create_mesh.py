from mom6_bathy.grid import Grid
from mom6_bathy.topo import Topo
import xarray as xr

grid = Grid.from_supergrid('../supergrid/ORCA_gridgen/ocean_hgrid_trimmed.nc')

topo = Topo.from_topo_file(grid, '../topography/topo.sub25.tx1_12v1.GEBCO_2025.edit1.SmL1.0_C1.0.nc', min_depth=9.5, varname="D_interp")

# ESMF mesh file:
topo.write_esmf_mesh("./ESMF_mesh_tx1_12v1_260213.nc")
print('Done!')
