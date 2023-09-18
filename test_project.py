from project import add_to_list, add_to_category, sort_ingredients, load_from_csv



def main():
    test_add_to_list()
    test_sort_ingredients()
    test_add_to_category()
    test_load_from_csv()

def test_add_to_list():
    assert add_to_list("apple", 2) == {'apple': 2}
    assert add_to_list("apple", 2) == {'apple': 4}
    assert add_to_list("TP", 1) == {'apple': 4, 'TP': 1}

def test_sort_ingredients():
    unsorted_dict = {'crab sticks': 'meat', 'mayo': 'condiments', 'rice vinegar': 'condiments', 'cucumber': 'produce', 'sesame seeds': 'baking', 'paper towels': 'cleaning', 'oats': 'breakfast', 'greek yogurt': 'dairy', 'chia seeds': 'baking', 'oat milk': 'dairy'}
    assert sort_ingredients(unsorted_dict) == {'paper towels': 'cleaning', 'greek yogurt': 'dairy', 'oat milk': 'dairy', 'oats': 'breakfast', 'sesame seeds': 'baking', 'chia seeds': 'baking', 'mayo': 'condiments', 'rice vinegar': 'condiments', 'crab sticks': 'meat', 'cucumber': 'produce'}

def test_add_to_category():
    assert add_to_category('apple', 'produce') != {'apple': 'produce'}

def test_load_from_csv():
    assert load_from_csv("list.csv") == True
    assert load_from_csv("not a list.csv") == False

if __name__ == "__main__":
    main()