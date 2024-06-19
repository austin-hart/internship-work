# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: oms.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\toms.proto\"\x17\n\x15SupportedExchangesGet\"+\n\x16SupportedExchangesPost\x12\x11\n\tjson_data\x18\x01 \x01(\t\"\'\n\x13SupportedMarketsGet\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\")\n\x14SupportedMarketsPost\x12\x11\n\tjson_data\x18\x01 \x01(\t\"j\n\rPlaceOrderGet\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\x12\x0e\n\x06market\x18\x02 \x01(\t\x12\x0c\n\x04side\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x02\x12\x0c\n\x04size\x18\x05 \x01(\x02\x12\x0c\n\x04kind\x18\x06 \x01(\t\"#\n\x0ePlaceOrderPost\x12\x11\n\tjson_data\x18\x01 \x01(\t\"\"\n\x0e\x43\x61ncelOrderGet\x12\x10\n\x08order_id\x18\x01 \x01(\t\"$\n\x0f\x43\x61ncelOrderPost\x12\x11\n\tjson_data\x18\x01 \x01(\t\"\"\n\x0eOrderStatusGet\x12\x10\n\x08order_id\x18\x01 \x01(\t\"$\n\x0fOrderStatusPost\x12\x11\n\tjson_data\x18\x01 \x01(\t2\xc5\x02\n\x15OrderManagementSystem\x12J\n\x15GetSupportedExchanges\x12\x16.SupportedExchangesGet\x1a\x17.SupportedExchangesPost\"\x00\x12\x44\n\x13GetSupportedMarkets\x12\x14.SupportedMarketsGet\x1a\x15.SupportedMarketsPost\"\x00\x12/\n\nPlaceOrder\x12\x0e.PlaceOrderGet\x1a\x0f.PlaceOrderPost\"\x00\x12\x32\n\x0b\x43\x61ncelOrder\x12\x0f.CancelOrderGet\x1a\x10.CancelOrderPost\"\x00\x12\x35\n\x0eGetOrderStatus\x12\x0f.OrderStatusGet\x1a\x10.OrderStatusPost\"\x00\x62\x06proto3')



_SUPPORTEDEXCHANGESGET = DESCRIPTOR.message_types_by_name['SupportedExchangesGet']
_SUPPORTEDEXCHANGESPOST = DESCRIPTOR.message_types_by_name['SupportedExchangesPost']
_SUPPORTEDMARKETSGET = DESCRIPTOR.message_types_by_name['SupportedMarketsGet']
_SUPPORTEDMARKETSPOST = DESCRIPTOR.message_types_by_name['SupportedMarketsPost']
_PLACEORDERGET = DESCRIPTOR.message_types_by_name['PlaceOrderGet']
_PLACEORDERPOST = DESCRIPTOR.message_types_by_name['PlaceOrderPost']
_CANCELORDERGET = DESCRIPTOR.message_types_by_name['CancelOrderGet']
_CANCELORDERPOST = DESCRIPTOR.message_types_by_name['CancelOrderPost']
_ORDERSTATUSGET = DESCRIPTOR.message_types_by_name['OrderStatusGet']
_ORDERSTATUSPOST = DESCRIPTOR.message_types_by_name['OrderStatusPost']
SupportedExchangesGet = _reflection.GeneratedProtocolMessageType('SupportedExchangesGet', (_message.Message,), {
  'DESCRIPTOR' : _SUPPORTEDEXCHANGESGET,
  '__module__' : 'oms_pb2'
  # @@protoc_insertion_point(class_scope:SupportedExchangesGet)
  })
_sym_db.RegisterMessage(SupportedExchangesGet)

SupportedExchangesPost = _reflection.GeneratedProtocolMessageType('SupportedExchangesPost', (_message.Message,), {
  'DESCRIPTOR' : _SUPPORTEDEXCHANGESPOST,
  '__module__' : 'oms_pb2'
  # @@protoc_insertion_point(class_scope:SupportedExchangesPost)
  })
_sym_db.RegisterMessage(SupportedExchangesPost)

SupportedMarketsGet = _reflection.GeneratedProtocolMessageType('SupportedMarketsGet', (_message.Message,), {
  'DESCRIPTOR' : _SUPPORTEDMARKETSGET,
  '__module__' : 'oms_pb2'
  # @@protoc_insertion_point(class_scope:SupportedMarketsGet)
  })
