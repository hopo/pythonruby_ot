
urlpatterns = [
    # AdminSite
    url(r'^admin/', admin.site.urls, ''),

    # 메인
    url(r'^', include('main.urls', namespace='main'), ''),

    # 검색
    url(r'^search/', include('search.urls', namespace='search'), ''),

    # 유저
    url(r'^users/', include('users.urls', namespace='users'), ''),

    # 기획단공
    url(r'^planning/', include('planning.urls', namespace='planning'), ''),

    # 바로단공
    url(r'^straight/', include('straight.urls', namespace='straight'), ''),

    # 이벤트
    url(r'^events/', include('event.urls', namespace='event'), ''),

    # 커스텀 페이지
    url(r'^page/', include('page.urls', namespace='page'), name='page'),

    # Third Party URL
    url(r'^redactor/', include('redactor.urls'), ''),
    url(r'^billing/', include('billing.urls', namespace='billing'), name='billing'),
    url(r'^summernote/', include('django_summernote.urls'), ''),
    url(r'^ckeditor/', include('ckeditor_uploader.urls'), ''),

    # favicon.ico
    url(r'^favicon\.ico', RedirectView.as_view(url='/static/img/logo_16_16.png', permanent=True)),

    # robots.txt
    url( r'^robots\.txt', lambda x: HttpResponse('User-Agent: *\nDisallow: /admin/\nDisallow: /static/', content_type='text/plain'), name='robots_file'),

    # fb_dangong
    url(r'^qqahzij96og8d4dsi6d3obs9z9fnvj\.html', lambda x: HttpResponse('qqahzij96og8d4dsi6d3obs9z9fnvj', content_type='text/plain'), name='fb_dangong')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

# ============================================
# *** planning/urls.py
# ============================================
urlpatterns = [
    # 전체
    url(r'^all$', PlanningAllView.as_view(), name='planning_all'),
    url(r'^doing$', DoingPlanningView.as_view(), name='planning_doing'),
    url(r'^ended$', EndedPlanningView.as_view(), name='planning_ended'),

    # 상세
    url(r'^(?P<planning_id>\d+)$', PlanningDetail.as_view(), name='planning_detail'),

    # Order
    url(r'^order/detail$', OrderDetail.as_view(), name='planning_order_detail'),
    url(r'^order/save$', OrderSave.as_view(), name='planning_order_save'),

    # FAQ
    url(r'^(?P<p2s_id>\d+)/faq$', FAQRegister.as_view(), name='faq_register'),
    url(r'^(?P<p2s_id>\d+)/faq/(?P<faq_id>\d+)/update$', FAQUpdate.as_view(), name='faq_update'),
    url(r'^(?P<p2s_id>\d+)/faq/(?P<faq_id>\d+)/remove$', FAQRemove.as_view(), name='faq_remove'),

    # Review
    url(r'^(?P<p2s_id>\d+)/review$', ReviewRegister.as_view(), name='review_register'),
    url(r'^(?P<p2s_id>\d+)/review/(?P<review_id>\d+)/update$', ReviewUpdate.as_view(), name='review_update'),
    url(r'^(?P<p2s_id>\d+)/review/(?P<review_id>\d+)/remove$', ReviewRemove.as_view(), name='review_remove'),
    url(r'^(?P<p2s_id>\d+)/review/filter$', ReviewFilter.as_view(), name='review_filter'),

    # 공유
    url(r'^fb-share/(?P<planning_id>\d+)$', ShareFacebook.as_view(), name='planning_fb_share'),
]

# ============================================
# *** straight/urls.py
# ============================================
urlpatterns = [
    url(r'^all$', StraightAllView.as_view(), name='straight_all'),

    url(r'^(?P<straight_id>\d+)$', StraightDetail.as_view(), name='straight_detail'),
    url(r'^(?P<straight_id>\d+)/basket$', BasketInsert.as_view(), name='straight_basket_insert'),
    url(r'^order/detail$', OrderDetail.as_view(), name='straight_order_detail'),
    url(r'^order/save$', OrderSave.as_view(), name='straight_order_save'),

    url(r'^basket$', BasketList.as_view(), name='straight_basket_list'),
    url(r'^basket/all-order$', BasketAllOrder.as_view(), name='straight_basket_all_order'),
    url(r'^basket/select-order$', BasketSelectOrder.as_view(), name='straight_basket_select_order'),
    url(r'^basket/delete$', BasketDeleteView.as_view(), name='straight_basket_delete'),
    url(r'^basket/(?P<basket_id>\d+)/quantity$', BasketQuantity.as_view(), name='straight_basket_quantity'),
    url(r'^basket/(?P<basket_id>\d+)/remove$', BasketRemove.as_view(), name='straight_basket_remove'),

    url(r'^fb-share/(?P<straight_id>\d+)$', ShareFacebook.as_view(), name='straight_fb_share'),
    
    url(r'^recoverorderedstock$', RecoverOrderedStock.as_view(), name='straight_recoverorderedstock') # @@@
]

# ============================================
# *** users/urls.py
# ============================================

urlpatterns = [
    url(r'^terms-register$', UserRegisterTerm.as_view(), name='terms_register'),
    url(r'^register$', UserRegister.as_view(), name='register'),
    url(r'^login/$', user_login, name='login'),
    url(r'^kakao_login/$', kakao_login, name='kakao_login'),
    url(r'^kakao_logout/$', kakao_logout, name='kakao_logout'),
    url(r'^oauth/$', oauth, name='oauth'),
    url(r'^fb-login$', facebook_login, name='fb_login'),
    url(r'^naver_login_session/$', naver_login_session, name='naver_login_session'),
    url(r'^naver-auth/$', TemplateView.as_view(template_name='users/naver_auth.html'), name='naver_auth'),
    url(r'^naver-login/$', naver_login, name='naver_login'),
    url(r'^logout$', user_logout, name='logout'),
    url(r'^find-password$', FindPassword.as_view(), name='find_password'),
    url(r'^temp-auth/(?P<temp_token>.*)$', TempPasswordChange.as_view(), name='temp_auth'),
    url(r'^register/complete/(?P<register_type>.*)$', RegisterComplete.as_view(), name='register_complete'),

    url(r'^my-info$', MyInfo.as_view(), name='my_info'),
    url(r'^my-password-change$', MyPasswordChange.as_view(), name='my_password_change'),

    url(r'^my-order-inquiry$', MyOrderInquiry.as_view(), name='my_order_inquiry'),
    url(r'^my-order-inquiry/straight/add$', MyStraightInquiryAdd.as_view(), name='my_straight_inquiry_add'),
    url(r'^my-order-inquiry/review$', MyOrderInquiryReview.as_view(), name='my_order_inquiry_review'),
    url(r'^my-order-inquiry/address$', MyOrderInquiryAddress.as_view(), name='my_order_inquiry_address'),
    url(r'^my-order-inquiry/quantity$', MyOrderInquiryQuantity.as_view(), name='my_order_inquiry_quantity'),
    url(r'^my-order-inquiry/survey$', MyOrderInquirySurvey.as_view(), name='my_order_inquiry_survey'),

    url(r'^my-faq$', MyFAQ.as_view(), name='my_faq'),
    url(r'^my-faq/(?P<p2s_id>\d+)/faq/(?P<faq_id>\d+)/update$', MyFAQUpdate.as_view(), name='my_faq_update'),
    url(r'^my-faq/(?P<p2s_id>\d+)/faq/(?P<faq_id>\d+)/remove$', MyFAQRemove.as_view(), name='my_faq_remove'),

    url(r'^my-review$', MyReview.as_view(), name='my_review'),
    url(r'^my-review/(?P<p2s_id>\d+)/review/(?P<review_id>\d+)/update$', MyReviewUpdate.as_view(), name='my_review_update'),
    url(r'^my-review/(?P<p2s_id>\d+)/review/(?P<review_id>\d+)/remove$', MyReviewRemove.as_view(), name='my_review_remove'),
    url('^my-cards/$', RegisterCardView.as_view(), name='my_cards'),
    url(r'^cards/(?P<pk>[-\d]+)/delete/$', DeleteCardView.as_view(), name='card_delete'),
    url(r'^address-book$', AddressBookCall.as_view(), name='address_book_call'),
    url(r'^address-history$', AddressHistory.as_view(), name='address_history'),
]

# ============================================
# *** billing/urls.py
# ============================================
urlpatterns = [
    url(r'^cancel/planning/order/(?P<planning_o_id>\d+)$', OrderPlanningCancel.as_view(), name='planning_cancel'),
    url(r'^cancel/straight/order/(?P<straight_o_id>\d+)$', OrderStraightCancel.as_view(), name='straight_cancel'),
    url(r'^checksavedcard$', CheckSavedCard.as_view(), name='check_cardnumber'),
]

