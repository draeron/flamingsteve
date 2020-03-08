# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fpixel.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.grpc_ecosystem.grpc_gateway.third_party.googleapis.google.api import annotations_pb2 as github_dot_com_dot_grpc__ecosystem_dot_grpc__gateway_dot_third__party_dot_googleapis_dot_google_dot_api_dot_annotations__pb2
from github.com.grpc_ecosystem.grpc_gateway.protoc_gen_swagger.options import annotations_pb2 as github_dot_com_dot_grpc__ecosystem_dot_grpc__gateway_dot_protoc__gen__swagger_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fpixel.proto',
  package='fpixels',
  syntax='proto3',
  serialized_options=b'\222A5\022 \n\027Flame Pixels Controller2\0050.1.0\032\016localhost:8080*\001\001',
  serialized_pb=b'\n\x0c\x66pixel.proto\x12\x07\x66pixels\x1aZgithub.com/grpc-ecosystem/grpc-gateway/third_party/googleapis/google/api/annotations.proto\x1aSgithub.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger/options/annotations.proto\"\x0e\n\x0c\x45mptyRequest\"\x0c\n\nEmptyReply\"7\n\x13ListSensorsResponse\x12 \n\x07sensors\x18\x01 \x03(\x0b\x32\x0f.fpixels.Device\"\"\n\x14SensorRawDataRequest\x12\n\n\x02id\x18\x01 \x01(\t\"(\n\x15SensorRawDataResponse\x12\x0f\n\x07payload\x18\x01 \x01(\t\":\n\x14ListDisplaysResponse\x12\"\n\x08\x64isplays\x18\x01 \x03(\x0b\x32\x10.fpixels.Display\"\x19\n\x0b\x44rawRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x7f\n\x06\x44\x65vice\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x12\x10\n\x08hostname\x18\x04 \x01(\t\":\n\x04Type\x12\x0b\n\x07Unknown\x10\x00\x12\x0b\n\x07\x44isplay\x10\x01\x12\n\n\x06Sensor\x10\x02\x12\x0c\n\x08Presence\x10\x03\"I\n\x07\x44isplay\x12\x1f\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\x0f.fpixels.Device\x12\r\n\x05width\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r2\xc3\x03\n\x0b\x46lamePixels\x12g\n\x0bListSensors\x12\x15.fpixels.EmptyRequest\x1a\x1c.fpixels.ListSensorsResponse\"#\x92\x41\r\x12\x0bListSensors\x82\xd3\xe4\x93\x02\r\x12\x0b/v1/sensors\x12\x80\x01\n\x10GetSensorRawData\x12\x1d.fpixels.SensorRawDataRequest\x1a\x1e.fpixels.SensorRawDataResponse\"-\x92\x41\x0f\x12\rSensorRawData\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/sensor/{id}/raw\x12k\n\x0cListDisplays\x12\x15.fpixels.EmptyRequest\x1a\x1d.fpixels.ListDisplaysResponse\"%\x92\x41\x0e\x12\x0cListDisplays\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/displays\x12[\n\x04\x44raw\x12\x14.fpixels.DrawRequest\x1a\x13.fpixels.EmptyReply\"(\x92\x41\r\x12\x0b\x44isplayInfo\x82\xd3\xe4\x93\x02\x12\x1a\r/v1/draw/{id}:\x01*B8\x92\x41\x35\x12 \n\x17\x46lame Pixels Controller2\x05\x30.1.0\x1a\x0elocalhost:8080*\x01\x01\x62\x06proto3'
  ,
  dependencies=[github_dot_com_dot_grpc__ecosystem_dot_grpc__gateway_dot_third__party_dot_googleapis_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,github_dot_com_dot_grpc__ecosystem_dot_grpc__gateway_dot_protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,])



_DEVICE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='fpixels.Device.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Display', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Sensor', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Presence', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=523,
  serialized_end=581,
)
_sym_db.RegisterEnumDescriptor(_DEVICE_TYPE)


