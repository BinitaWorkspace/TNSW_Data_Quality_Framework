def transform_passenger_data(data):

    transformed_data = []

    for row in data:

        cleaned_row = []

        for value in row:

            if isinstance(value, str):
                value = value.strip()

            cleaned_row.append(value)

        transformed_data.append(tuple(cleaned_row))

    return transformed_data


if __name__ == "__main__":

    sample_data = [
        (1001, " John ")
    ]

    print(transform_passenger_data(sample_data))