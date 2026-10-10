# -*- coding: utf-8 -*-
"""Lists all rooms in the active model."""
from pyrevit import revit, DB, script

doc = revit.doc
output = script.get_output()

rooms = (DB.FilteredElementCollector(doc)
         .OfCategory(DB.BuiltInCategory.OST_Rooms)
         .WhereElementIsNotElementType()
         .ToElements())

output.print_md('## Rooms in model: {}'.format(len(rooms)))
output.print_table(
    table_data=[[r.Number, r.get_Parameter(DB.BuiltInParameter.ROOM_NAME).AsString()]
                for r in rooms],
    columns=['Number', 'Name'])
