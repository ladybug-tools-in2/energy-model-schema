model_sample = {
    "convert_to_meters": 1,
    "type": "Model",
    "name": "face_by_face_model",
    "faces": [
        {
            "name": "floor",
            "face_type": "Floor",
            "type": "Face",
            "parent": {
                "name": "south_room",
                "type": "zone"
            },
            "rad_modifier": {
                "modifier": "void",
                "type": "Plastic",
                "name": "generic_floor",
                "r_reflectance": 0.2,
                "g_reflectance": 0.2,
                "b_reflectance": 0.2,
                "specularity": 0,
                "roughness": 0
            },
            "rad_modifier_dir": {
                "type": "Opaque",
                "name": "black",
                "reflectance": 0
            },
            "vertices": [
                {
                    "x": 0,
                    "y": 0,
                    "z": 3.2
                },
                {
                    "x": -4.242640687119285,
                    "y": 4.242640687119286,
                    "z": 3.2
                },
                {
                    "x": -1.2727922061357848,
                    "y": 7.212489168102785,
                    "z": 3.2
                },
                {
                    "x": 2.9698484809835,
                    "y": 2.9698484809834995,
                    "z": 3.2
                }
            ]
        },
        {
            "name": "ceiling",
            "face_type": "RoofCeiling",
            "type": "Face",
            "parent": {
                "name": "south_room",
                "type": "zone"
            },
            "rad_modifier": {
                "modifier": "void",
                "type": "Plastic",
                "name": "generic_roof",
                "r_reflectance": 0.8,
                "g_reflectance": 0.8,
                "b_reflectance": 0.8,
                "specularity": 0,
                "roughness": 0
            },
            "rad_modifier_dir": {
                "type": "Opaque",
                "name": "black",
                "reflectance": 0
            },
            "vertices": [
                {
                    "x": 0,
                    "y": 0,
                    "z": 7.4
                },
                {
                    "x": 2.9698484809835,
                    "y": 2.9698484809834995,
                    "z": 7.4
                },
                {
                    "x": -1.2727922061357848,
                    "y": 7.212489168102785,
                    "z": 7.4
                },
                {
                    "x": -4.242640687119285,
                    "y": 4.242640687119286,
                    "z": 7.4
                }
            ]
        },
        {
            "name": "back_wall",
            "type": "Face",
            "parent": {
                "name": "south_room",
                "type": "zone"
            },
            "face_type": "Wall",
            "rad_modifier": {
                "modifier": "void",
                "type": "Plastic",
                "name": "generic_wall",
                "r_reflectance": 0.5,
                "g_reflectance": 0.5,
                "b_reflectance": 0.5,
                "specularity": 0,
                "roughness": 0
            },
            "rad_modifier_dir": {
                "type": "Opaque",
                "name": "black",
                "reflectance": 0
            },
            "vertices": [
                {
                    "x": 0,
                    "y": 0,
                    "z": 3.2
                },
                {
                    "x": 2.9698484809835,
                    "y": 2.9698484809834995,
                    "z": 3.2
                },
                {
                    "x": 2.9698484809835,
                    "y": 2.9698484809834995,
                    "z": 7.4
                },
                {
                    "x": 0,
                    "y": 0,
                    "z": 7.4
                }
            ],
            "apertures": [
                {
                    "name": "back_glazing",
                    "face_type": "Window",
                    "type": "Aperture",
                    "parent": {
                        "name": "back_wall",
                        "type": "face"
                    },
                    "rad_modifier": {
                        "modifier": "void",
                        "type": "Glass",
                        "name": "generic_glass",
                        "r_transmittance": 0.6,
                        "g_transmittance": 0.6,
                        "b_transmittance": 0.6,
                        "refraction_index": 1.52
                    },
                    "vertices": [
                        {
                            "x": 0.7778174593052024,
                            "y": 0.7778174593052023,
                            "z": 3.9000000000000004
                        },
                        {
                            "x": 2.1920310216782974,
                            "y": 2.192031021678297,
                            "z": 3.9000000000000004
                        },
                        {
                            "x": 2.1920310216782974,
                            "y": 2.192031021678297,
                            "z": 5.9
                        },
                        {
                            "x": 0.7778174593052024,
                            "y": 0.7778174593052023,
                            "z": 5.9
                        }
                    ]
                }
            ]
        },
        {
            "name": "right_wall",
            "type": "Face",
            "parent": {
                "name": "south_room",
                "type": "zone"
            },
            "face_type": "Wall",
            "rad_modifier": {
                "modifier": "void",
                "type": "Plastic",
                "name": "generic_wall",
                "r_reflectance": 0.5,
                "g_reflectance": 0.5,
                "b_reflectance": 0.5,
                "specularity": 0,
                "roughness": 0
            },
            "rad_modifier_dir": {
                "type": "Opaque",
                "name": "black",
                "reflectance": 0
            },
            "vertices": [
                {
                    "x": 2.9698484809835,
                    "y": 2.9698484809834995,
                    "z": 3.2
                },
                {
                    "x": -1.2727922061357848,
                    "y": 7.212489168102785,
                    "z": 3.2
                },
                {
                    "x": -1.2727922061357848,
                    "y": 7.212489168102785,
                    "z": 7.4
                },
                {
                    "x": 2.9698484809835,
                    "y": 2.9698484809834995,
                    "z": 7.4
                }
            ]
        },
        {
            "name": "front_wall",
            "type": "Face",
            "parent": {
                "name": "south_room",
                "type": "zone"
            },
            "face_type": "Wall",
            "rad_modifier": {
                "modifier": "void",
                "type": "Opaque",
                "name": "generic_wall",
                "reflectance": 0.5
            },
            "rad_modifier_dir": {
                "type": "Opaque",
                "name": "black",
                "reflectance": 0
            },
            "vertices": [
                {
                    "x": -1.2727922061357848,
                    "y": 7.212489168102785,
                    "z": 3.2
                },
                {
                    "x": -4.242640687119285,
                    "y": 4.242640687119286,
                    "z": 3.2
                },
                {
                    "x": -4.242640687119285,
                    "y": 4.242640687119286,
                    "z": 7.4
                },
                {
                    "x": -1.2727922061357848,
                    "y": 7.212489168102785,
                    "z": 7.4
                }
            ]
        },
        {
            "name": "left_wall",
            "type": "Face",
            "parent": {
                "name": "south_room",
                "type": "zone"
            },
            "face_type": "Wall",
            "rad_modifier": {
                "modifier": "void",
                "type": "Opaque",
                "name": "generic_wall",
                "reflectance": 0.5
            },
            "rad_modifier_dir": {
                "type": "Opaque",
                "name": "black",
                "reflectance": 0
            },
            "vertices": [
                {
                    "x": 0,
                    "y": 0,
                    "z": 3.2
                },
                {
                    "x": 0,
                    "y": 0,
                    "z": 7.4
                },
                {
                    "x": -4.242640687119285,
                    "y": 4.242640687119286,
                    "z": 7.4
                },
                {
                    "x": -4.242640687119285,
                    "y": 4.242640687119286,
                    "z": 3.2
                }
            ]
        }
    ]
}