from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Accessory
from .forms import AccessoryForm

# Create your views here.

# READ — list all accessories
def accessory_list(request):
    accessories = Accessory.objects.all()
    return render(request, 'accessories/accessory_list.html', {'accessories': accessories})

# READ — single accessory detail
def accessory_detail(request, pk):
    accessory = get_object_or_404(Accessory, pk=pk)
    return render(request, 'accessories/accessory_detail.html', {'accessory': accessory})

# CREATE — staff only
@staff_member_required
def accessory_add(request):
    form = AccessoryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('accessory_list')
    return render(request, 'accessories/accessory_form.html', {'form': form, 'title': 'Add Accessory'})

# UPDATE — staff only
@staff_member_required
def accessory_edit(request, pk):
    accessory = get_object_or_404(Accessory, pk=pk)
    form = AccessoryForm(request.POST or None, request.FILES or None, instance=accessory)
    if form.is_valid():
        form.save()
        return redirect('accessory_detail', pk=pk)
    return render(request, 'accessories/accessory_form.html', {'form': form, 'title': 'Edit Accessory'})

# DELETE — staff only
@staff_member_required
def accessory_delete(request, pk):
    accessory = get_object_or_404(Accessory, pk=pk)
    if request.method == 'POST':
        accessory.delete()
        return redirect('accessory_list')
    return render(request, 'accessories/accessory_confirm_delete.html', {'accessory': accessory})