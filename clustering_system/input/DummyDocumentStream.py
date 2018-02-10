from typing import Sequence

from clustering_system.input.IDocumentStream import IDocumentStream


class DummyDocumentStream(IDocumentStream):

    def __init__(self, documents: Sequence[str]):
        super().__init__()
        self.i = 0
        self.documents = documents

    def __iter__(self):
        """
        Return dummy documents one by one containing random string.
        """
        while self.i < len(self.documents):
            line = self.documents[self.i]
            self.i += 1

            # assume there's one document per line, tokens separated by whitespace
            yield self._process(line)