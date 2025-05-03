#!/usr/bin/env python3
"""
Provides statistics about Nginx logs stored in MongoDB:
- Total number of logs
- Number of logs for each HTTP method
- Number of logs with method=GET and path=/status
"""

from pymongo import MongoClient


def task_12():
    """Connect to MongoDB and display log statistics."""
    client = MongoClient()
    collec = client.logs.nginx

    # Count total number of log documents
    nb_logs = collec.count_documents({})

    # Count by HTTP method
    get = collec.count_documents({"method": "GET"})
    post = collec.count_documents({"method": "POST"})
    put = collec.count_documents({"method": "PUT"})
    patch = collec.count_documents({"method": "PATCH"})
    delete = collec.count_documents({"method": "DELETE"})

    # Count GET requests to /status
    status = collec.count_documents({"method": "GET", "path": "/status"})

    # Print results
    print(f'{nb_logs} logs')
    print('Methods:')
    print(f'\tmethod GET: {get}')
    print(f'\tmethod POST: {post}')
    print(f'\tmethod PUT: {put}')
    print(f'\tmethod PATCH: {patch}')
    print(f'\tmethod DELETE: {delete}')
    print(f'{status} status check')

    client.close()


if __name__ == "__main__":
    task_12()
