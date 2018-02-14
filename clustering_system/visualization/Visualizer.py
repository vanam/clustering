from networkx import DiGraph, write_gexf


class Visualizer:

    def __init__(self):
        self.documents = {}

    def add_documents(self, docs: list, metadata: list, time: int):
        for doc, metadata in zip(docs, metadata):
            doc_id = metadata[0]
            # TODO load title, description
            self.documents[str(doc_id)] = [time, time, doc, []]  # (start_time, end_time, doc_vec, cluster_list)

    def set_cluster_for_doc(self, t, doc_id, cluster_id):
        self.documents[doc_id][1] = t + 1
        self.documents[doc_id][3].append((int(cluster_id), t, t + 1))

    def save(self, filename: str):
        graph = DiGraph(mode="dynamic")

        for doc_id, doc in self.documents.items():
            graph.add_node(
                doc_id,
                label=doc_id,
                start=doc[0],
                end=doc[1],
                cluster=doc[3],  # [(value, start, end), ...]
                # TODO save title, description
                # title="tit 1",
                # description="desc 1",
                viz={"position": {"x": doc[2][0], "y": doc[2][1], "z": 0}})

            # TODO add edges for dd-CRP

        write_gexf(graph, filename)