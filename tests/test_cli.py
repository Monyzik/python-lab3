from click.testing import CliRunner

from src.cli import loop, stack_cli


def test_cli_sorts():
    runner = CliRunner()
    result = runner.invoke(loop, input="sort quick 1 3 2")
    assert "1 2 3" in result.output
    result = runner.invoke(loop, input="sort bucket 1 3 2")
    assert "1 2 3" in result.output
    result = runner.invoke(loop, input="sort radix 1 3 2")
    assert "1 2 3" in result.output


def test_cli_fibonacci():
    runner = CliRunner()
    result = runner.invoke(loop, input="fibonacci 3")
    assert "2" in result.output
    result = runner.invoke(loop, input="fibonacci -r 3")
    assert "2" in result.output


def test_cli_factorial():
    runner = CliRunner()
    result = runner.invoke(loop, input="factorial 3")
    assert "6" in result.output
    result = runner.invoke(loop, input="factorial -r 3")
    assert "6" in result.output


def test_cli_stack():
    runner = CliRunner()
    runner.invoke(loop, input="stack push 5")
    runner.invoke(loop, input="stack peek")
    runner.invoke(loop, input="stack pop")
    runner.invoke(loop, input="stack is_empty")
    runner.invoke(loop, input="stack min")
    runner.invoke(loop, input="stack size")


def test_cli_queue():
    runner = CliRunner()
    runner.invoke(loop, input="queue enqueue 5")
    runner.invoke(loop, input="queue dequeue")
    runner.invoke(loop, input="queue front")
    runner.invoke(loop, input="queue is_empty")
    runner.invoke(loop, input="queue size")
