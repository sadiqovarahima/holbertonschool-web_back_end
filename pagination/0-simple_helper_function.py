#!/usr/bin/env python3
"""
Səhifələmə (Pagination) üçün köməkçi funksiya.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Səhifə nömrəsi və ölçüsünə əsasən başlanğıc və 
    son indeksləri qaytaran funksiya.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    
    return (start_index, end_index)
