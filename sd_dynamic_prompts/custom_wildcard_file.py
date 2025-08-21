from __future__ import annotations

import re
from dynamicprompts.wildcards.collection.text_file import WildcardTextFile

class CustomWildcardTextFile(WildcardTextFile):
    """
    A custom wildcard text file that splits entries by blank lines.
    """
    def get_values(self) -> list[str]:
        if self._cache is not None:
            return self._cache

        with self._path.open(encoding=self._encoding, errors="ignore") as f:
            content = f.read()
            # Split by 2 or more newlines, and filter out empty strings
            entries = re.split(r'\n{2,}', content)
            self._cache = [entry.strip() for entry in entries if entry.strip()]
            return self._cache
