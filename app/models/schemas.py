"""Model schemas."""
from pydantic import BaseModel, Schema, validator, ValidationError, UrlStr, ConstrainedStr
from typing import List, Union
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime


class FaceType(str, Enum):
    wall = 'Wall'
    roof_celing = 'RoofCeiling'
    floor = 'Floor'
    air_wall = 'AirWall'
    window = 'Window'
    shading = 'Shading'


class ParentFace(BaseModel):
    """Parent face information"""
    id: UUID = Schema(default=None, description="Unique UUID value.")

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    type = 'face'


class Opaque(BaseModel):
    """Opaque Material Schema"""
    type: Enum('Opaque', {'type': 'Opaque'})

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    reflectance:  float = Schema(
        ...,
        ge=0,
        le=1
    )


class Transparent(BaseModel):
    """Transparent Material Schema"""
    type: Enum('Transparent', {'type': 'Transparent'})

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'

    )

    transmittance:  float = Schema(
        ...,
        ge=0,
        le=1
    )


class Plastic(BaseModel):
    """Plastic Material Schema"""
    type: Enum('Plastic', {'type': 'Plastic'})

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    r_reflectance:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    g_reflectance:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    b_reflectance:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    specularity:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    roughness:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    modifier:  str = 'void'


class Glass(BaseModel):
    """Glass Material Schema"""
    type: Enum('Glass', {'type': 'Glass'})

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    r_transmittance:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    g_transmittance:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    b_transmittance:  float = Schema(
        ...,
        ge=0,
        le=1
    )

    refraction_index:  float = Schema(
        ...,
        ge=0,
        le=5
    )

    modifier:  str = 'void'


class Vertex(BaseModel):
    """Individual Vertex Schema"""
    x: float = Schema(..., description='X coordinate of the vertex')
    y: float = Schema(..., description='y coordinate of the vertex')
    z: float = Schema(..., description='z coordinate of the vertex')


class FaceBase(BaseModel):
    """The Base Face model

    Some clever description
    """

    id: UUID = Schema(default=None, description="Unique UUID value.")

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    vertices: List[Vertex] = Schema(
        ...,
        min_items=3
    )

    # TODO: write type assignment based on face normal direction as default value function
    face_type: FaceType = FaceType.wall

    rad_modifier: Union[Opaque, Transparent, Plastic, Glass]

    rad_modifier_dir: Union[Opaque, Transparent,
                            Plastic, Glass] = Schema(default=None)


class ShadeFace(FaceBase):
    """ShadeFace Schema"""
    type: Enum('ShadeFace', {'type': 'ShadeFace'})

    face_type: Enum('Shading', {'face_type': 'Shading'})


class Aperture(FaceBase):
    """Aperture Schema"""
    type: Enum('Aperture', {'type': 'Aperture'})

    face_type: Enum('Window', {'face_type': 'Window'})

    blinds: List[ShadeFace] = []

    parent: ParentFace


class Face(FaceBase):
    """A single model face.

    Some clever description
    """
    type: Enum('Face', {'type': 'Face'})

    apertures: List[Aperture] = Schema(default=[])

class Model(BaseModel):
    """Face by Face Model Schema"""
    type: Enum('Model', {'type': 'Model'})

    id: UUID = Schema(default=None, description="Unique UUID value.")

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    convert_to_meters: float = Schema(
        default=1
    )

    faces: List[Union[Face, ShadeFace]] = Schema(
        default=[]
    )

class ModelOut(BaseModel):
    """Face by Face Model Schema Out"""
    type: Enum('Model', {'type': 'Model'})

    id: UUID = Schema(default=None, description="Unique UUID value.")

    name: str = Schema(
        ...,
        regex=r'^[.A-Za-z0-9_-]*$'
    )

    convert_to_meters: float = Schema(
        default=1
    )

    face_count: int = Schema(
        ...,
        description="Number of faces attached to this model"
    )

    created_at: datetime = Schema(
        None, description="Model creation time.")

    url: UrlStr = Schema(
        ...,
        description='URL to the model',
        example='https://api.pollination.cloud/models/7bd00d58-6485-4ca6-b889-3da6d8df3ee4'
    )

    faces_url: UrlStr = Schema(
        ...,
        description='URL to get faces from this model.',
        example='https://api.pollination.cloud/models/7bd00d58-6485-4ca6-b889-3da6d8df3ee4/faces'
    )