class SimpleReport:
    @staticmethod
    def earliest_manufacturing_date(product_list):
        return min(
            [
                each["data_de_fabricacao"]
                for each in product_list
            ]
        )

    @staticmethod
    def closest_expiration_date(product_list):
        return min(
            [
                each["data_de_validade"]
                for each in product_list
            ]
        )

    @staticmethod
    def company_with_more_products(product_list):
        companies = {}
        for product in product_list:
            if product["nome_da_empresa"] in companies:
                companies[product["nome_da_empresa"]] += 1
            else:
                companies[product["nome_da_empresa"]] = 1
        return max(companies, key=companies.get)

    @staticmethod
    def generate(products):
        earliest_manufacturing = SimpleReport.earliest_manufacturing_date(
            products
        )
        closest_expiration = SimpleReport.closest_expiration_date(products)
        company_more_products = SimpleReport.company_with_more_products(
            products
        )

        result = (
            f"Data de fabricação mais antiga: {earliest_manufacturing}\n"
            f"Data de validade mais próxima: {closest_expiration}\n"
            f"Empresa com mais produtos: {company_more_products}"
        )

        return result
