# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf_defs.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf_defs.proto',
  package='',
  serialized_pb='\n\x13protobuf_defs.proto\"s\n\x0fMatlabBridgeMsg\x12\x14\n\x03run\x18\x01 \x01(\x0b\x32\x07.RunSet\x12\x1a\n\x05props\x18\x02 \x03(\x0b\x32\x0b.Properties\x12\x17\n\x03res\x18\x03 \x01(\x0b\x32\n.ResultSet\x12\x15\n\x05model\x18\x04 \x01(\x0b\x32\x06.Model\"!\n\x05Model\x12\x18\n\x05mPath\x18\x01 \x01(\x0b\x32\t.FilePath\",\n\nProperties\x12\r\n\x03key\x18\x01 \x01(\t:\x00\x12\x0f\n\x05value\x18\x02 \x01(\t:\x00\"K\n\x06Result\x12\x1c\n\x08original\x18\x01 \x01(\x0b\x32\n.Labelable\x12#\n\x0b\x66oundLabels\x18\x02 \x01(\x0b\x32\x0e.LabelableList\"#\n\nResultList\x12\x15\n\x04rslt\x18\x01 \x03(\x0b\x32\x07.Result\")\n\tResultSet\x12\x1c\n\x07results\x18\x01 \x01(\x0b\x32\x0b.ResultList\"\'\n\rDirectoryPath\x12\x16\n\x0crelativePath\x18\x01 \x01(\t:\x00\"A\n\x08\x46ilePath\x12!\n\tdirectory\x18\x01 \x01(\x0b\x32\x0e.DirectoryPath\x12\x12\n\x08\x66ilename\x18\x02 \x01(\t:\x00\"x\n\tSubstrate\x12\x15\n\x07isImage\x18\x01 \x01(\x08:\x04true\x12\x16\n\x07isVideo\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x17\n\x04path\x18\x03 \x01(\x0b\x32\t.FilePath\x12\x10\n\x05width\x18\x04 \x01(\x05:\x01\x30\x12\x11\n\x06height\x18\x05 \x01(\x05:\x01\x30\"\x1a\n\tSemantics\x12\r\n\x03url\x18\x01 \x01(\t:\x00\"1\n\x0fLabelProperties\x12\r\n\x03key\x18\x01 \x01(\t:\x00\x12\x0f\n\x05value\x18\x02 \x01(\t:\x00\"t\n\x05Label\x12\x17\n\x08hasLabel\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x0e\n\x04name\x18\x02 \x01(\t:\x00\x12$\n\nproperties\x18\x03 \x01(\x0b\x32\x10.LabelProperties\x12\x1c\n\x08semantix\x18\x04 \x01(\x0b\x32\n.Semantics\"P\n\tLabelable\x12\x15\n\nconfidence\x18\x01 \x01(\x02:\x01\x30\x12\x13\n\x03lab\x18\x02 \x01(\x0b\x32\x06.Label\x12\x17\n\x03sub\x18\x03 \x01(\x0b\x32\n.Substrate\"\xf5\x01\n\x0cLabeledTrack\x12\x15\n\nconfidence\x18\x01 \x01(\x02:\x01\x30\x12\x13\n\x03lab\x18\x02 \x01(\x0b\x32\x06.Label\x12\x17\n\x03sub\x18\x03 \x01(\x0b\x32\n.Substrate\x12.\n\x12keyframesLocations\x18\x04 \x01(\x0b\x32\x12.FrameLocationList\x12\x35\n\x06interp\x18\x05 \x01(\x0e\x32\x1b.LabeledTrack.Interpolation:\x08\x44ISCRETE\"9\n\rInterpolation\x12\x0c\n\x08\x44ISCRETE\x10\x00\x12\n\n\x06LINEAR\x10\x01\x12\x0e\n\nPOLYNOMIAL\x10\x02\":\n\x11\x46rameLocationList\x12%\n\rframelocation\x18\x01 \x03(\x0b\x32\x0e.FrameLocation\"y\n\rFrameLocation\x12\x1d\n\x05\x66rame\x18\x01 \x01(\x0b\x32\x0e.VideoSeekTime\x12\x15\n\x03loc\x18\x02 \x01(\x0b\x32\x08.Point2D\x12\x17\n\x08occluded\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x19\n\noutOfFrame\x18\x04 \x01(\x08:\x05\x66\x61lse\"/\n\rVideoSeekTime\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x10\n\x08\x66ramecnt\x18\x02 \x01(\x03\"\x1f\n\x07Point2D\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"S\n\rLabelableList\x12\x1d\n\tlabelable\x18\x01 \x03(\x0b\x32\n.Labelable\x12#\n\x0clabeledTrack\x18\x02 \x03(\x0b\x32\r.LabeledTrack\"\xa2\x01\n\x07Purpose\x12/\n\x05ptype\x18\x01 \x01(\x0e\x32\x14.Purpose.PurposeType:\nUNPURPOSED\x12\x12\n\x07\x63lassID\x18\x02 \x01(\x05:\x01\x30\"R\n\x0bPurposeType\x12\x0e\n\nUNPURPOSED\x10\x00\x12\x0c\n\x08POSITIVE\x10\x01\x12\x0c\n\x08NEGATIVE\x10\x02\x12\x0e\n\nMULTICLASS\x10\x03\x12\x07\n\x03\x41NY\x10\x04\"W\n\x14PurposedLabelableSeq\x12\x15\n\x03pur\x18\x01 \x01(\x0b\x32\x08.Purpose\x12(\n\x10labeledArtifacts\x18\x02 \x01(\x0b\x32\x0e.LabelableList\">\n\x14PurposedListSequence\x12&\n\x07purlist\x18\x01 \x03(\x0b\x32\x15.PurposedLabelableSeq\"6\n\x06RunSet\x12,\n\rpurposedLists\x18\x01 \x01(\x0b\x32\x15.PurposedListSequence')



