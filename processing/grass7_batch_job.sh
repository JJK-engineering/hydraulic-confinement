g.proj -c proj4="+proj=omerc +lat_0=46.95240555555556 +lonc=7.439583333333333 +alpha=90 +k=1 +x_0=2600000 +y_0=1200000 +ellps=bessel +units=m +no_defs"
r.external input="data/swissALTI3D_.tif" band=1 output=tmp1515237942425 --overwrite -o
v.in.ogr min_area=0.0001 snap=-1 input="tmp" layer=TestBuffer output=tmp1515237942426 --overwrite -o
g.region n=1274890.0 s=1260650.0 e=2624270.0 w=2603510.0 res=5.0
r.what  map="tmp1515237942425" points="tmp1515237942426" null_value="NA" separator="," cache="500" -n > tmp/test_buffer.csv --overwrite
exit