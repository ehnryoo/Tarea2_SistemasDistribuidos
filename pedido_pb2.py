# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pedido.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cpedido.proto\x12\x07pedidos\"\xaa\x01\n\x06\x43ompra\x12\x0f\n\x07\x63liente\x18\x01 \x01(\t\x12\x10\n\x08producto\x18\x02 \x01(\t\x12\x0e\n\x06precio\x18\x03 \x01(\x02\x12\x15\n\rpasarela_pago\x18\x04 \x01(\t\x12\x15\n\rmarca_tarjeta\x18\x05 \x01(\t\x12\r\n\x05\x62\x61nco\x18\x06 \x01(\t\x12\x0e\n\x06\x63omuna\x18\x07 \x01(\t\x12\x11\n\tdireccion\x18\x08 \x01(\t\x12\r\n\x05\x65mail\x18\t \x01(\t\"+\n\tRespuesta\x12\x0f\n\x07mensaje\x18\x01 \x01(\t\x12\r\n\x05\x65xito\x18\x02 \x01(\x08\x32I\n\x0eGestionPedidos\x12\x37\n\x0eRealizarCompra\x12\x0f.pedidos.Compra\x1a\x12.pedidos.Respuesta\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pedido_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_COMPRA']._serialized_start=26
  _globals['_COMPRA']._serialized_end=196
  _globals['_RESPUESTA']._serialized_start=198
  _globals['_RESPUESTA']._serialized_end=241
  _globals['_GESTIONPEDIDOS']._serialized_start=243
  _globals['_GESTIONPEDIDOS']._serialized_end=316
# @@protoc_insertion_point(module_scope)
