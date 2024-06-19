def order_listener(self) -> None:
     self.ws.send(self.subscription)
      while True:
           try:
                msg = self.ws.recv()
                # result_dict = {"orderID": "", "owner": "", "timestamp": "", "price": "",
                #              "size": "", "available_size": "", "side": "", "status": "", "tokenID": ""}
                # msg_dict = json.loads(msg)
                # result_dict["owner"], result_dict['timestamp'], result_dict['price'], result_dict['size'], result_dict['available_size'], result_dict['side'], result_dict[
                #   'status'], result_dict['tokenID'] = msg_dict["owner"], msg_dict['timestamp'], msg_dict['price'], msg_dict['size'], msg_dict['size'], msg_dict['side'], 'STATUS_LIVE', msg_dict['market']
                # order_id = msg_dict["id"]
                print(msg)
                # if msg_dict['type'] == 'insert':
                # self.recorded_orders[order_id] = result_dict
                # if msg_dict['type'] == 'partial_fill':
                # self.recorded_orders[order_id]['available_size']

            except:
                self.ws.close()
                self.socket_connected = False
                self.ws = websocket.WebSocket()
                print("connection lost... reconnecting")
                while not self.socket_connected:
                    try:
                        self.ws.connect(
                            "wss://ws-subscriptions-clob-staging.polymarket.com/ws/orders")
                        self.ws.send(self.subscription)
                        self.sync_orders_thread.submit(self.sync_orders)
                        self.socket_connected = True
                        print("re-connection successful")
                    except:
                        time.sleep(1)
