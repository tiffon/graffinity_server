from Graph import *


class FlightGraph(Graph):
    """ Implementation of a Graph object for converting from flight neo4j database to something for the frontend.
    """

    def __init__(self, graph):
        Graph.__init__(self, graph)

    def _get_edge_id(self, edge):
        return edge["id"]

    def _get_node_id(self, node):
        return node["id"]

    def _get_edge_as_dict(self, source, target, edge):
        edge_dictionary = {
                    "ID": Utils.get_property_as_int(edge, "id"),
                    "SourceID": Utils.get_property_as_int(source, "id"),
                    "TargetID": Utils.get_property_as_int(target, "id"),
                    "Carrier": edge["carrier"]
                }
        return edge_dictionary

    def _init_edge_attributes(self):
        self._edge_attributes.append({
            "Name": "ID",
            "DisplayName": "id",
            "Type": "int",
            "DataType": "index",
            "Unique": "true"
        })

        self._edge_attributes.append({
            "Name": "SourceID",
            "DisplayName": "source id",
            "Type": "int",
            "DataType": "source-index",
            "Unique": "false"
        })

        self._edge_attributes.append({
            "Name": "TargetID",
            "DisplayName": "target id",
            "Type": "int",
            "DataType": "target-index",
            "Unique": "true"
        })

        self._edge_attributes.append({
            "Name": "Carrier",
            "DisplayName": "carrier",
            "Type": "string",
            "DataType": "categorical",
            "Unique": "false"
        })

    def _init_node_attributes(self):

        self._node_attributes.append({
            "Name": "ID",
            "DisplayName": "id",
            "DatabaseName": "id",
            "Type": "int",
            "DataType": "index",
            "Unique": "true"
        })

        self._node_attributes.append({
            "Name": "Airport",
            "DisplayName": "airport",
            "DatabaseName": "airport",
            "Type": "string",
            "DataType": "id",
            "Unique": "true"
        })

        self._node_attributes.append({
            "Name": "city_name",
            "DisplayName": "city",
            "DatabaseName": "city_name",
            "Type": "string",
            "DataType": "categorical",
            "Unique": "false"
        })

        self._node_attributes.append({
            "Name": "state",
            "DisplayName": "state",
            "DatabaseName": "state",
            "Type": "string",
            "DataType": "categorical",
            "Unique": "false"
        })

        self._node_attributes.append({
            "Name": "market",
            "DisplayName": "market",
            "DatabaseName": "market",
            "Type": "string",
            "DataType": "categorical",
            "Unique": "false"
        })

        self._node_attributes.append({
            "Name": "degree",
            "DisplayName": "degree",
            "DatabaseName": "degree",
            "Type": "int",
            "DataType": "quantitative",
            "Unique": "false"
        })

        self._node_attributes.append({
            "Name": "lat",
            "DisplayName": "lat",
            "DatabaseName": "lat",
            "Type": "float",
            "DataType": "quantitative",
            "Unique": "false"
        })

        self._node_attributes.append({
            "Name": "lon",
            "DisplayName": "lon",
            "DatabaseName": "lon",
            "Type": "float",
            "DataType": "quantitative",
            "Unique": "false"
        })