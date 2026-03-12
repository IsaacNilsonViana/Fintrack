from app.schemas import CategoryCreate

def test_create_category(db_session):
    data = CategoryCreate(
        user_id = 1,
        name = "Alimentação",
        type = "expense"
    )

    category = create_category(db_session, data)

    assert category is not None
    assert category.id is not None
    assert category.user_id == 1
    assert category.name == "Alimentação"
    assert category.type == "expense"