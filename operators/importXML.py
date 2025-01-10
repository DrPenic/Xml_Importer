import bpy
from ..utils.importXMLdef import import_xml
from ..utils.applyDataToObjects import apply_data_to_objects

class ImportXMLOperator(bpy.types.Operator):
    bl_idname = "import_scene.xml_data"
    bl_label = "Import XML Data"
    
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    
    def execute(self, context):
        color_scheme, objects_data = import_xml(self.filepath)
        apply_data_to_objects(color_scheme, objects_data)
        self.report({'INFO'}, "XML data successfully applied!")
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}