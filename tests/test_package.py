import re

import olpipeline


def test_olpipeline_has_version() -> None:
    assert re.match(r"\d+\.\d+\.\d+", olpipeline.__version__)
