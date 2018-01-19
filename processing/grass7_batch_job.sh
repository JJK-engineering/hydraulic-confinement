g.proj -c proj4="+proj=longlat +datum=WGS84 +no_defs"
v.in.ogr min_area=0.0001 snap=-1 input="tmp" layer=TestAlignmentLine output=tmp1516308553832 --overwrite -o
g.region n=1274890 s=1260650 e=2624270 w=2603510 res=100
v.to.points  input="tmp1516308553832" dmax="100" use=vertex -i output=output0e592ae5944d4843ae39c2ba7741ac61 --overwrite
v.out.ogr -s -e input=output0e592ae5944d4843ae39c2ba7741ac61 type=auto output="tmp" format=ESRI_Shapefile output_layer=TestAlignmentPoints --overwrite
exit