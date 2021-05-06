from model import Batch, OrderLine
from datetime import date


def make_batch_and_line(sku, batch_qty, line_qty):
    return(
        Batch("batch-001", sku, qty=batch_qty, eta=date.today()),
        OrderLine("order-123", sku, line_qty)
    )


def test_allocatint_to_a_batch_reduces_available_quantity():
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine("order-ref", "SMALL-TABLE", 2)
    batch.allocate(line)
    print(batch._allocations)


def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = make_batch_and_line("Lamp", 20, 2)
    print(large_batch.can_allocate(small_line))


def test_cant_allocate_if_available_less_than_required():
    large_batch, small_line = make_batch_and_line("Lamp", 20, 25)
    print(large_batch.can_allocate(small_line))


def test_can_allocate_if_available_equal_to_required():
    large_batch, small_line = make_batch_and_line("Lamp", 20, 20)
    print(large_batch.can_allocate(small_line))
    print(large_batch.available_quantity)


def test_cant_allocate_if_sku_doesnt_match():
    batch = Batch("batch-001", "UNCOMFORTABLE-CHAIR", 100, eta=None)
    different_sku_line = OrderLine("order-123", "EXPENSIVE-TOASTER", 10)
    print(batch.can_allocate(different_sku_line))


def allocate():
    batch, orderline = make_batch_and_line("Lamp", 10, 5)
    batch.allocate(orderline)
    batch.allocate(OrderLine("ab", "Lamp", 2))
    print(batch.allocated_quantity)
    print(batch._allocations)
    print(batch.available_quantity)


allocate()
