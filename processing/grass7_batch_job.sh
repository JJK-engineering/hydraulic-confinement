g.proj -c proj4="+proj=omerc +lat_0=46.95240555555556 +lonc=7.439583333333333 +alpha=90 +k=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +units=m +no_defs"
r.external input="data/swissALTI3D_.tif" band=1 output=tmp1517066456622 --overwrite -o
g.region n=1274890 s=1260650 e=2624270 w=2603510 res=5.0
r.slope.aspect  elevation="tmp1517066456622" precision=DCELL zscale="1" min_slope="0" slope=slope3b95dd00655a4b5eb28d22903289232b --overwrite
g.region raster=slope3b95dd00655a4b5eb28d22903289232b
r.out.gdal --overwrite -c createopt="TFW=YES,COMPRESS=LZW" input=slope3b95dd00655a4b5eb28d22903289232b output="tmp/swissALTI3D_slope.tif"
exit