from django.urls import path, include
from adminPanel import views
from products import views as product_views
from category import views as category_views
from sale import views as sale_views
from order import views as order_views
from user import views as user_views
from app import views as app_views

app_name = 'adminPanel'
urlpatterns = [
    # dashboard url
    path('', views.Index),

    # user management
    path('/users', user_views.Users.as_view(), name='admin_users'),
    # path('/users/add', user_views.AddUsers.as_view(), name='add_user'),

    # products management
    path('/products', product_views.Products.as_view(), name='admin_products'),
    path('/products/<int:pk>', product_views.ProductView.as_view(), name='admin_product'),
    path('/products/edit/<int:pk>', product_views.UpdateProduct.as_view(), name='edit_product'),
    path('/products/delete/<int:pk>', product_views.DeleteProduct.as_view(), name='delete_product'),
    path('/products/add', product_views.AddProduct.as_view(), name='add_product'),
    path('/products/addinstance/<int:pk>', product_views.AddInstance.as_view(), name='add_instance'),
    path('/products/<int:product>/<int:pk>/deleteinstance', product_views.DeleteInstance.as_view(),
         name='delete_instance'),
    path('/products/updateinstance/<int:product>/<int:pk>', product_views.UpdateInstance.as_view(),
         name='update_instance'),

    path('/upload', app_views.ajax_upload),
    path('/<str:directory>/<str:id>/delete', app_views.delete_file),

    # category management
    path('/categories', category_views.Categories.as_view(), name='admin_categories'),
    path('/categories/<int:pk>', category_views.Categoryy.as_view(), name='admin_category'),
    path('/categories/add', category_views.AddCategory.as_view(), name='add_category'),
    path('/categories/addfamilly', category_views.AddProductFamily.as_view(), name='add_productfamily'),
    path('/categories/productfamilies', category_views.ProductFamilies.as_view(), name='admin_productfamilies'),
    path('/categories/productfamilies/edit/<int:pk>', category_views.EditProductFamily.as_view(),
         name='edit_productfamily'),
    path('/categories/productfamilies/delete/<int:pk>', category_views.DeleteProductFamily.as_view(),
         name='delete_productfamily'),
    path('/categories/edit/<int:pk>', category_views.EditCategory.as_view(), name='edit_category'),
    path('/categories/delete/<int:pk>', category_views.DeleteCategory.as_view(), name='delete_category'),

    # discount and bonus management
    path('/discounts', sale_views.Discounts.as_view(), name='admin_discounts'),
    path('/discounts/add', sale_views.AddDiscount.as_view(), name='add_discount'),
    path('/discounts/edit/<int:pk>', sale_views.EditDiscount.as_view(), name='edit_discount'),
    path('/discounts/delete/<int:pk>', sale_views.DeleteDiscount.as_view(), name='delete_discount'),

    path('/bonuses', sale_views.Bonuses.as_view(), name='admin_bonuses'),
    path('/bonuses/add', sale_views.AddBonus.as_view(), name='add_bonus'),
    path('/bonuses/edit/<int:pk>', sale_views.EditBonus.as_view(), name='edit_bonus'),
    path('/bonuses/delete/<int:pk>', sale_views.DeleteBonus.as_view(), name='delete_bonus'),

    # order management
    path('/orders', order_views.Orders.as_view(), name='admin_orders'),
    path('/orders/add', order_views.AddOrder.as_view(), name='add_order'),
    path('/calendar', views.Calender, name='admin_calendar')
]