_LABELEDTRACK_INTERPOLATION = _descriptor.EnumDescriptor(
  name='Interpolation',
  full_name='LabeledTrack.Interpolation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DISCRETE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINEAR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POLYNOMIAL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1076,
  serialized_end=1133,
)

_PURPOSE_PURPOSETYPE = _descriptor.EnumDescriptor(
  name='PurposeType',
  full_name='Purpose.PurposeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNPURPOSED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSITIVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEGATIVE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTICLASS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANY', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1566,
  serialized_end=1648,
)


_MATLABBRIDGEMSG = _descriptor.Descriptor(
  name='MatlabBridgeMsg',
  full_name='MatlabBridgeMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='run', full_name='MatlabBridgeMsg.run', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='props', full_name='MatlabBridgeMsg.props', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res', full_name='MatlabBridgeMsg.res', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model', full_name='MatlabBridgeMsg.model', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=23,
  serialized_end=138,
)


_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mPath', full_name='Model.mPath', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=140,
  serialized_end=173,
)


_PROPERTIES = _descriptor.Descriptor(
  name='Properties',
  full_name='Properties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Properties.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Properties.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=175,
  serialized_end=219,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='original', full_name='Result.original', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='foundLabels', full_name='Result.foundLabels', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=221,
  serialized_end=296,
)


_RESULTLIST = _descriptor.Descriptor(
  name='ResultList',
  full_name='ResultList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rslt', full_name='ResultList.rslt', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=298,
  serialized_end=333,
)


_RESULTSET = _descriptor.Descriptor(
  name='ResultSet',
  full_name='ResultSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='ResultSet.results', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=335,
  serialized_end=376,
)


_DIRECTORYPATH = _descriptor.Descriptor(
  name='DirectoryPath',
  full_name='DirectoryPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relativePath', full_name='DirectoryPath.relativePath', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=378,
  serialized_end=417,
)


