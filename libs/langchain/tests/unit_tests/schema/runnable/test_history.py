from langchain.schema.runnable.history import __all__

EXPECTED_ALL = ["RunnableWithMessageHistory"]


def test_all_imports() -> None:
    assert set(__all__) == set(EXPECTED_ALL)
