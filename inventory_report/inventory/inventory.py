import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def read_csv(cls, path):
        with open(path) as file:
            return list(csv.DictReader(file))

    @classmethod
    def read_json(cls, path):
        with open(path) as file:
            return json.loads(file.read())

    @classmethod
    def read_xml(cls, path):
        with open(path) as file:
            return xmltodict.parse(file.read())["dataset"]["record"]

    @classmethod
    def import_data(cls, path, type_report):
        if path.endswith(".csv"):
            product_list = cls.read_csv(path)
        if path.endswith(".json"):
            product_list = cls.read_json(path)
        if path.endswith(".xml"):
            product_list = cls.read_xml(path)

        if type_report == "simples":
            result = SimpleReport.generate(product_list)
        else:
            result = CompleteReport.generate(product_list)
        return result