_sym_db.RegisterMessage(SupportedMarketsGet)

SupportedMarketsPost = _reflection.GeneratedProtocolMessageType('SupportedMarketsPost', (_message.Message,), {
  'DESCRIPTOR' : _SUPPORTEDMARKETSPOST,
  '__module__' : 'oms_pb2'
  # @@protoc_insertion_point(class_scope:SupportedMarketsPost)
  })
_sym_db.RegisterMessage(SupportedMarketsPost)

PlaceOrderGet = _reflection.GeneratedProtocolMessageType('PlaceOrderGet', (_message.Message,), {
  'DESCRIPTOR' : _PLACEORDERGET,
  '__module__' : 'oms_pb2'
  # @@protoc_insertion_point(class_scope:PlaceOrderGet)
  })
_sym_db.RegisterMessage(PlaceOrderGet)

PlaceOrderPost = _reflection.GeneratedProtocolMessageType('PlaceOrderPost', (_message.Message,), {
  'DESCRIPTOR' : _PLACEORDERPOST,
  '__module__' : 'oms_pb2'
  # @@protoc_insertion_point(class_scope:PlaceOrderPost)
  })
_sym_db.RegisterMessage(PlaceOrderPost)

CancelOrderGet = _reflection.GeneratedProtocolMessageType('CancelOrderGet', (_message.Message,), {
  'DESCRIPTOR' : _CANCELORDERGET,
  '__module__' : 'oms_pb2'
  # @@protoc_insertion_point(class_scope:CancelOrderGet)
  })
_sym_db.RegisterMessage(CancelOrderGet)

CancelOrderPost = _reflection.GeneratedProtocolMessageType('CancelOrderPost', (_message.Message,), {
  'DESCRIPTOR' : _CANCELORDERPOST,
  '__module__' : 'oms_pb2'
  # @@protoc_insertion_point(class_scope:CancelOrderPost)
  })
_sym_db.RegisterMessage(CancelOrderPost)

OrderStatusGet = _reflection.GeneratedProtocolMessageType('OrderStatusGet', (_message.Message,), {
  'DESCRIPTOR' : _ORDERSTATUSGET,
  '__module__' : 'oms_pb2'
  # @@protoc_insertion_point(class_scope:OrderStatusGet)
  })
_sym_db.RegisterMessage(OrderStatusGet)

OrderStatusPost = _reflection.GeneratedProtocolMessageType('OrderStatusPost', (_message.Message,), {
  'DESCRIPTOR' : _ORDERSTATUSPOST,
  '__module__' : 'oms_pb2'
  # @@protoc_insertion_point(class_scope:OrderStatusPost)
  })
_sym_db.RegisterMessage(OrderStatusPost)

_ORDERMANAGEMENTSYSTEM = DESCRIPTOR.services_by_name['OrderManagementSystem']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SUPPORTEDEXCHANGESGET._serialized_start=13
  _SUPPORTEDEXCHANGESGET._serialized_end=36
  _SUPPORTEDEXCHANGESPOST._serialized_start=38
  _SUPPORTEDEXCHANGESPOST._serialized_end=81
  _SUPPORTEDMARKETSGET._serialized_start=83
  _SUPPORTEDMARKETSGET._serialized_end=122
  _SUPPORTEDMARKETSPOST._serialized_start=124
  _SUPPORTEDMARKETSPOST._serialized_end=165
  _PLACEORDERGET._serialized_start=167
  _PLACEORDERGET._serialized_end=273
  _PLACEORDERPOST._serialized_start=275
  _PLACEORDERPOST._serialized_end=310
  _CANCELORDERGET._serialized_start=312
  _CANCELORDERGET._serialized_end=346
  _CANCELORDERPOST._serialized_start=348
  _CANCELORDERPOST._serialized_end=384
  _ORDERSTATUSGET._serialized_start=386
  _ORDERSTATUSGET._serialized_end=420
  _ORDERSTATUSPOST._serialized_start=422
  _ORDERSTATUSPOST._serialized_end=458
  _ORDERMANAGEMENTSYSTEM._serialized_start=461
  _ORDERMANAGEMENTSYSTEM._serialized_end=786
# @@protoc_insertion_point(module_scope)