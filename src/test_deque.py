"""Test deque.py."""

import pytest


@pytest.fixture
def empty_deque():
    """Create empty deque."""
    from deque import Deque
    unpopulated_deque = Deque()
    return unpopulated_deque


@pytest.fixture
def full_deque():
    """Create deque initialized with iterable."""
    from deque import Deque
    populated_deque = Deque(iterable=[1, 2, 3])
    return populated_deque


def test_full_deque_is_full(full_deque):
    """Test that populating deque with iterable produces head with value of 3."""
    assert full_deque._deque.head.value == 3


def test_full_deque_has_tail(full_deque):
    """Test that populating deque with iterable has correct tail element."""
    assert full_deque._deque.tail.value == 1


def test_full_deque_has_length(full_deque):
    """Test that full deque has length of 3."""
    assert full_deque._deque._length == 3


def test_empty_deque_is_empty(empty_deque):
    """Test that empty deque is empty."""
    assert empty_deque.size() == 0


def test_initializing_deque_with_non_iterable_raises_error():
    """Test that error is raised when you try to initialize with noniterable."""
    from deque import Deque
    with pytest.raises(TypeError):
        new_deque = Deque(interable=123456)


def test_append_to_empty_deque_check_head(empty_deque):
    """Test append method on empty deque first value is Denny Way."""
    empty_deque.append("Denny Way")
    assert empty_deque._deque.head.value == "Denny Way"


def test_append_to_empty_deque_check_tail(empty_deque):
    """Test append method on empty deque tail is Denny Way."""
    empty_deque.append("Denny Way")
    assert empty_deque._deque.tail.value == "Denny Way"


def test_append_to_empty_deque_size(empty_deque):
    """Test append method on empty deque size is 1."""
    empty_deque.append("Denny Way")
    assert empty_deque.size() == 1


def test_append_to_full_deque_check_head(full_deque):
    """Test append method on full deque head is 3."""
    full_deque.append("Denny Way")
    assert full_deque._deque.head.value == 3


def test_append_to_full_deque_check_tail(full_deque):
    """Test append method on full deque tail is 3."""
    full_deque.append("Denny Way")
    assert full_deque._deque.tail.value == "Denny Way"


def test_append_to_full_deque_size(full_deque):
    """Test append method on full deque size is 4."""
    full_deque.append("Denny Way")
    assert full_deque.size() == 4


def test_appendleft_to_empty_deque_check_head(empty_deque):
    """Test appendleft method on empty deque head is Denny Way."""
    empty_deque.appendleft("Denny Way")
    assert empty_deque._deque.head.value == "Denny Way"


def test_appendleft_to_empty_deque_check_tail(empty_deque):
    """Test appendleft method on empty deque tail is Denny Way."""
    empty_deque.appendleft("Denny Way")
    assert empty_deque._deque.tail.value == "Denny Way"


def test_appendleft_to_empty_deque_size(empty_deque):
    """Test appendleft method on empty deque size is 1."""
    empty_deque.appendleft("Denny Way")
    assert empty_deque.size() == 1


def test_appendleft_to_full_deque_check_head(full_deque):
    """Test appendleft method on full deque head is Denny Way."""
    full_deque.appendleft("Denny Way")
    assert full_deque._deque.head.value == "Denny Way"


def test_appendleft_to_full_deque_check_tail(full_deque):
    """Test appendleft method on full deque tail is 1."""
    full_deque.appendleft("Denny Way")
    assert full_deque._deque.tail.value == 1


def test_appendleft_to_full_deque_size(full_deque):
    """Test appendleft method on full deque size is 4."""
    full_deque.appendleft("Denny Way")
    assert full_deque.size() == 4


def test_pop_to_full_deque_tail(full_deque):
    """Test pop method on full deque tail is 2."""
    full_deque.pop()
    assert full_deque._deque.tail.value == 2


def test_pop_to_full_deque_returns_correct_value(full_deque):
    """Test pop method on full deque returns 1."""
    assert full_deque.pop() == 1


def test_pop_to_full_deque_size_decrease(full_deque):
    """Test pop method on full deque size is ."""
    full_deque.pop()
    assert full_deque._deque._length == 2


def test_pop_empty_deque_raises_error(empty_deque):
    """Test pop mehtod on empty deque raises error."""
    with pytest.raises(IndexError):
        empty_deque.pop()


def test_popleft_to_full_deque_tail(full_deque):
    """Test pop method on full deque tail is 2."""
    full_deque.popleft()
    assert full_deque._deque.tail.value == 1


def test_popleft_to_full_deque_returns_correct_value(full_deque):
    """Test pop method on full deque returns 1."""
    assert full_deque.popleft() == 3


def test_popleft_to_full_deque_size_decrease(full_deque):
    """Test pop method on full deque size is ."""
    full_deque.popleft()
    assert full_deque._deque._length == 2


def test_popleft_empty_deque_raises_error(empty_deque):
    """Test pop mehtod on empty deque raises error."""
    with pytest.raises(IndexError):
        empty_deque.popleft()


def test_cant_peek_empty(empty_deque):
    """Test peek can't be called on empty deques."""
    assert empty_deque.peek() is None


def test_peek_returns_value(full_deque):
    """Test peeking at the proper (tail) value."""
    assert full_deque.peek() == 1


def test_cant_peekleft_empty(empty_deque):
    """Test peekleft can't be called on empty deques."""
    assert empty_deque.peekleft() is None


def test_peekleft_returns_value(full_deque):
    """Test peeklefting at the proper (head) value."""
    assert full_deque.peekleft() == 3


def test_pop_with_append(empty_deque):
    """Test pop will return correct value."""
    empty_deque.append(1)
    empty_deque.append(2)
    empty_deque.pop()
    empty_deque.append(3)
    empty_deque.append(4)
    empty_deque.append(5)
    assert empty_deque.pop() == 5


def test_pop_with_appendleft(empty_deque):
    """Test pop will return correct value."""
    empty_deque.appendleft(1)
    empty_deque.appendleft(2)
    empty_deque.pop()
    empty_deque.appendleft(3)
    empty_deque.appendleft(4)
    empty_deque.appendleft(5)
    assert empty_deque.pop() == 2


def test_popleft_with_append(empty_deque):
    """Test popleft will return correct value."""
    empty_deque.append(1)
    empty_deque.append(2)
    empty_deque.popleft()
    empty_deque.append(3)
    empty_deque.append(4)
    empty_deque.append(5)
    assert empty_deque.popleft() == 2


def test_popleft_with_appendleft(empty_deque):
    """Test popleft will return correct value."""
    empty_deque.appendleft(1)
    empty_deque.appendleft(2)
    empty_deque.popleft()
    empty_deque.appendleft(3)
    empty_deque.appendleft(4)
    empty_deque.appendleft(5)
    assert empty_deque.popleft() == 5


def test_popleft_with_append_and_pop(empty_deque):
    """Test popleft will return correct value."""
    empty_deque.append(1)
    empty_deque.append(2)
    empty_deque.pop()
    empty_deque.append(3)
    empty_deque.append(4)
    empty_deque.append(5)
    assert empty_deque.popleft() == 1


def test_pop_with_append_and_popleft(empty_deque):
    """Test pop will return correct value."""
    empty_deque.append(1)
    empty_deque.append(2)
    empty_deque.popleft()
    empty_deque.append(3)
    empty_deque.append(4)
    empty_deque.append(5)
    empty_deque.popleft()
    assert empty_deque.pop() == 5
