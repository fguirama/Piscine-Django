import sys
from antigravity import geohash


def main():
    try:
        _, latitude, longitude, datetime = sys.argv
    except ValueError:
        raise Exception('usage: python3 geohashing.py [latitude] [longitude] [datetime]')

    try:
        lat = float(latitude)
    except ValueError:
        raise Exception('latitude must be numeric value')

    try:
        lon = float(longitude)
    except ValueError:
        raise Exception('longitude must be numeric value')

    if not (-90 <= lat <= 90):
        raise Exception('latitude must be between -90 and 90')
    if not (-180 <= lon <= 180):
        raise Exception('longitude must be between -180 and 180')

    geohash(lat, lon, datetime.encode())


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')
        exit(1)
