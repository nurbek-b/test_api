from rest_framework import routers
from rental_app import views as myapp_views


router = routers.DefaultRouter()

router.register('friends', myapp_views.FriendViewset)
router.register('belongings', myapp_views.BelongingViewset)
router.register('borrowings', myapp_views.BorrowedViewset)