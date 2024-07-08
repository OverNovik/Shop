from tastypie.resources import ModelResource

from shop.models import Category, Course
from .authentication import CustomAuthentication
from tastypie.authorization import Authorization


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = "category"
        allowed_methods = ["get"]


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = "courses"
        allowed_methods = ["get", "post", "delete"]
        exclude = ["created_at", "updated_at", "reviews_qty"]
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data["category_id"]
        return bundle

    def dehydrate(self, bundle):
        bundle.data["category_id"] = bundle.obj.category_id
        bundle.data["category"] = bundle.obj.category
        return bundle
