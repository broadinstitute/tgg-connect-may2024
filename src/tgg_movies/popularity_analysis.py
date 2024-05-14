import hail as hl


def calculate_movies_avg_rating(joint: hl.Table):
    movies_avg_rating = joint.group_by(joint.id, joint.title).aggregate(
        avg_rating=hl.agg.mean(joint.rating)
    )
    return movies_avg_rating


def sort_movies_by_rating(movies_avg_rating: hl.Table, top: bool = True, n: int = 10):
    sorted_movies = movies_avg_rating.order_by(
        hl.desc(movies_avg_rating.avg_rating)
        if top
        else hl.asc(movies_avg_rating.avg_rating)
    )
    return sorted_movies.head(n)
