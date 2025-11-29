import click
from click_shell import shell

from src.algorithms.bucket_sort import bucket_sort
from src.algorithms.radix_sort import radix_sort
from src.constants import SORTS_NAMES
from src.algorithms.factorial import factorial_recursive, factorial
from src.algorithms.fibonacci import fibo_recursive, fibo
from src.structures.queue import Queue
from src.structures.stack import Stack

stack: Stack = Stack()
queue: Queue = Queue()


@shell(prompt="> ", intro="Алгоритмы? Нет, не слышали")
def loop():
    pass


@loop.command("queue")
@click.argument("command", nargs=1, type=str)
@click.option("--item", "-i", nargs=1, type=int)
def stack_cli(command: str, item: int) -> None:
    if command == "enqueue":
        queue.enqueue(item)
    elif command == "dequeue":
        print(queue.dequeue())
    elif command == "front":
        print(queue.front())
    elif command == "size" or command == "len":
        print(len(queue))
    elif command == "is_empty":
        print(queue.is_empty())


@loop.command("stack")
@click.argument("command", nargs=1, type=str)
@click.option("--item", "-i", nargs=1, type=int)
def stack_cli(command: str, item: int) -> None:
    if command == "push":
        stack.push(item)
    elif command == "pop":
        print(stack.pop())
    elif command == "size" or command == "len":
        print(len(stack))
    elif command == "peek":
        print(stack.peek())
    elif command == "is_empty":
        print(stack.is_empty())
    elif command == "min":
        print(stack.min())


@loop.command("sort")
@click.argument("sort_type", nargs=1, type=click.Choice(SORTS_NAMES.keys()))
@click.argument("array", nargs=-1, type=int)
@click.option("--base", nargs=1, type=int, default=10)
@click.option("--buckets", nargs=1, type=int)
def sort_cli(sort_type: str, array, base: int, buckets: int) -> None:
    if sort_type == "bucket":
        print(*bucket_sort(array, buckets))
        return
    if sort_type == "radix":
        print(*radix_sort(array, base))
        return
    print(*SORTS_NAMES[sort_type](list(array)))


@loop.command("fibonacci")
@click.argument("n", nargs=1, type=int)
@click.option("-r", is_flag=True, default=False)
def factorial_cli(n: int, r: bool) -> None:
    if r:
        print(fibo_recursive(n))
    else:
        print(fibo(n))


@loop.command("factorial")
@click.argument("n", nargs=1, type=int)
@click.option("-r", is_flag=True, default=False)
def factorial_cli(n: int, r: bool) -> None:
    if r:
        print(factorial_recursive(n))
    else:
        print(factorial(n))
