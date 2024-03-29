(function($) {
    "use strict";
    $('#pricing_select input[name="rating_option"]').on('click', function() {
        if ($(this).val() == 'price_free') {
            $('#custom_price_cont').hide();
        }
        if ($(this).val() == 'custom_price') {
            $('#custom_price_cont').show();
        } else {}
    });
    $(".education-info").on('click', '.trash', function() {
        $(this).closest('.education-cont').remove();
        return false;
    });
    $(".add-education").on('click', function() {
        var educationcontent = '<div class="row form-row education-cont">' +
            '<div class="col-12 col-md-10 col-lg-11">' +
            '<div class="row form-row">' +
            '<div class="col-12 col-md-6 col-lg-4">' +
            '<div class="form-group">' +
            '<label>Degree</label>' +
            '<input type="text" class="form-control">' +
            '</div>' +
            '</div>' +
            '<div class="col-12 col-md-6 col-lg-4">' +
            '<div class="form-group">' +
            '<label>College/Institute</label>' +
            '<input type="text" class="form-control">' +
            '</div>' +
            '</div>' +
            '<div class="col-12 col-md-6 col-lg-4">' +
            '<div class="form-group">' +
            '<label>Year of Completion</label>' +
            '<input type="text" class="form-control">' +
            '</div>' +
            '</div>' +
            '</div>' +
            '</div>' +
            '<div class="col-12 col-md-2 col-lg-1"><label class="d-md-block d-sm-none d-none">&nbsp;</label><a href="#" class="btn btn-danger trash"><i class="far fa-trash-alt"></i></a></div>' +
            '</div>';
        $(".education-info").append(educationcontent);
        return false;
    });
    $(".experience-info").on('click', '.trash', function() {
        $(this).closest('.experience-cont').remove();
        return false;
    });

    
    $(".add-experience").on('click', function() {
        var experiencecontent = '<div class="row form-row experience-cont">' +
          '<div class="col-12 col-md-10 col-lg-11">' +
          '<div class="row form-row">' +
          '<div class="col-12 col-md-6 col-lg-4">' +
          '<div class="form-group">' +
          '<label for="id_product_name">Nom Produit</label>' +
          '<input type="text" class="form-control" name="product_name">' +
          '</div>' +
          '</div>' +
          '<div class="col-12 col-md-6 col-lg-4">' +
          '<div class="form-group">' +
          '<label for="id_product_quantity">Quantity</label>' +
          '<input type="text" class="form-control" name="product_quantity">' +
          '</div>' +
          '</div>' +
          '<div class="col-12 col-md-6 col-lg-4">' +
          '<div class="form-group">' +
          '<label for="id_product_unit_price">Unit Price</label>' +
          '<input type="text" class="form-control" name="product_unit_price">' +
          '</div>' +
          '</div>' +
          '<div class="col-12 col-md-6 col-lg-4">' +
          '<div class="form-group">' +
          '<label for="id_total">Total</label>' +
          '<input type="text" class="form-control" name="total">' +
          '</div>' +
          '</div>' +
          '</div>' +
          '</div>' +
          '<div class="col-12 col-md-2 col-lg-1"><label class="d-md-block d-sm-none d-none">&nbsp;</label><a href="#" class="btn btn-danger trash"><i class="far fa-trash-alt"></i></a></div>' +
          '</div>';
        $(".experience-info").append(experiencecontent);
        return false;
    });
    
          
    $(".awards-info").on('click', '.trash', function() {
        $(this).closest('.awards-cont').remove();
        return false;
    });
    $(".add-award").on('click', function() {
        var regcontent = '<div class="row form-row awards-cont">' +
            '<div class="col-12 col-md-5">' +
            '<div class="form-group">' +
            '<label>Awards</label>' +
            '<input type="text" class="form-control">' +
            '</div>' +
            '</div>' +
            '<div class="col-12 col-md-5">' +
            '<div class="form-group">' +
            '<label>Year</label>' +
            '<input type="text" class="form-control">' +
            '</div>' +
            '</div>' +
            '<div class="col-12 col-md-2">' +
            '<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
            '<a href="#" class="btn btn-danger trash"><i class="far fa-trash-alt"></i></a>' +
            '</div>' +
            '</div>';
        $(".awards-info").append(regcontent);
        return false;
    });
    $(".membership-info").on('click', '.trash', function() {
        $(this).closest('.membership-cont').remove();
        return false;
    });
    $(".add-membership").on('click', function() {
        var membershipcontent = '<div class="row form-row membership-cont">' +
            '<div class="col-12 col-md-10 col-lg-5">' +
            '<div class="form-group">' +
            '<label>Memberships</label>' +
            '<input type="text" class="form-control">' +
            '</div>' +
            '</div>' +
            '<div class="col-12 col-md-2 col-lg-2">' +
            '<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
            '<a href="#" class="btn btn-danger trash"><i class="far fa-trash-alt"></i></a>' +
            '</div>' +
            '</div>';
        $(".membership-info").append(membershipcontent);
        return false;
    });
    $(".registrations-info").on('click', '.trash', function() {
        $(this).closest('.reg-cont').remove();
        return false;
    });
    $(".add-reg").on('click', function() {
        var regcontent = '<div class="row form-row reg-cont">' +
            '<div class="col-12 col-md-5">' +
            '<div class="form-group">' +
            '<label>Registrations</label>' +
            '<input type="text" class="form-control">' +
            '</div>' +
            '</div>' +
            '<div class="col-12 col-md-5">' +
            '<div class="form-group">' +
            '<label>Year</label>' +
            '<input type="text" class="form-control">' +
            '</div>' +
            '</div>' +
            '<div class="col-12 col-md-2">' +
            '<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
            '<a href="#" class="btn btn-danger trash"><i class="far fa-trash-alt"></i></a>' +
            '</div>' +
            '</div>';
        $(".registrations-info").append(regcontent);
        return false;
    });
})(jQuery);