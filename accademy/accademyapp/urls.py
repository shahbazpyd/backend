from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, StudentViewSet

router = DefaultRouter()

router.register("courses", CourseViewSet)
router.register("students", StudentViewSet)

urlpatterns = router.urls
