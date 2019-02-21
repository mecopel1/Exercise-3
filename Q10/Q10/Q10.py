import arcpy

arcpy.env.overwriteOutput=True
arcpy.env.workspace= r'D:\Grad_Spring2019\610-Programming\Exercise3\Exercise 3.gdb'

#create a spatial join
targetFeature='Tracts'
joinFeature='General_Offense'
outputFeature='Joined'

arcpy.SpatialJoin_analysis(targetFeature, joinFeature, outputFeature)