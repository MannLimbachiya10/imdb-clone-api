from rest_framework.throttling import UserRateThrottle

class ReviewCreatethrottle(UserRateThrottle):
    scope = 'review-create'

class ReviewListthrottle(UserRateThrottle):
    scope = 'review-list'