import bpy

class XMLImportPanel(bpy.types.Panel):
    bl_label = "XML importer"
    bl_idname = "SCENE_PT_xml_import"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'XML Importer'
    def draw(self, context):
        layout = self.layout
        layout.operator("import_scene.xml_data", text="Import XML")