_EMPTYREQUEST = _descriptor.Descriptor(
  name='EmptyRequest',
  full_name='fpixels.EmptyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=216,
)


_EMPTYREPLY = _descriptor.Descriptor(
  name='EmptyReply',
  full_name='fpixels.EmptyReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=230,
)


_LISTSENSORSRESPONSE = _descriptor.Descriptor(
  name='ListSensorsResponse',
  full_name='fpixels.ListSensorsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensors', full_name='fpixels.ListSensorsResponse.sensors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=287,
)


_SENSORRAWDATAREQUEST = _descriptor.Descriptor(
  name='SensorRawDataRequest',
  full_name='fpixels.SensorRawDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='fpixels.SensorRawDataRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=323,
)


_SENSORRAWDATARESPONSE = _descriptor.Descriptor(
  name='SensorRawDataResponse',
  full_name='fpixels.SensorRawDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='fpixels.SensorRawDataResponse.payload', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=365,
)


_LISTDISPLAYSRESPONSE = _descriptor.Descriptor(
  name='ListDisplaysResponse',
  full_name='fpixels.ListDisplaysResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='displays', full_name='fpixels.ListDisplaysResponse.displays', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=425,
)


_DRAWREQUEST = _descriptor.Descriptor(
  name='DrawRequest',
  full_name='fpixels.DrawRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='fpixels.DrawRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=427,
  serialized_end=452,
)


_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='fpixels.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='fpixels.Device.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='fpixels.Device.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='fpixels.Device.model', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='fpixels.Device.hostname', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DEVICE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=454,
  serialized_end=581,
)


_DISPLAY = _descriptor.Descriptor(
  name='Display',
  full_name='fpixels.Display',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='fpixels.Display.device', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='fpixels.Display.width', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='fpixels.Display.height', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=583,
  serialized_end=656,
)

_LISTSENSORSRESPONSE.fields_by_name['sensors'].message_type = _DEVICE
_LISTDISPLAYSRESPONSE.fields_by_name['displays'].message_type = _DISPLAY
_DEVICE_TYPE.containing_type = _DEVICE
_DISPLAY.fields_by_name['device'].message_type = _DEVICE
DESCRIPTOR.message_types_by_name['EmptyRequest'] = _EMPTYREQUEST
DESCRIPTOR.message_types_by_name['EmptyReply'] = _EMPTYREPLY
DESCRIPTOR.message_types_by_name['ListSensorsResponse'] = _LISTSENSORSRESPONSE
DESCRIPTOR.message_types_by_name['SensorRawDataRequest'] = _SENSORRAWDATAREQUEST
DESCRIPTOR.message_types_by_name['SensorRawDataResponse'] = _SENSORRAWDATARESPONSE
DESCRIPTOR.message_types_by_name['ListDisplaysResponse'] = _LISTDISPLAYSRESPONSE
DESCRIPTOR.message_types_by_name['DrawRequest'] = _DRAWREQUEST
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['Display'] = _DISPLAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyRequest = _reflection.GeneratedProtocolMessageType('EmptyRequest', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYREQUEST,
  '__module__' : 'fpixel_pb2'
  # @@protoc_insertion_point(class_scope:fpixels.EmptyRequest)
  })
_sym_db.RegisterMessage(EmptyRequest)

EmptyReply = _reflection.GeneratedProtocolMessageType('EmptyReply', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYREPLY,
  '__module__' : 'fpixel_pb2'
  # @@protoc_insertion_point(class_scope:fpixels.EmptyReply)
  })
_sym_db.RegisterMessage(EmptyReply)

ListSensorsResponse = _reflection.GeneratedProtocolMessageType('ListSensorsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSENSORSRESPONSE,
  '__module__' : 'fpixel_pb2'
  # @@protoc_insertion_point(class_scope:fpixels.ListSensorsResponse)
  })
