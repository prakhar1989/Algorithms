"""
Find the maximum rectangle (in terms of area) under a histogram in linear time.
I mean the area of largest rectangle that fits entirely in the Histogram.


http://tech-queries.blogspot.in/2011/03/maximum-area-rectangle-in-histogram.html
http://stackoverflow.com/questions/4311694/maximize-the-rectangular-area-under-histogram
http://tech-queries.blogspot.in/2011/09/find-largest-sub-matrix-with-all-1s-not.html
http://stackoverflow.com/questions/3806520/finding-maximum-size-sub-matrix-of-all-1s-in-a-matrix-having-1s-and-0s

"""

# hist represented as ith bar has height h(i)
histogram = [6, 4, 2, 1, 3, 4, 5, 2, 6]

"""
steps -
1. Find Li - no. of adjacent bars to the left that have h >= h(i)
2. Find Ri - no. of adjacent bars to the right that have h >= h(i)
3. Area = h(i) * (L(i) + R(i) + 1)
4. compute max area
"""


def find_Li(hist, i):
    left_edge = 0
    for j in range(i-1, -1, -1):
        if hist[j] >= hist[i]:
            left_edge += 1
        else:
            return left_edge

    return left_edge


def find_Ri(hist, i):
    right_edge = 0
    for j in range(i + 1, len(hist)):
        if hist[j] >= hist[i]:
            right_edge += 1
        else:
            return right_edge

    return right_edge


def get_area(hist, i):
    return hist[i] * (find_Li(hist, i) + find_Ri(hist, i) + 1)


def get_max_area(hist):
    max_area = 0
    for i in range(len(hist)):
        area = get_area(hist, i)
        if area > max_area:
            max_area = area
    return max_area


def max_rectangle_area(histogram):
    """Find the area of the largest rectangle that fits entirely under
    the histogram.

    """
    stack = []
    top = lambda: stack[-1]
    max_area = 0
    pos = 0  # current position in the histogram
    for pos, height in enumerate(histogram):
        start = pos  # position where rectangle starts
        while True:
            if not stack or height > top()[1]:
                stack.append((start, height))  # push
            elif stack and height < top()[1]:
                max_area = max(max_area, top()[1] * (pos - top()[0]))
                start, _ = stack.pop()
                continue
            break  # height == top().height goes here

    pos += 1
    for start, height in stack:
        max_area = max(max_area, height * (pos - start))

    return max_area

print max_rectangle_area(histogram)
