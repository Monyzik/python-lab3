from src.algorithms.bubble_sort import bubble_sort
from src.algorithms.bucket_sort import bucket_sort
from src.algorithms.counting_sort import counting_sort
from src.algorithms.heap_sort import heap_sort
from src.algorithms.quick_sort import quick_sort
from src.algorithms.radix_sort import radix_sort

SORTS = (bubble_sort, bucket_sort, counting_sort, heap_sort, quick_sort, radix_sort)

SORTS_NAMES = {"bubble": bubble_sort, "bucket": bucket_sort, "counting": counting_sort,
               "heap": heap_sort, "quick": quick_sort, "radix": radix_sort}