_FILEPATH = _descriptor.Descriptor(
  name='FilePath',
  full_name='FilePath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='directory', full_name='FilePath.directory', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='FilePath.filename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=419,
  serialized_end=484,
)


_SUBSTRATE = _descriptor.Descriptor(
  name='Substrate',
  full_name='Substrate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isImage', full_name='Substrate.isImage', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isVideo', full_name='Substrate.isVideo', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='Substrate.path', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='Substrate.width', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='Substrate.height', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=486,
  serialized_end=606,
)


_SEMANTICS = _descriptor.Descriptor(
  name='Semantics',
  full_name='Semantics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='Semantics.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=608,
  serialized_end=634,
)


_LABELPROPERTIES = _descriptor.Descriptor(
  name='LabelProperties',
  full_name='LabelProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='LabelProperties.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='LabelProperties.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=636,
  serialized_end=685,
)


_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hasLabel', full_name='Label.hasLabel', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Label.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='properties', full_name='Label.properties', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='semantix', full_name='Label.semantix', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=687,
  serialized_end=803,
)


_LABELABLE = _descriptor.Descriptor(
  name='Labelable',
  full_name='Labelable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='confidence', full_name='Labelable.confidence', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lab', full_name='Labelable.lab', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub', full_name='Labelable.sub', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=805,
  serialized_end=885,
)


_LABELEDTRACK = _descriptor.Descriptor(
  name='LabeledTrack',
  full_name='LabeledTrack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='confidence', full_name='LabeledTrack.confidence', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lab', full_name='LabeledTrack.lab', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub', full_name='LabeledTrack.sub', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyframesLocations', full_name='LabeledTrack.keyframesLocations', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interp', full_name='LabeledTrack.interp', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LABELEDTRACK_INTERPOLATION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=888,
  serialized_end=1133,
)


_FRAMELOCATIONLIST = _descriptor.Descriptor(
  name='FrameLocationList',
  full_name='FrameLocationList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='framelocation', full_name='FrameLocationList.framelocation', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1135,
  serialized_end=1193,
)


_FRAMELOCATION = _descriptor.Descriptor(
  name='FrameLocation',
  full_name='FrameLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame', full_name='FrameLocation.frame', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loc', full_name='FrameLocation.loc', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='occluded', full_name='FrameLocation.occluded', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outOfFrame', full_name='FrameLocation.outOfFrame', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1195,
  serialized_end=1316,
)


_VIDEOSEEKTIME = _descriptor.Descriptor(
  name='VideoSeekTime',
  full_name='VideoSeekTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='VideoSeekTime.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='framecnt', full_name='VideoSeekTime.framecnt', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1318,
  serialized_end=1365,
)


_POINT2D = _descriptor.Descriptor(
  name='Point2D',
  full_name='Point2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Point2D.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='Point2D.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1367,
  serialized_end=1398,
)


_LABELABLELIST = _descriptor.Descriptor(
  name='LabelableList',
  full_name='LabelableList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='labelable', full_name='LabelableList.labelable', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labeledTrack', full_name='LabelableList.labeledTrack', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1400,
  serialized_end=1483,
)


_PURPOSE = _descriptor.Descriptor(
  name='Purpose',
  full_name='Purpose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ptype', full_name='Purpose.ptype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classID', full_name='Purpose.classID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PURPOSE_PURPOSETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1486,
  serialized_end=1648,
)


_PURPOSEDLABELABLESEQ = _descriptor.Descriptor(
  name='PurposedLabelableSeq',
  full_name='PurposedLabelableSeq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pur', full_name='PurposedLabelableSeq.pur', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labeledArtifacts', full_name='PurposedLabelableSeq.labeledArtifacts', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1650,
  serialized_end=1737,
)


