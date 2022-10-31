from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        10,
        "Titanium Dioxide",
        "Target Corporation",
        "2020-12-08",
        "2023-12-08",
        "FR29 5791 5333 58XR G4PR IG28 D08",
        "local seco",
    )

    assert (
        str(product) == (
            f"O produto {product.nome_do_produto}"
            f" fabricado em {product.data_de_fabricacao}"
            f" por Target Corporation com validade"
            f" até {product.data_de_validade}"
            f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
        )
    )
