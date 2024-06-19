# pylint:skip-file
"""Main application. This is what a client would call."""


import grpc
from project.grpcdocs import repository_pb2_grpc
from concurrent.futures import ThreadPoolExecutor
from project.grpcdocs import repository_pb2
import logging
#from service.respository_manager import RepositoryManager
from project.grpcdocs.server import RepositoryServicer
from project.service.postgres_respository_manager import PostgresRepositoryManager
from project.service import models


def main():
    """Main function for app"""
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', level=logging.INFO)
    repository_manager = PostgresRepositoryManager(
        user='postgres', password='password', host='localhost', port='5432', db='modeldb')  # initaliize manager
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    repository_pb2_grpc.add_RepositoryServicer_to_server(
        RepositoryServicer(repository_manager), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info('REPOSITORY SERVER RUNNING.')
    server.wait_for_termination()


if __name__ == '__main__':
    main()
