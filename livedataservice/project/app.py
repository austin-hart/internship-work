# pylint:skip-file
"""Main application. This is what a client would call."""

from project.datastore.redis_data_store import RedisDataStore
import grpc
from project.grpcdocs import live_data_service_pb2
from concurrent.futures import ThreadPoolExecutor
from project.grpcdocs import live_data_service_pb2_grpc
from project.service.data_feed_manager import DataFeedManager
from project.grpcdocs.server import LiveDataServiceServicer
import logging


def main():
    """Main function for app"""
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', level=logging.INFO)
    redis = RedisDataStore(host='localhost', port=6379)
    data_feed_manager = DataFeedManager(redis)
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    live_data_service_pb2_grpc.add_LiveDataServiceServicer_to_server(
        LiveDataServiceServicer(data_feed_manager), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info('SERVER RUNNING.')
    data_feed_manager.start()
    server.wait_for_termination()


if __name__ == '__main__':
    main()
