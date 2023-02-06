# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import *


admin.site.site_header = "Nubatar"



# CONTACT ADMIN
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['email', 'first_name', 'last_name', 'active', 'timestamp']
    list_display_links  = ['email',]
    list_filter         = ['email']
    search_fields       = ['email', 'first_name', 'last_name']
    list_per_page       = 25
    class Meta:
        model = Contact
admin.site.register(Contact, ContactAdmin)










# SUCRIBER ADMIN
class SubscriberAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['email', 'active', 'timestamp', 'updated']
    list_display_links  = ['email',]
    list_filter         = ['email']
    search_fields       = ['email', ]
    list_per_page       = 25
    class Meta:
        model = Subscriber
admin.site.register(Subscriber, SubscriberAdmin)













# BLOG CATEGORY ADMIN
class BlogCategoryAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['name', 'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name', ]
    list_per_page       = 25
    class Meta:
        model = BlogCategory
admin.site.register(BlogCategory, BlogCategoryAdmin)









# BLOG ADMIN
class BlogAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['category','name', 'active', 'timestamp', 'updated']
    list_display_links  = ['category',]
    list_filter         = ['name']
    search_fields       = ['category__name', 'active', 'name',]
    list_per_page       = 25
    class Meta:
        model = Blog
admin.site.register(Blog, BlogAdmin)












# BLOG COMMENT ADMIN
class BlogCommentAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['blog', 'name', 'email', 'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['blog__name', 'name', 'email', 'active', ]
    list_per_page       = 25
    class Meta:
        model = BlogComment
admin.site.register(BlogComment, BlogCommentAdmin)









# TESTIMONY ADMIN
class TestimonyAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['full_name', 'active', 'timestamp', 'updated']
    list_display_links  = ['full_name',]
    list_filter         = ['full_name']
    search_fields       = ['full_name', ]
    list_per_page       = 25
    class Meta:
        model = Testimony
admin.site.register(Testimony, TestimonyAdmin)








# PRODUCT IMAGE  ADMIN

class StockAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['description', 'active', 'timestamp', 'updated']
    list_display_links  = ['description',]
    list_filter         = ['description']
    search_fields       = ['name', 'active', ]
    list_per_page       = 25
    class Meta:
        model = Stock
admin.site.register(Stock, StockAdmin)






# PRODUCT IMAGE  ADMIN

class ProductImageAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['file','name', 'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name', 'active', ]
    list_per_page       = 25
    class Meta:
        model = Product
admin.site.register(ProductImage, ProductImageAdmin)







# PRODUCT SUPPLIER  ADMIN

class SupplierAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['name', 'email',  'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name', 'active', ]
    list_per_page       = 25
    class Meta:
        model = Supplier
admin.site.register(Supplier, SupplierAdmin)






# PRODUCT CATEGORY  ADMIN

class ProductCategoryAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['name', 'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name', 'active', ]
    list_per_page       = 25
    class Meta:
        model = ProductCategory
admin.site.register(ProductCategory, ProductCategoryAdmin)









# PRODUCT  ADMIN

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['name', 'category', 'brand_name', 'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name', 'category', 'brand_name', 'active', ]
    list_per_page       = 25
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)








# PHARMACY CATEGORY  ADMIN

class PharmacyCategoryAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['name', 'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name', 'active', ]
    list_per_page       = 25
    class Meta:
        model = PharmacyCategory
admin.site.register(PharmacyCategory, PharmacyCategoryAdmin)





# PHARMACY  ADMIN

class PharmacyAdmin(admin.ModelAdmin):
    date_hierarchy      = 'timestamp'
    list_display        = ['name', 'location', 'address', 'category', 'start_hour', 'end_hour', 'start_day', 'end_day', 'active', 'timestamp', 'updated']
    list_display_links  = ['name',]
    list_filter         = ['name']
    search_fields       = ['name', 'location', 'category', 'active', ]
    list_per_page       = 25
    class Meta:
        model = Pharmacy
admin.site.register(Pharmacy, PharmacyAdmin)
















