from hobby.utils import define_hobbies
from language.utils import define_languages
from availability.utils import define_days
from website_users.utils import define_age_ranges
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def get_hobby_list():
    """Convert hobby choices tuple int a list and return a hobby list."""
    return [item[1] for item in define_hobbies()]


def get_language_list():
    """Convert hobby choices tuple int a list and return a hobby list."""
    return [item[1] for item in define_languages()]


def get_day_list():
    """Convert hobby choices tuple int a list and return a hobby list."""
    return [item[1] for item in define_days()]


def get_age_range_list():
    """Convert hobby choices tuple int a list and return a hobby list."""
    return [item[1] for item in define_age_ranges()]


def paginate_results(search_results, page_number, results_per_page):
    """Paginate search results."""

    # Credit: https://www.youtube.com/watch?v=YlMxfqcw77s
    # Learned how to paginate filtered objects
    
    search_results = search_results
    paginator = Paginator(search_results, results_per_page)
    
    # Try paginating with different numbers of results per page
    try:
        search_results = paginator.page(page_number)
    except PageNotAnInteger:
        search_results = paginator.page(results_per_page)  # specified number
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return search_results