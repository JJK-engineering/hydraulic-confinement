g.proj -c proj4="+proj=longlat +datum=WGS84 +no_defs"
v.in.ogr min_area=0.0001 snap=-1 input="tmp" layer=TestAlignmentLine output=tmp1516294948822 --overwrite -o
g.region n=1274890 s=1260650 e=2624270 w=2603510 res=100
v.to.points  input="tmp1516294948822" dmax="100" use=vertex -i output=outputdb1d7f70a67b424ea6d807b058aec42c --overwrite
v.out.ogr -s -e input=outputdb1d7f70a67b424ea6d807b058aec42c type=auto output="tmp" format=ESRI_Shapefile output_layer=TestAlignmentPoints --overwrite
exit