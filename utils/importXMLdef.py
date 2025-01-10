import bpy
import xml.etree.ElementTree as ET

def import_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()  # root будет ссылаться на <test_task>
    except Exception as e:
        raise RuntimeError(f"Error parsing XML: {e}")
    
    color_scheme = {}
    objects_data = []

    color_scheme_node = root.find("color_scheme")
    if color_scheme_node is not None:
        for color in color_scheme_node:
            color_name = color.tag
            color_values = list(map(float, color.text.split()))
            color_values.append(1.0)
            color_scheme[color_name] = color_values

    for obj in root:
        if obj.tag.startswith("object_"):
            object_data = {}
            object_data['name'] = obj.find("name").text

            matrix = []
            for row in obj.find("matrix"):
                matrix.append(list(map(float, row.text.split())))
            object_data['matrix'] = matrix

            transform = list(map(float, obj.find("transform").text.split()))
            object_data['transform'] = transform

            objects_data.append(object_data)

    return color_scheme, objects_data