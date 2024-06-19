from project.service.order_management_system import OrderManagementSystem
from project.service.polymarket_exchange_info import PolymarketExchangeInfo


# pylint:skip-file
"""Main application. This is what a client would call."""
import grpc
from project.grpcdocs import oms_pb2
from concurrent.futures import ThreadPoolExecutor
from project.grpcdocs import oms_pb2_grpc
import logging
from project.grpcdocs.server import OrderManagementSystemServicer


def main():
    """Main function for app"""
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', level=logging.INFO)
    # order_management_system = OrderManagementSystem()  # initaliize manager
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    oms_pb2_grpc.add_OrderManagementSystemServicer_to_server(
        OrderManagementSystemServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info('OMS SERVER RUNNING.')
    server.wait_for_termination()


if __name__ == '__main__':
    main()
