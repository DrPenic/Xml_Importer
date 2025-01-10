import bpy
from mathutils import Matrix, Vector
from collections import defaultdict

def apply_data_to_objects(color_scheme, objects_data):
    print("Applying DATA...")

    references_collection = bpy.data.collections.get("REFERENCES")
    if references_collection is None:
        print("Collection 'REFERENCES' not found!")
        return

    created_objects = {}

    for object_data in objects_data:
        obj_name = object_data['name']
        base_name = obj_name.split('.')[0]

        obj = references_collection.objects.get(base_name)
        if obj is None:
            print(f"Object '{base_name}' not found in the 'REFERENCES' collection!")
            continue

        if base_name in created_objects:
            original_obj = created_objects[base_name]
            new_obj = original_obj.copy()
            new_obj.data = original_obj.data.copy()
            references_collection.objects.link(new_obj)
        else:
            new_obj = obj
            created_objects[base_name] = obj  

        if 'transform' in object_data:
            transform = Vector(object_data['transform'])

        if 'matrix' in object_data:
            raw_matrix = object_data['matrix']

        matrix_3x3 = Matrix(raw_matrix)
        matrix_transposed = matrix_3x3.transposed()
        matrix_4x4 = matrix_transposed.to_4x4()
        print(matrix_4x4)

        translation_matrix = Matrix.Translation(transform)
        print(translation_matrix)

        final_matrix = translation_matrix @ matrix_4x4 
        print(final_matrix)

        new_obj.matrix_world = final_matrix

        # Applying_colors
        if obj.vertex_groups:
            for group in obj.vertex_groups:
                color_name = group.name
                if color_name in color_scheme:
                    color_values = color_scheme[color_name]

                    if not obj.data.vertex_colors:
                        obj.data.vertex_colors.new(name="Color")

                    color_layer = obj.data.vertex_colors["Color"]

                    for poly in obj.data.polygons:
                        for loop_index in poly.loop_indices:
                            color_layer.data[loop_index].color = color_values

    print("Finished applying data to objects.")