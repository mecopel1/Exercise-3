import arcpy 

arcpy.env.workspace =r'D:\Grad_Spring2019\610-Programming\Exercise3\Exercise 3.gdb'

#Feature class to feature class
inFeatures = 'General_Offense'
outLocation = r'D:\Grad_Spring2019\610-Programming\Exercise3\Exercise 3.gdb'
outFeatureClass = 'Assault'
delimitedField = arcpy.AddFieldDelimiters(arcpy.env.workspace, "OffenseCustom")
expression = delimitedField + " = 'Assault'"
 
arcpy.FeatureClassToFeatureClass_conversion(inFeatures, outLocation, 
                                            outFeatureClass, expression)

print('Yes!')