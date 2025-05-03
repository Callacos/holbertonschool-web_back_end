#!/usr/bin/env python3
"""
documentation for index_range function
"""
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    documentation for index_range function
    """
    start_index = (page - 1) * page_size
    end_index = page_size * page
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Dataset indexed by sorting position, starting at 0
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Dataset indexed by sorting position, starting at 0
        """
        assert isinstance(
            page,
            int) and page > 0, "page must be a positive integer"
        assert isinstance(
            page_size,
            int) and page_size > 0, "page_size must be a positive integer"

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ documentation for get_hyper function
        """
        data = self.get_page(page, page_size)
        dataset_size = len(self.dataset())
        total_pages = math.ceil(dataset_size / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
            }
