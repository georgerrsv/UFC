# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: filme.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='filme.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x66ilme.proto\"\x8c\x01\n\x05\x46ilme\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06titulo\x18\x02 \x01(\t\x12\x0f\n\x07\x64iretor\x18\x03 \x01(\t\x12\x0b\n\x03\x61no\x18\x04 \x01(\x05\x12\x0f\n\x07\x64uracao\x18\x05 \x01(\x05\x12\x0e\n\x06genero\x18\x06 \x01(\t\x12\x15\n\rclassificacao\x18\x07 \x01(\x05\x12\x11\n\tdescricao\x18\x08 \x01(\t\"\x95\x01\n\x0e\x41\x64\x64\x46ilmRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06titulo\x18\x02 \x01(\t\x12\x0f\n\x07\x64iretor\x18\x03 \x01(\t\x12\x0b\n\x03\x61no\x18\x04 \x01(\x05\x12\x0f\n\x07\x64uracao\x18\x05 \x01(\x05\x12\x0e\n\x06genero\x18\x06 \x01(\t\x12\x15\n\rclassificacao\x18\x07 \x01(\x05\x12\x11\n\tdescricao\x18\x08 \x01(\t\"\x1f\n\x11RemoveFilmRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x1d\n\x0fListFilmRequest\x12\n\n\x02id\x18\x01 \x01(\t\" \n\x12ListCatalogRequest\x12\n\n\x02id\x18\x01 \x01(\t\"R\n\x08Response\x12\x15\n\rerror_message\x18\x01 \x01(\t\x12\x15\n\x05\x66ilme\x18\x02 \x01(\x0b\x32\x06.Filme\x12\x18\n\x08\x63\x61talogo\x18\x03 \x03(\x0b\x32\x06.Filme\"\xd5\x01\n\x07Request\x12\x0e\n\x06method\x18\x01 \x01(\t\x12)\n\x10\x61\x64\x64_film_request\x18\x02 \x01(\x0b\x32\x0f.AddFilmRequest\x12/\n\x13remove_film_request\x18\x03 \x01(\x0b\x32\x12.RemoveFilmRequest\x12+\n\x11list_film_request\x18\x04 \x01(\x0b\x32\x10.ListFilmRequest\x12\x31\n\x14list_catalog_request\x18\x05 \x01(\x0b\x32\x13.ListCatalogRequestb\x06proto3'
)




_FILME = _descriptor.Descriptor(
  name='Filme',
  full_name='Filme',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Filme.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='titulo', full_name='Filme.titulo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='diretor', full_name='Filme.diretor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ano', full_name='Filme.ano', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duracao', full_name='Filme.duracao', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genero', full_name='Filme.genero', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classificacao', full_name='Filme.classificacao', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='descricao', full_name='Filme.descricao', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=16,
  serialized_end=156,
)


_ADDFILMREQUEST = _descriptor.Descriptor(
  name='AddFilmRequest',
  full_name='AddFilmRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='AddFilmRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='titulo', full_name='AddFilmRequest.titulo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='diretor', full_name='AddFilmRequest.diretor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ano', full_name='AddFilmRequest.ano', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duracao', full_name='AddFilmRequest.duracao', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genero', full_name='AddFilmRequest.genero', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classificacao', full_name='AddFilmRequest.classificacao', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='descricao', full_name='AddFilmRequest.descricao', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=159,
  serialized_end=308,
)


_REMOVEFILMREQUEST = _descriptor.Descriptor(
  name='RemoveFilmRequest',
  full_name='RemoveFilmRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='RemoveFilmRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=310,
  serialized_end=341,
)


_LISTFILMREQUEST = _descriptor.Descriptor(
  name='ListFilmRequest',
  full_name='ListFilmRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ListFilmRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=343,
  serialized_end=372,
)


_LISTCATALOGREQUEST = _descriptor.Descriptor(
  name='ListCatalogRequest',
  full_name='ListCatalogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ListCatalogRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=374,
  serialized_end=406,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_message', full_name='Response.error_message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filme', full_name='Response.filme', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='catalogo', full_name='Response.catalogo', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=408,
  serialized_end=490,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='Request.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='add_film_request', full_name='Request.add_film_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remove_film_request', full_name='Request.remove_film_request', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='list_film_request', full_name='Request.list_film_request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='list_catalog_request', full_name='Request.list_catalog_request', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=493,
  serialized_end=706,
)

_RESPONSE.fields_by_name['filme'].message_type = _FILME
_RESPONSE.fields_by_name['catalogo'].message_type = _FILME
_REQUEST.fields_by_name['add_film_request'].message_type = _ADDFILMREQUEST
_REQUEST.fields_by_name['remove_film_request'].message_type = _REMOVEFILMREQUEST
_REQUEST.fields_by_name['list_film_request'].message_type = _LISTFILMREQUEST
_REQUEST.fields_by_name['list_catalog_request'].message_type = _LISTCATALOGREQUEST
DESCRIPTOR.message_types_by_name['Filme'] = _FILME
DESCRIPTOR.message_types_by_name['AddFilmRequest'] = _ADDFILMREQUEST
DESCRIPTOR.message_types_by_name['RemoveFilmRequest'] = _REMOVEFILMREQUEST
DESCRIPTOR.message_types_by_name['ListFilmRequest'] = _LISTFILMREQUEST
DESCRIPTOR.message_types_by_name['ListCatalogRequest'] = _LISTCATALOGREQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Filme = _reflection.GeneratedProtocolMessageType('Filme', (_message.Message,), {
  'DESCRIPTOR' : _FILME,
  '__module__' : 'filme_pb2'
  # @@protoc_insertion_point(class_scope:Filme)
  })
_sym_db.RegisterMessage(Filme)

AddFilmRequest = _reflection.GeneratedProtocolMessageType('AddFilmRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDFILMREQUEST,
  '__module__' : 'filme_pb2'
  # @@protoc_insertion_point(class_scope:AddFilmRequest)
  })
_sym_db.RegisterMessage(AddFilmRequest)

RemoveFilmRequest = _reflection.GeneratedProtocolMessageType('RemoveFilmRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEFILMREQUEST,
  '__module__' : 'filme_pb2'
  # @@protoc_insertion_point(class_scope:RemoveFilmRequest)
  })
_sym_db.RegisterMessage(RemoveFilmRequest)

ListFilmRequest = _reflection.GeneratedProtocolMessageType('ListFilmRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFILMREQUEST,
  '__module__' : 'filme_pb2'
  # @@protoc_insertion_point(class_scope:ListFilmRequest)
  })
_sym_db.RegisterMessage(ListFilmRequest)

ListCatalogRequest = _reflection.GeneratedProtocolMessageType('ListCatalogRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCATALOGREQUEST,
  '__module__' : 'filme_pb2'
  # @@protoc_insertion_point(class_scope:ListCatalogRequest)
  })
_sym_db.RegisterMessage(ListCatalogRequest)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'filme_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'filme_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)


# @@protoc_insertion_point(module_scope)
