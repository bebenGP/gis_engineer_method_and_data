                         #####JALANIN SCRIPT DI PYCHARM#####
        #####SCRIPT MENGGUNAKAN FUNGSI HEXAGON PADA GENERATE TESSELLATION#####


import arcpy
import os

input_workspace = r'D:\PT LOCATOR LOGIC\PROJECT\P 51 (Hexagone Grids)\input.gdb'
output_workspace = r'D:\PT LOCATOR LOGIC\PROJECT\P 51 (Hexagone Grids)\output.gdb'

arcpy.env.workspace = input_workspace
#fclist = arcpy.ListFeatureClasss("desa")
fclist = arcpy.ListFeatureClasses("desa")

outfc = os.path.join(output_workspace,"tes_hexagone")

bentuk = 'HEXAGON'
ukuran = '153 SquareMeters'

for fc in fclist:
    arcpy.AddMessage('Progress sedang berjalan. . . . .  {}'.format(fc))
    arcpy.GenerateTessellation_management(outfc,
                                          Extent=arcpy.Describe(fc).Extent,
                                          Shape_Type=bentuk,
                                          Size=ukuran,
                                          Spatial_Reference=arcpy.Describe(fc).spatialReference)
    arcpy.AddMessage('{} Selesai'.format(fc))