_PURPOSEDLISTSEQUENCE = _descriptor.Descriptor(
  name='PurposedListSequence',
  full_name='PurposedListSequence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='purlist', full_name='PurposedListSequence.purlist', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1739,
  serialized_end=1801,
)


_RUNSET = _descriptor.Descriptor(
  name='RunSet',
  full_name='RunSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='purposedLists', full_name='RunSet.purposedLists', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1803,
  serialized_end=1857,
)

_MATLABBRIDGEMSG.fields_by_name['run'].message_type = _RUNSET
_MATLABBRIDGEMSG.fields_by_name['props'].message_type = _PROPERTIES
_MATLABBRIDGEMSG.fields_by_name['res'].message_type = _RESULTSET
_MATLABBRIDGEMSG.fields_by_name['model'].message_type = _MODEL
_MODEL.fields_by_name['mPath'].message_type = _FILEPATH
_RESULT.fields_by_name['original'].message_type = _LABELABLE
_RESULT.fields_by_name['foundLabels'].message_type = _LABELABLELIST
_RESULTLIST.fields_by_name['rslt'].message_type = _RESULT
_RESULTSET.fields_by_name['results'].message_type = _RESULTLIST
_FILEPATH.fields_by_name['directory'].message_type = _DIRECTORYPATH
_SUBSTRATE.fields_by_name['path'].message_type = _FILEPATH
_LABEL.fields_by_name['properties'].message_type = _LABELPROPERTIES
_LABEL.fields_by_name['semantix'].message_type = _SEMANTICS
_LABELABLE.fields_by_name['lab'].message_type = _LABEL
_LABELABLE.fields_by_name['sub'].message_type = _SUBSTRATE
_LABELEDTRACK.fields_by_name['lab'].message_type = _LABEL
_LABELEDTRACK.fields_by_name['sub'].message_type = _SUBSTRATE
_LABELEDTRACK.fields_by_name['keyframesLocations'].message_type = _FRAMELOCATIONLIST
_LABELEDTRACK.fields_by_name['interp'].enum_type = _LABELEDTRACK_INTERPOLATION
_LABELEDTRACK_INTERPOLATION.containing_type = _LABELEDTRACK;
_FRAMELOCATIONLIST.fields_by_name['framelocation'].message_type = _FRAMELOCATION
_FRAMELOCATION.fields_by_name['frame'].message_type = _VIDEOSEEKTIME
_FRAMELOCATION.fields_by_name['loc'].message_type = _POINT2D
_LABELABLELIST.fields_by_name['labelable'].message_type = _LABELABLE
_LABELABLELIST.fields_by_name['labeledTrack'].message_type = _LABELEDTRACK
_PURPOSE.fields_by_name['ptype'].enum_type = _PURPOSE_PURPOSETYPE
_PURPOSE_PURPOSETYPE.containing_type = _PURPOSE;
_PURPOSEDLABELABLESEQ.fields_by_name['pur'].message_type = _PURPOSE
_PURPOSEDLABELABLESEQ.fields_by_name['labeledArtifacts'].message_type = _LABELABLELIST
_PURPOSEDLISTSEQUENCE.fields_by_name['purlist'].message_type = _PURPOSEDLABELABLESEQ
_RUNSET.fields_by_name['purposedLists'].message_type = _PURPOSEDLISTSEQUENCE
DESCRIPTOR.message_types_by_name['MatlabBridgeMsg'] = _MATLABBRIDGEMSG
DESCRIPTOR.message_types_by_name['Model'] = _MODEL
DESCRIPTOR.message_types_by_name['Properties'] = _PROPERTIES
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['ResultList'] = _RESULTLIST
DESCRIPTOR.message_types_by_name['ResultSet'] = _RESULTSET
DESCRIPTOR.message_types_by_name['DirectoryPath'] = _DIRECTORYPATH
DESCRIPTOR.message_types_by_name['FilePath'] = _FILEPATH
DESCRIPTOR.message_types_by_name['Substrate'] = _SUBSTRATE
DESCRIPTOR.message_types_by_name['Semantics'] = _SEMANTICS
DESCRIPTOR.message_types_by_name['LabelProperties'] = _LABELPROPERTIES
DESCRIPTOR.message_types_by_name['Label'] = _LABEL
DESCRIPTOR.message_types_by_name['Labelable'] = _LABELABLE
DESCRIPTOR.message_types_by_name['LabeledTrack'] = _LABELEDTRACK
DESCRIPTOR.message_types_by_name['FrameLocationList'] = _FRAMELOCATIONLIST
DESCRIPTOR.message_types_by_name['FrameLocation'] = _FRAMELOCATION
DESCRIPTOR.message_types_by_name['VideoSeekTime'] = _VIDEOSEEKTIME
DESCRIPTOR.message_types_by_name['Point2D'] = _POINT2D
DESCRIPTOR.message_types_by_name['LabelableList'] = _LABELABLELIST
DESCRIPTOR.message_types_by_name['Purpose'] = _PURPOSE
DESCRIPTOR.message_types_by_name['PurposedLabelableSeq'] = _PURPOSEDLABELABLESEQ
DESCRIPTOR.message_types_by_name['PurposedListSequence'] = _PURPOSEDLISTSEQUENCE
DESCRIPTOR.message_types_by_name['RunSet'] = _RUNSET

class MatlabBridgeMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MATLABBRIDGEMSG

  # @@protoc_insertion_point(class_scope:MatlabBridgeMsg)

class Model(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODEL

  # @@protoc_insertion_point(class_scope:Model)

class Properties(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROPERTIES

  # @@protoc_insertion_point(class_scope:Properties)

class Result(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESULT

  # @@protoc_insertion_point(class_scope:Result)

class ResultList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESULTLIST

  # @@protoc_insertion_point(class_scope:ResultList)

class ResultSet(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESULTSET

  # @@protoc_insertion_point(class_scope:ResultSet)

class DirectoryPath(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DIRECTORYPATH

  # @@protoc_insertion_point(class_scope:DirectoryPath)

class FilePath(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FILEPATH

  # @@protoc_insertion_point(class_scope:FilePath)

class Substrate(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUBSTRATE

  # @@protoc_insertion_point(class_scope:Substrate)

class Semantics(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SEMANTICS

  # @@protoc_insertion_point(class_scope:Semantics)

class LabelProperties(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LABELPROPERTIES

  # @@protoc_insertion_point(class_scope:LabelProperties)

class Label(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LABEL

  # @@protoc_insertion_point(class_scope:Label)

class Labelable(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LABELABLE

  # @@protoc_insertion_point(class_scope:Labelable)

class LabeledTrack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LABELEDTRACK

  # @@protoc_insertion_point(class_scope:LabeledTrack)

class FrameLocationList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRAMELOCATIONLIST

  # @@protoc_insertion_point(class_scope:FrameLocationList)

class FrameLocation(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRAMELOCATION

  # @@protoc_insertion_point(class_scope:FrameLocation)

class VideoSeekTime(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VIDEOSEEKTIME

  # @@protoc_insertion_point(class_scope:VideoSeekTime)

class Point2D(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POINT2D

  # @@protoc_insertion_point(class_scope:Point2D)

class LabelableList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LABELABLELIST

  # @@protoc_insertion_point(class_scope:LabelableList)

class Purpose(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURPOSE

  # @@protoc_insertion_point(class_scope:Purpose)

class PurposedLabelableSeq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURPOSEDLABELABLESEQ

  # @@protoc_insertion_point(class_scope:PurposedLabelableSeq)

class PurposedListSequence(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PURPOSEDLISTSEQUENCE

  # @@protoc_insertion_point(class_scope:PurposedListSequence)

class RunSet(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RUNSET

  # @@protoc_insertion_point(class_scope:RunSet)


# @@protoc_insertion_point(module_scope)
