#!/usr/bin/env python

import json
from pathlib import Path

output = []
with open("/app/coverage.summary.json", "w") as f:
    for path in Path('/app/vol/').iterdir():
        # Read the configuration first.
        options = path / 'options.json'
        options = options.read_text()
        summary = json.loads(options)
        coverage = path / 'coverage.json'
        coverage = coverage.read_text()
        coverage = json.loads(coverage)
        # https://gcovr.com/en/5.0/guide.html#json-summary-output
        coverage.pop('files')
        coverage.pop('gcovr/summary_format_version')
        coverage.pop('root')
        summary["coverage"] = coverage
        output.append(summary)
    json.dump(output, f)
