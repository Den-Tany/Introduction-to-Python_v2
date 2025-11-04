# test файл
import pytest
from shop_03 import Shop
@pytest.mark.parametrize("result", ["$58.29"])
def test_time_wait(result):
    shop = Shop()
    shop.startWeb()
    shop.auth()
    shop.choice()
    shop.filling_out_the_form()
    total_coast = shop.total_cost()
    shop.quit()
    print(result)
    assert result == total_coast

# import pytest
# from shop_03 import Shop

# @pytest.fixture(scope="module")
# def setup():
#     shop = Shop()
#     yield shop
#     shop.quit()

# @pytest.mark.parametrize("expected_result", ["$58.29"])  # Без слова "Total:"
# def test_total_cost(setup, expected_result):
#     shop = setup
#     shop.startWeb()
#     shop.auth()
#     shop.choice()
#     shop.filling_out_the_form()
#     actual_result = shop.total_cost()
#     assert expected_result == actual_result


