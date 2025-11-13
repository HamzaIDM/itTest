def load_file_to_list(filename):
    with open(filename, 'r') as file:
        city_tests_list = []
        lines = file.readlines()
        for line in lines:
            data = line.split()
            city_tests_list.append({
                "city": data[0],
                "NT": data[1],
                "NTP": data[2]
            })
    return city_tests_list


def display_city_tests(city_data):
    for key, value in city_data.items():
        print(f"{key}: {value}", end="\t\t")
    print()


def display_test_list(test_list):
    for info in test_list:
        display_city_tests(info)


def positivity_rate(city_data):
    NT = float(city_data["NT"])
    NTP = float(city_data["NTP"])

    return (NTP / NT) * 100 if (NT != 0) else 0


def display_positivity_rates(test_list):
    print("city\t\t\t\tPR")
    for info in test_list:
        print(f"{info['city']}\t\t\t\t{positivity_rate(info):.3f}%")


def store_pr_to_file(test_list, filename):
    with open(filename, "w") as prf:
        prf.write("city\t\t\t\tPR\n")
        for info in test_list:
            pr = positivity_rate(info)
            prf.write(f"{info['city']}\t\t\t\t{pr:.3f}%\n")


def national_positivity_rate(test_list):
    total_NTP, total_NT = 0, 0
    for data in test_list:
        total_NTP += float(data["NTP"])
        total_NT += float(data["NT"])
    if total_NT != 0:
        return (total_NTP / total_NT) * 100 if (total_NT != 0) else 0
    return 0


def danger_zone_city(city_data):
    pr = positivity_rate(city_data)
    if pr < 15:
        return "Green"
    elif pr <= 25:
        return "Orange"
    else:
        return "Red"


def display_danger_zone_cities(test_list):
    print("city\t\t\t\t\tState\n")
    for data in test_list:
        print(f"{data['city']}\t\t\t\t\t{danger_zone_city(data)}")


def count_cities_by_zone(test_list):
    Cgreen, Corange, Cred = 0, 0, 0
    for data in test_list:
        dangerColor = danger_zone_city(data)
        if dangerColor == "Green":
            Cgreen += 1
        elif dangerColor == "Orange":
            Corange += 1
        else:
            Cred += 1
    return {"Green": Cgreen, "Orange": Corange, "Red": Cred}


def store_statistics_to_file(test_list, filename):
    with open(filename, "w") as stat:
        stat.write("City\t\t\tNT\t\t\tNTP\t\t\tPR\t\t\tDanger_Zone\n")
        for data in test_list:
            stat.write(
                f"{data['city']}\t\t\t{data['NT']}\t\t\t{data['NTP']}\t\t\t{positivity_rate(data):.2f}%\t\t\t{danger_zone_city(data)}\n"
            )
        stat.write(f"\nNational Positivity Rate: {national_positivity_rate(test_list):.2f}%\n")
        zone_counts = count_cities_by_zone(test_list)
        stat.write(f"Green zone: {zone_counts['Green']}\tOrange zone: {zone_counts['Orange']}\tRed zone: {zone_counts['Red']}\n")


def main():
    print("This is really exciting!!\n")
    L = load_file_to_list("testsCovid19.txt")
    display_test_list(L)

    zone_counts = count_cities_by_zone(L)
    print(f"Green zone: {zone_counts['Green']}\tOrange zone: {zone_counts['Orange']}\tRed zone: {zone_counts['Red']}\n")

    print(f"\nNational Positivity Rate: {national_positivity_rate(L):.2f}%")

    store_statistics_to_file(L, "statisticsCovid19.txt")


if __name__ == "__main__":
    main()
