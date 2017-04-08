from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from reposition import models
from backend.forms.product import ProductForm, ProductImage, ProCategoryForm, ProBusinessForm, ProServiceForm
from utils.upload_image import save_image
from utils.pager import paginator

res = {'status': True, 'data': None, 'message': None}
title_dict = {
    'p_category': '分类管理',
    'p_category_add': '分类管理',
    'p_category_edit': '分类修改 ',
    'p_category_del': '分类删除',
    'p_service': '服务管理',
    'p_service_add': '服务添加',
    'p_service_edit': '服务修改',
    'p_service_del': '服务删除',
    'p_business': '业务管理',
    'p_business_add': '业务添加',
    'p_business_edit': '业务修改',
    'p_business_del': '业务删除',
    'product': '我的产品',
    'product_add': '产品添加',
    'product_edit': '产品修改',
    'product_del': '产品删除'
}


def p_category(req):
    form = ProCategoryForm(req.POST or None)
    category_obj = models.ProductCategory.objects.all()
    cate_r_list = []
    cate_p_list = []
    cate_c_list = []
    for row in category_obj:
        if row.cate_rootid == 0 and row.cate_parentid != 0:
            cate_c_list.append(row)
        elif row.cate_rootid == 0:
            cate_r_list.append(row)
        else:
            cate_p_list.append(row)

    if req.method == 'POST':
        if form.is_valid():
            pass
            # models.ProductCategory.objects.create()
        else:
            print(form.errors)

    return render(req, 'product/p_category.html', {'form': form,
                                                   'title': title_dict['p_category'],
                                                   'cate_r_list': cate_r_list,
                                                   'cate_p_list': cate_p_list,
                                                   'cate_c_list': cate_c_list
                                                   })


# 服务管理
def p_service(req):
    service_obj = models.ProductService.objects.all().order_by('-ctime')
    posts = paginator(req, service_obj)
    return render(req, 'product/p_service.html', {'title': title_dict['p_service'],
                                                  'posts': posts})


# 服务添加
def p_service_add(req):
    form = ProServiceForm(req.POST or None)
    if req.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            data['employee_id'] = req.session.get('employee_id')
            models.ProductService.objects.create(**data)
            return redirect('p_service')
    return render(req, 'product/p_service_add.html', {'form': form,
                                                      'title': title_dict['p_service_add'],})


# 服务修改
def p_service_edit(req, id):
    service_obj = models.ProductService.objects.filter(id=id).first()
    form = ProServiceForm()
    if req.method == 'POST':
        form = ProServiceForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            return redirect('p_service')
            #
    return render(req, 'product/p_service_add.html', {'title': title_dict['p_service_edit'],
                                                      'form': form})


# 服务删除
def p_service_del(req, id):
    pass


# 业务管理
def p_business(req):
    business_obj = models.ProcessName.objects.all()
    posts = paginator(req, business_obj)
    processsep_obj = models.ProcessStep.objects.all().order_by('p_name_id', 'number')
    return render(req, 'product/p_business.html', {'title': title_dict['p_business'],
                                                   'posts': posts,
                                                   'processsep_obj': processsep_obj})


# 业务添加
def p_business_add(req):
    form = ProBusinessForm(req.POST or None)
    error = None
    if req.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            employee_id = req.session.get('employee_id')
            name_obj = models.ProcessName.objects.filter(name=name).first()
            if not name_obj:
                name_obj = models.ProcessName.objects.create(name=name, employee_id=employee_id)
                step_number = req.POST.getlist('step_number')
                step_name = req.POST.getlist('step_name')
                for step_number, step_name in zip(step_number, step_name):
                    data = {'employee_id': employee_id, 'p_name_id': name_obj.id, 'process_name': name}
                    data.update({'number': step_number, 'name': step_name})
                    models.ProcessStep.objects.create(**data)
                return redirect('p_business')
        else:
            error = list(form.errors.values())[0][0]

    return render(req, 'product/p_business_add.html', {'title': title_dict['p_business_add'],
                                                       'form': form,
                                                       'error': error})


# 业务修改
def p_business_edit(req, id):
    form = ProBusinessForm(req.POST or None)
    error = None
    process_obj = models.ProcessStep.objects.filter(p_name_id=id).all()

    if req.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            employee_id = req.session.get('employee_id')
            name_obj = models.ProcessName.objects.filter(id=id, name=process_obj[0].process_name).filter()
            if name_obj:
                name_obj = models.ProcessName.objects.filter(id=id).update(name=name)
                models.ProcessStep.objects.filter(p_name_id=id).all().delete()
                step_number = req.POST.getlist('step_number')
                step_name = req.POST.getlist('step_name')

                for step_number, step_name in zip(step_number, step_name):
                    data = {'employee_id': employee_id, 'p_name_id': id, 'process_name': name}
                    data.update({'number': step_number, 'name': step_name})
                    models.ProcessStep.objects.create(**data)
                return redirect('p_business')
        else:
            error = list(form.errors.values())[0][0]
    return render(req, 'product/p_business_edit.html', {'title': title_dict['p_business_edit'],
                                                        'form': form,
                                                        'error': error,
                                                        'process_obj': process_obj})


from django.db import connection


def product(req):

    product_obj = models.Products.objects.order_by('-p_ctime')
    # product_obj = models.Products.objects.all().order_by('-p_ctime')
    posts = paginator(req, product_obj)

    return render(req, 'product/product.html', {'title': title_dict['product'],
                                                'posts':posts,
                                                })


# 添加产品
def product_add(req):
    form = ProductForm(req.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        data['p_employee_id'] = req.session.get('employee_id')
        product_obj = models.Products.objects.create(**form.cleaned_data)
        id = req.POST.get('p_t_imgae')
        models.ProductTImage.objects.filter(id=id).update(ul_product=product_obj)
        return redirect('articles_all')
    return render(req, 'product/product_add.html', {'form': form,
                                                    'title': title_dict['product_add'],
                                                    })


# 产品图片上传
def product_image_upload(req):
    res_dict = {'status': True, 'data': None, 'message': None}
    if req.method == 'POST':

        files = ProductImage(req.POST, req.FILES)
        if files.is_valid():
            img = req.FILES.get('img')
            data = save_image(img)
            if data:
                data['ul_employee_id'] = req.session.get('employee_id')
                image_obj = models.ProductTImage.objects.create(**data)
                res_dict['data'] = data['ul_url']
                res_dict['message'] = image_obj.id
                return JsonResponse(res_dict)
    res_dict['status'] = False
    return JsonResponse(res_dict)


# 产品修改
def product_edit(req, id):
    form = ProductForm(req.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        data['p_employee_id'] = req.session.get('employee_id')
        product_obj = models.Products.objects.create(**form.cleaned_data)
        id = req.POST.get('p_t_imgae')
        models.ProductCImage.objects.filter(id=id).update(ul_product=product_obj)
        return redirect('articles_all')
    return render(req, 'product/product_add.html', {'form': form,})


# 产品删除
def product_del(req, id):
    pass


def attribute(req):
    pass
