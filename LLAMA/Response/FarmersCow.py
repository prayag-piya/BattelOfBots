from math import hypot

def farmers_cow_main(p, n, polygon_points, query_points):
    """
    Main logic for FarmersCow problem, structured for testing.
    Parameters:
        p (int): Number of polygon points.
        n (int): Number of queries.
        polygon_points (list): List of (x, y) tuples defining the polygon.
        query_points (list): List of (x1, y1, x2, y2) tuples for queries.
    Returns:
        list: List of minimum distances for each query.
    """
    px, py = [], []
    # Handle polygon points
    for x, y in polygon_points:
        px.append((x, y))
        if px[-1] != px[0]: 
            px.append(px[0])

    results = []
    # Handle query points
    for x1, y1, x2, y2 in query_points:
        x1 -= px[0][0]
        y1 -= px[0][1]
        x2 -= px[0][0]
        y2 -= px[0][1]
        s = hypot(x2 - x1, y2 - y1)
        t = hypot((px[-1][0] - x1) + (x2 - px[0][0]), (px[-1][1] - y1) + (y2 - px[0][1]))
        results.append(min(s, t))
    return results
