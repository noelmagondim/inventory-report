from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def count_products(product_list):
        products_stocked = dict()
        for product in product_list:
            companies = product["nome_da_empresa"]
            if companies in products_stocked:
                products_stocked[companies] += 1
            else:
                products_stocked[companies] = 1
        return products_stocked

    @staticmethod
    def generate(product_list):
        simple_report = SimpleReport.generate(product_list)
        report_data = CompleteReport.count_products(product_list)
        products_stocked = ""
        items = report_data.items()

        for each, value in items:
            products_stocked += f"- {each}: {value}\n"

        result = (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{products_stocked}"
        )
        return result
