bl_info = {
    "name": "XML Importer",
    "author": "Egor",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > XML Import",
    "description": "Imports objects and colors from XML file",
    "category": "Import-Export",
}

import bpy
from .operators.importXML import ImportXMLOperator
from .ui.mainPanel import XMLImportPanel

def register():
    bpy.utils.register_class(ImportXMLOperator)
    bpy.utils.register_class(XMLImportPanel)

def unregister():
    bpy.utils.unregister_class(ImportXMLOperator)
    bpy.utils.unregister_class(XMLImportPanel)

if __name__ == "__main__":
    register()