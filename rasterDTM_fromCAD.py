# procedure for determining reading DXF file from CAD
# and converting to raster DTM
# and producing hillslpe raster

# project name: 'Nam Ang'

# usage
#  in qgis -> plugins -> python console -> show editor icon -> open in editor -> run

# python setup for qgis processing
import sys, os
from processing.core.Processing import Processing
Processing.initialize()
import processing
from processing.tools import *

# set wd for this procedure and project
os.chdir("/home/kaelin_joseph/DSS.HydraulicConfinement/")

# define required input files
#  check in CAD that elevations (z) are attributed to contour line vertices(required)
DXF = "data/incoming/topo nam ang.dxf"  #DTM with surface topography

# define required input data
# mapping
crs = 'EPSG:32648'  #define crs for project
grass_region = "726000,729500,1670500,1674000"  #map region E1,E2,N1,N2

# define temporary data
contoursDXF = 'tmp/contours.dxf'
vectorDTM = 'tmp/vectorDTM.shp'
vectorDTM_z = 'tmp/vectorDTM_z.shp'
vectorDTM_z_ = 'tmp/vectorDTM_z_.shp'

# define output data
DTM = 'data/incoming/NamAngRasterDTM.tif'
DTM_slope='data/incoming/NamAngRasterSlope.tif'

# read in dxf file and simplify topographical contours
processing.runalg("qgis:simplifygeometries",
                  DXF,1,contoursDXF)

# produce grass vecter DTM
processing.runalg("grass7:v.in.dxf",
                  contoursDXF,"",True,False,True,False,False,True,grass_region,0,vectorDTM)

# set CRS of vector DTM
#processing.runalg("qgis:reprojectlayer",
#                  vectorDTM,crs,vectorDTM_)

# add elevation (z) to attribute table of vector DTM
processing.runalg("qgis:fieldcalculator",
                  vectorDTM,"z",0,10,3,True,"z(start_point($geometry))",vectorDTM_z)

# repair topology of vector DTM
processing.runalg("grass7:v.build.all",  #algorithm not found
                  vectorDTM_z,0,grass_region,-1,0.0001,0,vectorDTM_z_)

# convert contour vector layer to contour raster layer

