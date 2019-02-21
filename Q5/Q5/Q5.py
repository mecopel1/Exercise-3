import arcpy
import os
arcpy.env.overwriteOutput = True 

#Create a file geodatabase
folderPath=r'D:\Grad_Spring2019\610-Programming\Exercise3'
gdbName='Q5.gdb'
arcpy.CreateFileGDB_management(folderPath, gdbName)
print('Created geodatabase')

#Feature classes variables
arcpy.env.workspace=r'D:\Grad_Spring2019\610-Programming\Exercise3\Q5.gdb'
featureList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities', 'Rivers']
path=r'D:\Grad_Spring2019\610-Programming\Exercise3\Q5.gdb'
for feature in featureList:
	arcpy.CreateFeatureclass_management(path,feature)
print('Created feature classes')
