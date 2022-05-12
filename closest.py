import csv
import itertools

from haversine import haversine


if __name__ == '__main__':
    with open('spoons.csv', newline='') as f:
        reader = csv.DictReader(f)
        pubs = list(reader)

    pub_pairs = []
    for pub_a, pub_b in itertools.combinations(pubs, 2):
        distance = haversine(
            (float(pub_a['lat']), float(pub_a['lng'])), 
            (float(pub_b['lat']), float(pub_b['lng'])),
        )
        pub_pairs.append({
            'pub_a': pub_a,
            'pub_b': pub_b,
            'distance': distance,
        })

    pub_pairs.sort(key=lambda c: c['distance'])

    for index, pair in enumerate(pub_pairs[:10], 1):
        print(f'#{index}')
        print(f'Pub A: {pair["pub_a"]["name"]}, {pair["pub_a"]["city"]}')
        print(f'Pub B: {pair["pub_b"]["name"]}, {pair["pub_b"]["city"]}')
        print(f'Distance: {pair["distance"]:.3f}km')
        print()