_sym_db.RegisterMessage(ListSensorsResponse)

SensorRawDataRequest = _reflection.GeneratedProtocolMessageType('SensorRawDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENSORRAWDATAREQUEST,
  '__module__' : 'fpixel_pb2'
  # @@protoc_insertion_point(class_scope:fpixels.SensorRawDataRequest)
  })
_sym_db.RegisterMessage(SensorRawDataRequest)

SensorRawDataResponse = _reflection.GeneratedProtocolMessageType('SensorRawDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENSORRAWDATARESPONSE,
  '__module__' : 'fpixel_pb2'
  # @@protoc_insertion_point(class_scope:fpixels.SensorRawDataResponse)
  })
_sym_db.RegisterMessage(SensorRawDataResponse)

ListDisplaysResponse = _reflection.GeneratedProtocolMessageType('ListDisplaysResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDISPLAYSRESPONSE,
  '__module__' : 'fpixel_pb2'
  # @@protoc_insertion_point(class_scope:fpixels.ListDisplaysResponse)
  })
_sym_db.RegisterMessage(ListDisplaysResponse)

DrawRequest = _reflection.GeneratedProtocolMessageType('DrawRequest', (_message.Message,), {
  'DESCRIPTOR' : _DRAWREQUEST,
  '__module__' : 'fpixel_pb2'
  # @@protoc_insertion_point(class_scope:fpixels.DrawRequest)
  })
_sym_db.RegisterMessage(DrawRequest)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'fpixel_pb2'
  # @@protoc_insertion_point(class_scope:fpixels.Device)
  })
_sym_db.RegisterMessage(Device)

Display = _reflection.GeneratedProtocolMessageType('Display', (_message.Message,), {
  'DESCRIPTOR' : _DISPLAY,
  '__module__' : 'fpixel_pb2'
  # @@protoc_insertion_point(class_scope:fpixels.Display)
  })
_sym_db.RegisterMessage(Display)


DESCRIPTOR._options = None

_FLAMEPIXELS = _descriptor.ServiceDescriptor(
  name='FlamePixels',
  full_name='fpixels.FlamePixels',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=659,
  serialized_end=1110,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListSensors',
    full_name='fpixels.FlamePixels.ListSensors',
    index=0,
    containing_service=None,
    input_type=_EMPTYREQUEST,
    output_type=_LISTSENSORSRESPONSE,
    serialized_options=b'\222A\r\022\013ListSensors\202\323\344\223\002\r\022\013/v1/sensors',
  ),
  _descriptor.MethodDescriptor(
    name='GetSensorRawData',
    full_name='fpixels.FlamePixels.GetSensorRawData',
    index=1,
    containing_service=None,
    input_type=_SENSORRAWDATAREQUEST,
    output_type=_SENSORRAWDATARESPONSE,
    serialized_options=b'\222A\017\022\rSensorRawData\202\323\344\223\002\025\022\023/v1/sensor/{id}/raw',
  ),
  _descriptor.MethodDescriptor(
    name='ListDisplays',
    full_name='fpixels.FlamePixels.ListDisplays',
    index=2,
    containing_service=None,
    input_type=_EMPTYREQUEST,
    output_type=_LISTDISPLAYSRESPONSE,
    serialized_options=b'\222A\016\022\014ListDisplays\202\323\344\223\002\016\022\014/v1/displays',
  ),
  _descriptor.MethodDescriptor(
    name='Draw',
    full_name='fpixels.FlamePixels.Draw',
    index=3,
    containing_service=None,
    input_type=_DRAWREQUEST,
    output_type=_EMPTYREPLY,
    serialized_options=b'\222A\r\022\013DisplayInfo\202\323\344\223\002\022\032\r/v1/draw/{id}:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_FLAMEPIXELS)

DESCRIPTOR.services_by_name['FlamePixels'] = _FLAMEPIXELS

# @@protoc_insertion_point(module_scope)