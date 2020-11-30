def get_data():  # MODEL
    return [
        {
            "name": "kevin",
            "score": 123
        },
        {
            "name": "nina",
            "score": 456
        }
    ]


def show_to_user(data):  # VIEW
    for item in data:
        print(f"Name: {item['name']}, Score: {item['score']}")


# main script - CONTROLLER
data = get_data()
show_to_user(data)
