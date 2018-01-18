# python setup for qgis processing
#import sys
#from qgis.core import *
#from PyQt4.QtGui import *
#app = QApplication([], True)
#QgsApplication.setPrefixPath("/usr", True)
#QgsApplication.initQgis()
#sys.path.append('/usr/share/qgis/python/plugins')
# impport qgis procesing
#from processing.core.Processing import Processing
#Processing.initialize()
#from processing.tools import *
#import processing

# points to line
def v_in_lines(input_file_points_csv,output_file_line_shp):
    import sys
#    from qgis.core import *
#    from PyQt4.QtGui import *
    from qgis.core import QgsApplication
    from PyQt4.QtGui import QApplication
    app = QApplication([], True)
    QgsApplication.setPrefixPath("/usr", True)
    QgsApplication.initQgis()
    sys.path.append('/usr/share/qgis/python/plugins')
    # impport qgis procesing
    from processing.core.Processing import Processing
    Processing.initialize()
#    from processing.tools import *
    from processing.tools import general
#    import processing
    # grass7:v.in.lines  #using general.runalg instead of processing.runalg
    general.runalg("grass7:v.in.lines",input_file_points_csv,",",False,
                      "2605158.67928,2621471.50192,1265877.44552,1269377.45567",0,output_file_line_shp)

# line to station points
def v_to_points(input_file_line_shp, output_file_points_shp):
    import sys
#    from qgis.core import *
#    from PyQt4.QtGui import *
    from qgis.core import QgsApplication
    from PyQt4.QtGui import QApplication
    app = QApplication([], True)
    QgsApplication.setPrefixPath("/usr", True)
    QgsApplication.initQgis()
    sys.path.append('/usr/share/qgis/python/plugins')
    # impport qgis procesing
    from processing.core.Processing import Processing
    Processing.initialize()
#    from processing.tools import *
    from processing.tools import general
#    import processing
    #grass7:v.to.points
    general.runalg("grass7:v.to.points",input_file_line_shp,"100",1,True,
                      "2603510,2624270,1260650,1274890",-1,0.0001,0,output_file_points_shp)

__all__ = ('v_in_lines', 'v_to_points')
