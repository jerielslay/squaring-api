from django.urls import path
from squaring_app.views import SquaringView

urlpatterns = [
    path('<int:number>/', SquaringView.as_view()),
]