import arcpy

arcpy.env.overwriteOutput=True
arcpy.env.workspace=r'D:\Grad_Spring2019\610-Programming\Exercise3\Exercise 3.gdb'

#Add a new field
in_table='CallsforService'
field_name='Crime_Explanation'
arcpy.AddField_management (in_table, field_name, 'TEXT')

#Update field using a different feature class
featureClass=r'D:\Grad_Spring2019\610-Programming\Exercise3\Exercise 3.gdb\CallsforService' 
fields=['CFSType','Crime_Explanation']

with arcpy.da.UpdateCursor(featureClass,fields) as cursor:
    for row in cursor:    
        if row[0]=='Burglary Call':
           row[1]='This is a burglary'
        cursor.updateRow(row)