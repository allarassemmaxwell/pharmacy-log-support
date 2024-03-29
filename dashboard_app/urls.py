from django.urls import path
from .views import *
from . import views
# from .api import *
urlpatterns = [
    # ==================================================
    #                     DASHBOARD URLS
    # ==================================================
    path('', dashboard_view, name="dashboard"),
    path('profile/', profile_view, name="profile"),
    path('blog/', blog_view, name="blog"),
    path('blog/add/', blog_add_view, name="blog_add"),
    path('blog/delete/<slug:slug>/', blog_delete_view, name="blog_delete"),
    path('blog/update/<slug:slug>/', blog_update_view, name="blog_update"),

    path('blog-category/', blog_category_view, name="blog_category"),
    path('blog-category/add/', blog_category_add_view, name="blog_category_add"),
    path('blog-category/delete/<slug:slug>/', blog_category_delete_view, name="blog_category_delete"),
    path('blog-category/update/<slug:slug>/', blog_category_update_view, name="blog_category_update"),

    

    path('contacts/', contact_view, name="contact"),
    path('contacts/delete/<int:id>/', contact_delete_view, name="contact_delete"),
    path('contacts/respond/<slug:slug>/', contact_responde_view, name="contact_respond"),
    path('newsletters/response/', response_contact_view, name="response_contact"),

    path('newsletters/', newsletter_view, name="newsletter"),
    path('newsletters/add/', newsletter_add_view, name="newsletter_add"),
    path('newsletters/delete/<int:id>/', newsletter_delete_view, name="newsletter_delete"),
    path('newsletters/update/<int:id>/', newsletter_update_view, name="newsletter_update"),


    path('newsletters/list/', mail_newsletter_view, name="mail_newsletter"),
    path('newsletters/list/add/', mail_newsletter_add_view, name="mail_add_newsletter"),

    path('partner/', partner_view, name="partner"),
    path('partner/add/', partner_add_view, name="partner_add"),
    path('partner/delete/<slug:slug>/', partner_delete_view, name="partner_delete"),
    path('partner/update/<slug:slug>/', partner_update_view, name="partner_update"),

    path('testimony/', testimony_view, name="testimony"),
    path('testimony/add/', testimony_add_view, name="testimony_add"),
    path('testimony/delete/<int:id>/', testimony_delete_view, name="testimony_delete"),
    path('testimony/update/<int:id>/', testimony_update_view, name="testimony_update"),

    path('user/', user_view, name="user"),
    path('user/add/', user_add_view, name="user_add"),
    path('user/delete/<str:id>/', user_delete_view, name="user_delete"),
    path('user/update/<str:id>/', user_update_view, name="user_update"),

    
    path('service/category/', service_category_view, name="service_category"),
    path('service/category/delete/<slug:slug>/', service_category_delete_view, name="service_category_delete"),
    path('service/category/update/<slug:slug>/', service_category_update_view, name="service_category_update"),


    path('service/', service_view, name="service"),
    path('service/add/', service_add_view, name="service_add"),
    path('service/delete/<slug:slug>/', service_delete_view, name="service_delete"),
    path('service/update/<slug:slug>/', service_update_view, name="service_update"),
    

    path('product/', product_view, name="product"),
    path('product/add/', product_add_view, name="product_add"),
    path('product/delete/<slug:slug>/', product_delete_view, name="product_delete"),
    path('product/update/<slug:slug>/', product_update_view, name="product_update"),


    path('product/image/', product_image_view, name="product_image"),
    path('product/image/delete/<slug:slug>/', product_image_delete_view, name="product_image_delete"),
    path('product/image/update/<slug:slug>/', product_image_update_view, name="product_image_update"),


    path('product/category/', product_category_view, name="product_category"),
    path('product/category/delete/<slug:slug>/', product_category_delete_view, name="product_category_delete"),
    path('product/category/update/<slug:slug>/', product_category_update_view, name="product_category_update"),


    path('supplier/', supplier_view, name="supplier"),
    path('supplier/add/', supplier_add_view, name="supplier_add"),
    path('supplier/delete/<slug:slug>/', supplier_delete_view, name="supplier_delete"),
    path('supplier/update/<slug:slug>/', supplier_update_view, name="supplier_update"),
    
    
    path('stock/', stock_view, name="stock"),
    path('stock/add/', stock_add_view, name="stock_add"),
    path('stock/delete/<str:id>/', stock_delete_view, name="stock_delete"),
    path('stock/update/<str:id>/', stock_update_view, name="stock_update"),
    path('stock_detail/<uuid:id>/', stock_detail_view, name="stock_detail"),
    
    
    path('stock/category/', stock_category_view, name="stock_category"),
    path('stock/category/delete/<slug:slug>/', stock_category_delete_view, name="stock_category_delete"),
    path('stock/category/update/<slug:slug>/', stock_category_update_view, name="stock_category_update"),

    
    path('issue_items/<uuid:id>/', issue_items_view, name="issue_items"),
    path('receive_items/<uuid:id>/', receive_items_view, name="receive_items"),
    path('reorder_level/<uuid:id>/', reorder_level_view, name="reorder_level"),
    
    
    path('appointment/symptoms/', appointment_symptom_view, name="appointment_symptom"),
    path('appointment/symptoms/delete/<slug:slug>/', appointment_symptom_delete_view, name="appointment_symptom_delete"),
    path('appointment/symptoms/update/<slug:slug>/', appointment_symptom_update_view, name="appointment_symptom_update"),

    path('appointment/', appointment_view, name="appointment"),
    path('appointment/add', appointment_add_view, name="appointment_add"),
    path('appointment/delete/<str:id>/', appointment_delete_view, name="appointment_delete"),
    path('appointment/update/<str:id>/', appointment_update_view, name="appointment_update"),
    path('appointment/detail/<str:id>/', appointment_detail_view, name="appointment_detail"),


    path('appointment/prescription/', appointment_prescription_view, name="appointment_prescription"),
    path('appointment/prescription/add/', appointment_prescription_add_view, name="appointment_prescription_add"),
    path('appointment/prescription/delete/<int:id>/', appointment_prescription_delete_view, name="appointment_prescription_delete"),
    path('appointment/prescription/update/<int:id>/', appointment_prescription_update_view, name="appointment_prescription_update"),

    path('patient/', patient_view, name="patient"),
    path('patient/add/', patient_add_view, name="patient_add"),
    path('patient/delete/<slug:slug>/', patient_delete_view, name="patient_delete"),
    path('patient-user/delete/<slug:slug>/', patient_user_delete_view, name="patient_user_delete"),
    path('patient/update/<slug:slug>/', patient_update_view, name="patient_update"),
    
    
    path('sale/', sale_view, name="sale"),
    path('sale/add/', sale_add_view, name="sale_add"),
    path('sale/delete/<str:id>/', sale_delete_view, name="sale_delete"),
    path('sale/update/<str:id>/', sale_update_view, name="sale_update"),
    path('sale/<str:id>/', sale_visualization_view, name='sale_visualization'),
    path('sale-pdf/<str:id>/', get_sale_pdf_view, name="sale_pdf"),
    
    
    # fridge management
    path('fridge/', fridge_view, name="fridge"),
    path('fridge/add/', fridge_add_view, name="fridge_add"),
    path('fridge/delete/<int:id>/', fridge_delete_view, name="fridge_delete"),
    path('fridge/update/<int:id>/',fridge_update_view, name="fridge_update"),
    
    
    # For Report  daily, weekly, monthly and annually
    
    path('rapport-quotidien/', rapport_quotidien_view, name="rapport_quotidien"), 
    path('rapport-hebdomadaire/', rapport_hebdomadaire_view, name="rapport_hebdomadaire"), 
    path('rapport-mensuel/', rapport_mensuel_view, name="rapport_mensuel"), 
    path('rapport-annuel/', rapport_annuel_view, name="rapport_annuel"),
    
    # For PDF Rapport 
    path('rapport-quotidien-pdf/', get_rapport_quotidien_pdf_view, name="rapport_quotidien_pdf"),
    path('rapport-hebdomadaire-pdf/', get_rapport_hebdomadaire_pdf_view, name="rapport_hebdomadaire_pdf"),
    path('rapport-mensuel-pdf/', get_rapport_mensuel_pdf_view, name="rapport_mensuel_pdf"),
    path('rapport-annuel-pdf/', get_rapport_annuel_pdf_view, name="rapport_annuel_pdf"),
    
    
    # Liens d'acces a la Notification,  add, detail, mise a jour et suppression
    
    path('notification/', notification_view, name="notification"),


    path('api/products/', productList, name="api_product_list"),


]




